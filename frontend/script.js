const BASE_URL = "https://ca-portal-backend-wokj.onrender.com";

function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch(`${BASE_URL}/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        if (data.message === "Login successful") {
            window.location.href = "dashboard.html";
        } else {
            alert("Invalid credentials");
        }
    });
}

function calculate() {
    const data = {
        purchase_cost: document.getElementById("purchase_cost").value,
        purchase_year: document.getElementById("purchase_year").value,
        sale_value: document.getElementById("sale_value").value,
        stamp_duty_value: document.getElementById("stamp_duty_value").value,
        sale_year: document.getElementById("sale_year").value,
        improvement_cost: document.getElementById("improvement_cost").value,
        improvement_year: document.getElementById("improvement_year").value,
        expenses: document.getElementById("expenses").value
    };

    fetch(`${BASE_URL}/calculate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        document.getElementById("result").innerText =
            `Tax Old: ${result.tax_old}, Tax New: ${result.tax_new}, Best: ${result.better_option}`;
    });
}

function loadFeature(feature) {

    let html = "";

    if (feature === "capital") {
        html = `
            <h2>Capital Gain Calculator</h2>

            <input id="purchase_cost" placeholder="Purchase Cost">
            <input id="purchase_year" placeholder="Purchase Year">

            <input id="sale_value" placeholder="Sale Value">
            <input id="stamp_duty_value" placeholder="Stamp Duty Value">
            <input id="sale_year" placeholder="Sale Year">

            <input id="improvement_cost" placeholder="Improvement Cost">
            <input id="improvement_year" placeholder="Improvement Year">

            <input id="expenses" placeholder="Expenses">

            <button onclick="calculate()">Calculate</button>

            <div id="result"></div>
        `;
    }

    else if (feature === "gst") {
        html = `
            <h2>GST Calculator</h2>
            <p>Coming Soon...</p>
        `;
    }

    else if (feature === "tax") {
        html = `
            <h2>Income Tax Calculator</h2>
            <p>Coming Soon...</p>
        `;
    }

    else if (feature === "normal") {
        html = `
            <h2>Normal Calculator</h2>
            <p>Coming Soon...</p>
        `;
    }

    document.getElementById("content").innerHTML = html;
}