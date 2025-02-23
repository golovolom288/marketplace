document.addEventListener('DOMContentLoaded', () => {
  const languageSwitch = document.querySelector('.footer-language');
  const languageMenu = document.querySelector('.language-menu');

  // Переключение отображения меню
  languageSwitch.addEventListener('click', (e) => {
      e.stopPropagation(); // Останавливаем всплытие события
      languageSwitch.classList.toggle('active'); // Добавляем/убираем класс active
  });

  // Останавливаем всплытие кликов внутри меню
  languageMenu.addEventListener('click', (e) => {
      e.stopPropagation(); // Останавливаем всплытие, чтобы меню не закрывалось
  });

  // Закрытие меню при клике вне области
  document.addEventListener('click', (e) => {
      // Проверяем, находится ли клик за пределами переключателя и меню
      if (!languageSwitch.contains(e.target)) {
          languageSwitch.classList.remove('active');
      }
  });


});