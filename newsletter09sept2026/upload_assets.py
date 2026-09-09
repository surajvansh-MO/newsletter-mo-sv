import os
import urllib.request
import uuid
import json

res_dir = r'c:\Users\Admin\Desktop\newsletter\newsletter09sept2026\resources_folder'
files = [f for f in os.listdir(res_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.svg')) and f != 'test_banner_crop.png']

urls = {}
for fname in files:
    fpath = os.path.join(res_dir, fname)
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
        with urllib.request.urlopen(req, timeout=15) as resp:
            url = resp.read().decode('utf-8').strip()
            urls[fname] = url
            print(f'{fname} -> {url}')
    except Exception as e:
        print(f'Error uploading {fname}: {e}')

out_json = r'c:\Users\Admin\Desktop\newsletter\newsletter09sept2026\uploaded_urls.json'
with open(out_json, 'w') as f:
    json.dump(urls, f, indent=2)

print(f'Uploaded {len(urls)} files successfully!')
