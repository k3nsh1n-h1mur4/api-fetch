const URL = 'http://127.0.0.1:5000/newUser'


function ValidateFieldEmpty() {
    const form = document.querySelector('form')
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        if(form.username.value === "" || form.password.value === "") {
            alert("Falta por llenar algún campo")
        }
    })
}

/*const form = document.querySelector('form')
form.addEventListener('submit', () => {
    let username = form.username.value;
    let password = form.password.value;
    window.localStorage.setItem('username', username)
    console.log(username, password)
    if(username === '')
        { console.log("sin usuario") }
    else if(password === '') { console.log("sin password") }
    const f = new FormData()
    f.append("username", username)
    f.append("password", password)
    fetch(URL, {
        "method": "POST",
        "body": f,
        //"headers" : {"Content-Type": "application/json"},
        //"body": JSON.stringify(f)
    })
})
*/

