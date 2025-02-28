import os
import telebot
from dotenv import load_dotenv
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
QR_CODE_PATH = os.getenv("QR_CODE_PATH")

bot = telebot.TeleBot(TOKEN)
user_data = {}
user_sessions = {}

def get_main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("🛍 Новый заказ"))
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Привет! Нажмите '🛍 Новый заказ', чтобы оформить покупку.\n\nЕсли хотите связаться с админом, используйте команду /contact.", reply_markup=get_main_menu())

@bot.message_handler(func=lambda message: message.text == "🛍 Новый заказ")
def new_order(message):
    bot.send_message(message.chat.id, "Отправьте скриншот вашей корзины 🛒.")
    user_data[message.chat.id] = {"step": "waiting_for_screenshot"}

@bot.message_handler(content_types=['photo'])
def handle_screenshot(message):
    user_id = message.chat.id

    if user_data.get(user_id, {}).get("step") == "waiting_for_screenshot":
        file_id = message.photo[-1].file_id
        user_data[user_id]["screenshot"] = file_id
        user_data[user_id]["step"] = "waiting_for_address"

        bot.send_message(user_id, "📍 Введите ваш адрес доставки:")
    else:
        bot.send_message(user_id, "⚠ Вы уже отправили заказ. Для нового заказа используйте '🛍 Новый заказ'.")

@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("step") == "waiting_for_address")
def handle_address(message):
    user_id = message.chat.id
    user_data[user_id]["address"] = message.text
    user_data[user_id]["step"] = "waiting_for_phone"

    bot.send_message(user_id, "📞 Введите ваш номер телефона:")

@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("step") == "waiting_for_phone")
def handle_phone(message):
    user_id = message.chat.id
    user_data[user_id]["phone"] = message.text
    user_data[user_id]["step"] = "waiting_for_payment"

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("💳 Оплатить по QR-коду"), KeyboardButton("💵 Оплатить при получении"))

    bot.send_message(user_id, "💰 Выберите способ оплаты:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("step") == "waiting_for_payment")
def handle_payment(message):
    user_id = message.chat.id
    payment_method = message.text

    if payment_method == "💳 Оплатить по QR-коду":
        user_data[user_id]["payment"] = "QR-код"
        user_data[user_id]["step"] = "waiting_for_payment_confirmation"

        with open(QR_CODE_PATH, "rb") as qr_code:
            bot.send_photo(user_id, qr_code, caption="📲 Оплатите по QR-коду и ждите подтверждения администратора.")

    elif payment_method == "💵 Оплатить при получении":
        user_data[user_id]["payment"] = "Наличные"
        user_data[user_id]["step"] = "waiting_for_admin_confirmation"

    send_order_to_admin(user_id)

def send_order_to_admin(user_id):
    data = user_data.get(user_id, {})
    if not data:
        return

    order_text = f"🛒 Новый заказ!\n\n"
    order_text += f"📍 Адрес: {data['address']}\n"
    order_text += f"📞 Телефон: {data['phone']}\n"
    order_text += f"💰 Оплата: {data['payment']}\n\n"

    screenshot_file_id = data.get("screenshot")
    if screenshot_file_id:
        bot.send_photo(ADMIN_ID, screenshot_file_id, caption=order_text)
    else:
        bot.send_message(ADMIN_ID, order_text)

@bot.message_handler(commands=['contact'])
def contact_admin(message):
    user_sessions[message.chat.id] = ADMIN_ID
    user_sessions[ADMIN_ID] = message.chat.id

    bot.send_message(ADMIN_ID, f"🔔 Новый запрос от пользователя {message.chat.id}.")
    bot.send_message(message.chat.id, "✅ Вы связаны с администратором. Напишите сообщение, и он его получит.\n\nДля выхода введите /stop")

@bot.message_handler(commands=['stop'])
def stop_chat(message):
    if message.chat.id in user_sessions:
        other_party = user_sessions.pop(message.chat.id)
        if other_party in user_sessions:
            del user_sessions[other_party]

        bot.send_message(message.chat.id, "❌ Беседа завершена. Вы можете снова написать /contact, чтобы связаться с админом.")
        bot.send_message(other_party, "❌ Собеседник завершил беседу.") if other_party != ADMIN_ID else None

@bot.message_handler(func=lambda message: message.chat.id in user_sessions and message.chat.id != ADMIN_ID)
def forward_to_admin(message):
    bot.send_message(ADMIN_ID, f"📩 Сообщение от {message.chat.id}:\n{message.text}")
    user_sessions[ADMIN_ID] = message.chat.id

@bot.message_handler(func=lambda message: message.chat.id == ADMIN_ID)
def reply_from_admin(message):
    user_id = user_sessions.get(ADMIN_ID)
    if user_id:
        bot.send_message(user_id, f"📩 Ответ от администратора:\n{message.text}")
    else:
        bot.send_message(ADMIN_ID, "⚠ Ошибка: пользователь не найден.")

if __name__ == '__main__':
    bot.polling(none_stop=True)
