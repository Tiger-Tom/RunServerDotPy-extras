window.onload = function() {
    sock = new WebSocket('ws://localhost:{8079}');
    sock.onmessage = function() { document.body.innerHTML += '<br>'+event.data.replaceAll('\n', '<br>') };
    sock.onopen = function() { sock.send('Hello, server!') };
}
