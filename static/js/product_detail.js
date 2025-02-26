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
