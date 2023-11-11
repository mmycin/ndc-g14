let session = document.cookie;
var login = document.getElementById("loginid");

if(session === "notloggedin") {
    window.location.href = '/login';
}

if(session === "loggedin") {
    login.text = "Admin"; 
}