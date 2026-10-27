import subprocess
import os
import shutil
import tempfile
import re

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html = os.path.abspath('index.html')

for mode, size in [('desktop', '800,2600'), ('mobile', '375,3200')]:
    temp_dir = tempfile.mkdtemp()
    temp_ss = os.path.join(temp_dir, 'ss.png')
    cmd = [
        edge,
        '--headless=new',
        f'--user-data-dir={temp_dir}',
        f'--window-size={size}',
        f'--screenshot={temp_ss}',
        f'file:///{html}'
    ]
    subprocess.run(cmd, capture_output=True)
    out_file = f'rendered_{mode}.png'
    if os.path.exists(temp_ss):
        shutil.copy(temp_ss, out_file)
        print(f'Saved {out_file}')
    else:
        print(f'Failed to save {out_file}')
    shutil.rmtree(temp_dir, ignore_errors=True)
