document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".add-to-cart").forEach((button) => {
      button.addEventListener("click", function () {
          let product = {
              name: this.getAttribute("data-name"),
              price: this.getAttribute("data-price"),
              image: this.getAttribute("data-image")
          };

          let cart = JSON.parse(localStorage.getItem("cart")) || [];
          cart.push(product);
          localStorage.setItem("cart", JSON.stringify(cart));

          alert("Товар добавлен в корзину!");
      });
  });
});
