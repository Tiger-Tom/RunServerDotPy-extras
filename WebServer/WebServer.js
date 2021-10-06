window.onload = function() {
    fetch('localhost:{%PORT}').then(response => response.text()).then(data => console.log(data))
}
