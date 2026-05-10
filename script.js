function register() {
    let user = document.getElementById("username").value;
    let pass = document.getElementById("password").value;

    localStorage.setItem(user, pass);
    alert("Registered Successfully!");
    window.location.href = "login.html";
}

function login() {
    let user = document.getElementById("loginUser").value;
    let pass = document.getElementById("loginPass").value;

    let storedPass = localStorage.getItem(user);

    if (storedPass === pass) {
        alert("Login Successful!");
        window.location.href = "dashboard.html";
    } else {
        alert("Invalid Credentials");
    }
}

function logout() {
    alert("Logged out!");
    window.location.href = "index.html";
}