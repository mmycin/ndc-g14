let login = document.getElementById("loginid");

let session = document.cookie;

console.log(session);
if(session === "loggedin") {
    login.text = "Admin"; 
} else if(session === "notloggedin") {
    login.text = "Login"; 
}
