// 🔐 LOGIN (simple demo)
function login() {
    const phone = document.getElementById("phone").value;

    if (phone.length < 10) {
        document.getElementById("loginStatus").innerText = "Invalid phone!";
    } else {
        document.getElementById("loginStatus").innerText = "Login successful!";
    }
}

// 👤 SAVE USER
function saveUser() {
    let data = {
        name: document.getElementById("uname").value,
        phone: document.getElementById("phone").value,
        email: document.getElementById("email").value,
        dob: document.getElementById("dob").value,
        age: document.getElementById("age").value,
        gender: document.getElementById("gender").value,
        address: document.getElementById("address").value,
        emergency: document.getElementById("emergency").value
    };

    fetch("https://locly-backend.onrender.com/save_user", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("userMsg").innerText = data.message;
    });
}

// 📅 BOOKING
document.getElementById("bookingForm").addEventListener("submit", function(e) {
    e.preventDefault();

    let data = {
        name: document.getElementById("name").value,
        location: document.getElementById("location").value,
        date: document.getElementById("date").value
    };

    fetch("https://locly-backend.onrender.com/book", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("msg").innerText = data.message;
        loadBookings(); // refresh
    });
});

// 📋 LOAD BOOKINGS
function loadBookings() {
    fetch("https://locly-backend.onrender.com/bookings")
    .then(res => res.json())
    .then(data => {
        let output = "";

        data.forEach(item => {
            output += `
                <p>${item.name} - ${item.location} - ${item.date}</p>
            `;
        });

        document.getElementById("bookingsList").innerHTML = output;
    });
}

loadBookings();