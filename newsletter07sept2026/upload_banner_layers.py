import os
import urllib.request
import uuid

files = ['banner-bg01.png', 'banner-bg02.png', 'banner-bg03.png']
res_dir = r'c:\Users\Admin\Desktop\newsletter\newsletter07sept2026\resourcesfolder'

for fname in files:
    fpath = os.path.join(res_dir, fname)
    if not os.path.exists(fpath):
        continue
    boundary = '----WebKitFormBoundary' + uuid.uuid4().hex
    with open(fpath, 'rb') as f:
        file_bytes = f.read()
    body = []
    body.append(f'--{boundary}'.encode())
    body.append(b'Content-Disposition: form-data; name="reqtype"')
    body.append(b'')
    body.append(b'fileupload')
    body.append(f'--{boundary}'.encode())
    body.append(f'Content-Disposition: form-data; name="fileToUpload"; filename="{fname}"'.encode())
    body.append(b'Content-Type: image/png')
    body.append(b'')
    body.append(file_bytes)
    body.append(f'--{boundary}--'.encode())
    body.append(b'')
    payload = b'\r\n'.join(body)
    
    req = urllib.request.Request(
        'https://catbox.moe/user/api.php',
        data=payload,
        headers={
            'Content-Type': f'multipart/form-data; boundary={boundary}',
            'User-Agent': 'Mozilla/5.0'
        }
    )
    with urllib.request.urlopen(req) as resp:
        url = resp.read().decode('utf-8').strip()
        print(f'{fname} -> {url}')
