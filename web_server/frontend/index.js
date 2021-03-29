var x = document.getElementById("input-login").placeholder;

const options = {
    body: JSON.stringify(x)
}
fetch("/", options);




