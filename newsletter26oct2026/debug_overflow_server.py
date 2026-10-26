import http.server
import socketserver
import threading
import subprocess
import json
import os

results = []

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/report':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            results.append(data)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass # suppress logs

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

injected = """
<script>
window.addEventListener('load', () => {
    const list = [];
    const winW = window.innerWidth;
    document.querySelectorAll('*').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.right > winW + 1 || el.scrollWidth > winW + 1) {
            list.push({
                tag: el.tagName,
                className: el.className ? el.className.toString() : '',
                id: el.id || '',
                right: Math.round(r.right),
                width: Math.round(r.width),
                scrollW: el.scrollWidth,
                text: (el.innerText || '').substring(0, 35).replace(/\\s+/g, ' ')
            });
        }
    });
    fetch('/report', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            winW: winW,
            docScrollW: document.documentElement.scrollWidth,
            bodyScrollW: document.body.scrollWidth,
            overflowing: list
        })
    });
});
</script>
"""

test_html = html.replace('</body>', injected + '</body>')
with open('temp_test.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

server = socketserver.TCPServer(('127.0.0.1', 8999), Handler)
t = threading.Thread(target=server.serve_forever)
t.daemon = True
t.start()

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--window-size=375,800",
    "http://127.0.0.1:8999/temp_test.html"
]

subprocess.run(cmd, timeout=10)

import time
time.sleep(1)
server.shutdown()

if results:
    print("Received Report:")
    print(json.dumps(results[0], indent=2))
else:
    print("No report received")

# cleanup
if os.path.exists('temp_test.html'):
    os.remove('temp_test.html')
