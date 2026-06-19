const products = [
    { id: 1, name: "Wireless Headphones", category: "Electronics", price: 79.99 },
    { id: 2, name: "USB-C Charging Cable", category: "Electronics", price: 12.99 },
    { id: 3, name: "Cotton T-Shirt", category: "Clothing", price: 19.99 },
    { id: 4, name: "Denim Jeans", category: "Clothing", price: 49.99 },
    { id: 5, name: "JavaScript Basics", category: "Books", price: 29.99 },
    { id: 6, name: "Web Development Guide", category: "Books", price: 34.99 },
    { id: 7, name: "Car Air Freshener", category: "Automobile Accessories", price: 8.99 },
    { id: 8, name: "Steering Wheel Cover", category: "Automobile Accessories", price: 24.99 }
];

let cart = [];

function addToCart(id) {
    const product = products.find(p => p.id === id);
    if (product) {
        cart.push(product);
        console.log(cart);
        updateCartDisplay();
    }
}

function removeFromCart(id) {
    const index = cart.findIndex(item => item.id === id);
    if (index !== -1) {
        cart.splice(index, 1);
    }
    updateCartDisplay();
}


function updateCartDisplay() {
    renderCart();
    updateTotal();
}

function updateTotal() {
    const total = cart.reduce((sum, item) => sum + item.price, 0);
    document.getElementById("totalAmount").textContent = `$${total.toFixed(2)}`;
}

function renderProducts(productList) {
    const productContainer = document.getElementById("productContainer");

    let html = "";

    productList.forEach(product => {
        html += `
            <div class="col-md-6 col-lg-4">
                <div class="card h-100">
                    <div class="card-body">
                        <h5 class="card-title">${product.name}</h5>
                        <p class="card-text">
                            <small class="text-muted">
                                Category: ${product.category}
                            </small>
                        </p>
                        <p class="card-text">
                            <strong>$${product.price.toFixed(2)}</strong>
                        </p>
                    </div>

                    <div class="card-footer bg-white border-top">
                        <button
                            class="btn btn-primary btn-sm w-100"
                            onclick="addToCart(${product.id})">
                            Add to Cart
                        </button>
                    </div>
                </div>
            </div>
        `;
    });

    productContainer.innerHTML = html;
}

function renderCart() {
    const cartItemsContainer = document.getElementById("cartItems");
    
    if (cart.length === 0) {
        cartItemsContainer.innerHTML = '<p class="text-muted">Cart is empty</p>';
        updateTotal();
        return;
    }
    
    let cartHTML = "<ul class=\"list-group list-group-flush\">";
    cart.forEach(item => {
        cartHTML += `
            <li class="list-group-item d-flex justify-content-between align-items-center">
                <div>
                    <strong>${item.name}</strong><br>
                    <small class="text-muted">$${item.price.toFixed(2)}</small>
                </div>
                <button class="btn btn-danger btn-sm" onclick="removeFromCart(${item.id})">Remove</button>
            </li>
        `;
    });
    cartHTML += "</ul>";
    cartItemsContainer.innerHTML = cartHTML;
}

document.addEventListener("DOMContentLoaded", () => {
    renderProducts(products);
    renderCart();
    updateTotal();
});

document.getElementById("categoryDropdown").addEventListener("change", function() {
    const filteredProducts = this.value === "" 
        ? products 
        : products.filter(product => product.category === this.value);
    renderProducts(filteredProducts);
});
