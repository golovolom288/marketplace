document.addEventListener("DOMContentLoaded", () => {
    const cartContainer = document.getElementById("cart-items");
    const checkoutButton = document.getElementById("checkout");
    const emptyCartMessage = document.getElementById("empty-cart");

    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    
    if (cart.length === 0) {
        emptyCartMessage.style.display = "block";
        checkoutButton.style.display = "none";
    } else {
        emptyCartMessage.style.display = "none";
        checkoutButton.style.display = "block";

        cart.forEach((product, index) => {
            let cartItem = document.createElement("div");
            cartItem.className = "cart-item";
            cartItem.innerHTML = `
                <img src="${product.image}" alt="${product.name}" class="cart-img">
                <div>${product.name} - ${product.price} ₽</div>
                <button class="remove-item" data-index="${index}">✖</button>
            `;
            cartContainer.appendChild(cartItem);
        });

        document.querySelectorAll(".remove-item").forEach((button) => {
            button.addEventListener("click", function () {
                let index = this.getAttribute("data-index");
                cart.splice(index, 1);
                localStorage.setItem("cart", JSON.stringify(cart));
                location.reload();
            });
        });
    }

    checkoutButton.addEventListener("click", () => {
        alert("Оплата прошла успешно!");
        localStorage.removeItem("cart");
        location.reload();
    });
});
