window.onload = function() {
    sock = new WebSocket('ws://localhost:{%PORT}');
    sock.addEventListener('message', function(event) {
        document.body.innerHTML += '<br>'+event.data.replaceAll('\n', '<br>');
    });
}
