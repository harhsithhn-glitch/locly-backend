const BACKEND = "https://locly-backend.onrender.com";

// LOGIN
function login() {
    const phone = document.getElementById("phone").value;

    if (phone.length < 10) {
        document.getElementById("loginStatus").innerText = "Invalid phone";
    } else {
        document.getElementById("loginStatus").innerText = "Login success";
    }
}

// SAVE USER
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

    fetch(BACKEND + "/save_user", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("userMsg").innerText = data.message;
    });
}

// PAYMENT + BOOKING
function payNow() {

    var options = {
        key: "YOUR_RAZORPAY_KEY", // ⚠️ replace
        amount: 200000,
        currency: "INR",
        name: "LOCLY",
        description: "Guide Booking",
        handler: function () {

            let data = {
                name: document.getElementById("name").value,
                location: document.getElementById("location").value,
                date: document.getElementById("date").value,
                payment_status: "Paid"
            };

            fetch(BACKEND + "/book", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(data)
            })
            .then(res => res.json())
            .then(data => {
                document.getElementById("msg").innerText = data.message;
                loadBookings();
            });
        }
    };

    var rzp = new Razorpay(options);
    rzp.open();
}

// LOAD BOOKINGS
function loadBookings() {
    fetch(BACKEND + "/bookings")
    .then(res => res.json())
    .then(data => {
        let output = "";

        data.forEach(item => {
            output += `
                <p>
                    ${item.name} - ${item.location} - ${item.date}
                    (${item.payment_status})
                </p>
            `;
        });

        document.getElementById("bookingsList").innerHTML = output;
    });
}

loadBookings();