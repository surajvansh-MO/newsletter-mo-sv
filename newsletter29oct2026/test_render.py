import subprocess
import os
import shutil
import tempfile

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html = os.path.abspath(r'newsletter29oct2026\index.html')

sizes = [
    ('desktop', '800,2600'),
    ('responsive_632', '632,2800'),
    ('mobile', '387,3000'),
    ('mobile_375', '375,3000')
]

for mode, size in sizes:
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
    out_file = os.path.join(r'newsletter29oct2026', f'rendered_{mode}.png')
    if os.path.exists(temp_ss):
        shutil.copy(temp_ss, out_file)
        print(f'Saved {out_file}')
    else:
        print(f'Failed to save {out_file}')
    shutil.rmtree(temp_dir, ignore_errors=True)
