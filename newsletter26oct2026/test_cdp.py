import subprocess
import time
import json
import urllib.request

# Start Edge with remote debugging
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
proc = subprocess.Popen([
    edge_path,
    "--headless",
    "--disable-gpu",
    "--remote-debugging-port=9222",
    "--window-size=375,800",
    "http://127.0.0.1:8080/index.html"
])

# But first we need a simple http server, or file URL
# Let's see if file URL works
proc.kill()

import os
file_url = "file:///" + os.path.abspath("index.html").replace("\\", "/")

proc = subprocess.Popen([
    edge_path,
    "--headless",
    "--disable-gpu",
    "--remote-debugging-port=9222",
    "--window-size=375,800",
    file_url
])

time.sleep(2)
try:
    tabs = json.loads(urllib.request.urlopen("http://127.0.0.1:9222/json").read())
    print("Found tabs:", len(tabs))
    import urllib.request
    ws_url = tabs[0]["webSocketDebuggerUrl"]
    print("WS URL:", ws_url)
    
    # We can connect using python websockets or just evaluate via CDP if websocket installed
    import socket
    # or let's check if 'websockets' package is installed
except Exception as e:
    print("Error:", e)
finally:
    proc.kill()
