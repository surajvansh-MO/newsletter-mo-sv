import subprocess
import os
import shutil
import tempfile

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

test_html = os.path.abspath(r'newsletter29oct2026\test_mq.html')
content = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body { background: white; font-size: 24px; }
@media (max-width: 480px) { body { background: #ffaaaa; } }
@media (max-width: 500px) { #box { color: green; } }
</style>
</head>
<body>
<div id="box">Info</div>
<script>
document.getElementById('box').innerText = 'w: ' + window.innerWidth + ' h: ' + window.innerHeight + ' m480: ' + window.matchMedia('(max-width: 480px)').matches;
</script>
</body>
</html>"""

with open(test_html, 'w', encoding='utf-8') as f:
    f.write(content)

for ws in ['400,600', '350,600', '300,600']:
    temp_dir = tempfile.mkdtemp()
    temp_ss = os.path.join(temp_dir, 'ss.png')
    cmd = [edge, '--headless=new', f'--user-data-dir={temp_dir}', f'--window-size={ws}', f'--screenshot={temp_ss}', f'file:///{test_html}']
    subprocess.run(cmd, capture_output=True)
    if os.path.exists(temp_ss):
        shutil.copy(temp_ss, rf'newsletter29oct2026\test_{ws.split(",")[0]}.png')
        print(f'Rendered test_{ws.split(",")[0]}.png')
    shutil.rmtree(temp_dir, ignore_errors=True)

if os.path.exists(test_html): os.remove(test_html)
