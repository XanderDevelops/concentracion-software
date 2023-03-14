function validateForm() {

    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    
    if (username == "" || password == "") {
        alert("Both username and password fields must be filled out");
        return false;
    }
    if (password.length < 8) {
        alert("Password must be at least 8 characters long");
        return false;
    }

    console.log(username);
    console.log(password);

    return true;
};

if (validateForm() = true){
    const request = new XMLHttpRequest();
    request.open('POST', `/ProcessUserInfo/${JSON.stringify(username, password)}`);
    request.send();
};

// let btn = document.getElementById("btn")
// btn.addEventListener('click' => {
//     validateForm();
//   });

