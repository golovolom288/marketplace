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

function startCountdown(hours) {
    let time = hours * 60 * 60; // Переводим в секунды
    const hoursElement = document.getElementById("hours");
    const minutesElement = document.getElementById("minutes");
    const secondsElement = document.getElementById("seconds");

    function updateTimerDisplay() {
        let hrs = Math.floor(time / 3600);
        let mins = Math.floor((time % 3600) / 60);
        let secs = time % 60;

        hoursElement.textContent = String(hrs).padStart(2, '0');
        minutesElement.textContent = String(mins).padStart(2, '0');
        secondsElement.textContent = String(secs).padStart(2, '0');

        if (time > 0) {
            time--;
            setTimeout(updateTimerDisplay, 1000);
        } else {
            hoursElement.textContent = "00";
            minutesElement.textContent = "00";
            secondsElement.textContent = "00";
        }
    }

    updateTimerDisplay();
}

startCountdown(1);


