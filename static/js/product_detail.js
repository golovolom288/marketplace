document.addEventListener("DOMContentLoaded", function () {
  const mainPhoto = document.querySelector(".main-photo img");
  const thumbnails = document.querySelectorAll(".other-photos img");

  thumbnails.forEach(thumbnail => {
      thumbnail.addEventListener("click", function () {
          mainPhoto.src = this.src;
          mainPhoto.alt = this.alt;
      });
  });
});

document.getElementById("copyLink").addEventListener("click", function () {
  const pageUrl = window.location.href;
  navigator.clipboard.writeText(pageUrl).then(() => {
      alert("Ссылка скопирована!");
  }).catch(err => {
      console.error("Ошибка копирования: ", err);
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const zoomImage = document.getElementById("zoomImage");
  const zoomLens = document.querySelector(".zoom-lens");

  if (zoomImage && zoomLens) {
      zoomImage.addEventListener("mousemove", function (e) {
          const { left, top, width, height } = zoomImage.getBoundingClientRect();
          const lensSize = 80;
          const scale = 2;

          let x = e.clientX - left - lensSize / 2;
          let y = e.clientY - top - lensSize / 2;

          // Ограничиваем движение внутри изображения
          x = Math.max(0, Math.min(x, width - lensSize));
          y = Math.max(0, Math.min(y, height - lensSize));

          zoomLens.style.display = "block";
          zoomLens.style.left = `${x}px`;
          zoomLens.style.top = `${y}px`;

          zoomLens.style.backgroundImage = `url(${zoomImage.src})`;
          zoomLens.style.backgroundSize = `${width * scale}px ${height * scale}px`;
          zoomLens.style.backgroundPosition = `-${x * scale}px -${y * scale}px`;
      });

      zoomImage.addEventListener("mouseleave", function () {
          zoomLens.style.display = "none";
      });
  }
});