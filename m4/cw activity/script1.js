function validate(e) {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const age = document.getElementById('age').value;
    const msgBox = document.getElementById('message').value;

    let message='';

    if (email==='') {
        message = 'Please enter an email.';
        msgBox.style.color ='red';
    } else if (pass === '')
}