var input = document.getElementById("key_pass");
var login = document.getElementById("loginid");

if(document.cookie === "") {
    document.cookie = "notloggedin";
} else {
    document.cookie = "loggedin";
}
if(document.cookie === "loggedin") {
    window.location.href = '/admin';
} 

addEventListener('keypress', function(event) {   // when the Enter key (13) is pressed, trigger a button click
    if (event.key === "Enter") {
        // Cancel the default action, if needed
        event.preventDefault();
        // Trigger the button element with a click
        document.getElementById("login").click();
      }
    })

const validate = function() {
    password = document.getElementById("key_pass").value;
    if(password === "ndcG-12514") {
        document.cookie = "loggedin";
        window.location.href = '/admin';
    } else {
        document.getElementById("key_pass").value = "";
        alert("Incorrect Password. Try again");
    }
}

