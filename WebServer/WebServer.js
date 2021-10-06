window.onload = function() {
    sock = new WebSocket('wss://localhost:{%PORT}');
    sock.onmessage = function() { document.body.innerHTML += '<br>'+event.data.replaceAll('\n', '<br>') };
    sock.onopen = function() { sock.send('Hello, server!') };
}
