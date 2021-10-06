window.onload = function() {
    sock = new WebSocket('ws://localhost:{%PORT}');
    sock.onopen = function() {
        sock.send('Connection opened!');
    }
    sock.onmessage = function(msg) {
        console.log(msg)
    }
}
