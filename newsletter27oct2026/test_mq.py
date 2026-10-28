import subprocess, os, tempfile, shutil
from PIL import Image

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
temp_dir = tempfile.mkdtemp()
temp_html = os.path.join(temp_dir, 'test.html')
temp_ss = os.path.join(temp_dir, 'ss.png')

with open(temp_html, 'w') as f:
    f.write('''<!DOCTYPE html><html><head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head><body><div id="box"></div><script>document.getElementById("box").innerText = window.innerWidth;</script></body></html>''')

cmd = [edge, '--headless=new', f'--user-data-dir={temp_dir}', '--window-size=375,600', f'--screenshot={temp_ss}', f'file:///{temp_html}']
subprocess.run(cmd, capture_output=True)

if os.path.exists(temp_ss):
    shutil.copy(temp_ss, 'ss_test_mq.png')
    print('Copied to ss_test_mq.png')

shutil.rmtree(temp_dir, ignore_errors=True)
