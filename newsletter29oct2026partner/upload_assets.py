import os
import urllib.request
import uuid
import json

res_dir = r'c:\Users\Admin\Desktop\newsletter\newsletter29oct2026partner\resources_folder'
files = [
    'miniorange_logo_top.png',
    'Group 7.png',
    'Frame 2147225204.png',
    'clock 1.png',
    'Frame 2147225375.png',
    'Frame 2147225384.png',
    'Frame 2147225385.png',
    'Frame 1562101659.png',
    'Frame 1562101659 (1).png',
    'Frame 1562101659 (2).png',
    'Frame 1562101659 (3).png',
    'Background.png',
    'close (1).png',
    'Line 1517 (1).png',
    'Icon.png'
]

urls = {}
for fname in files:
    fpath = os.path.join(res_dir, fname)
    if not os.path.exists(fpath):
        print(f'File not found: {fname}')
        continue
    boundary = '----WebKitFormBoundary' + uuid.uuid4().hex
    with open(fpath, 'rb') as f:
        file_bytes = f.read()
    
    ctype = 'image/png' if fname.endswith('.png') else ('image/jpeg' if fname.endswith(('.jpg', '.jpeg')) else 'image/svg+xml')
    body = []
    body.append(f'--{boundary}'.encode())
    body.append(b'Content-Disposition: form-data; name="reqtype"')
    body.append(b'')
    body.append(b'fileupload')
    body.append(f'--{boundary}'.encode())
    body.append(f'Content-Disposition: form-data; name="fileToUpload"; filename="{fname}"'.encode())
    body.append(f'Content-Type: {ctype}'.encode())
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
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            url = resp.read().decode('utf-8').strip()
            urls[fname] = url
            print(f'{fname} -> {url}')
    except Exception as e:
        print(f'Error uploading {fname}: {e}')

out_json = r'c:\Users\Admin\Desktop\newsletter\newsletter29oct2026partner\uploaded_urls.json'
with open(out_json, 'w') as f:
    json.dump(urls, f, indent=2)

print(f'Done! Uploaded {len(urls)} assets.')
