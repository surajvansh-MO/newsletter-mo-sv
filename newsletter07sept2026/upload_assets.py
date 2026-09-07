import os
import urllib.request
import uuid
import json

files = [
    'SocialLink-fb.png',
    'SocialLink-world.png',
    'attend-live-icon.png',
    'banner-bg-img.png',
    'calender-icon.png',
    'clock-icon.png',
    'cta-bg.png',
    'dhruv-bhaskar-pic.png',
    'iPad Mini (landscape).png',
    'mo Logo.png',
    'rayees-bhat-pic.png',
    'socialLink-linkedin.png'
]

res_dir = r'c:\Users\Admin\Desktop\newsletter\newsletter07sept2026\resourcesfolder'
urls = {}

for fname in files:
    fpath = os.path.join(res_dir, fname)
    if not os.path.exists(fpath):
        print(f'Missing: {fname}')
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
    try:
        with urllib.request.urlopen(req) as resp:
            url = resp.read().decode('utf-8').strip()
            urls[fname] = url
            print(f'{fname} -> {url}')
    except Exception as e:
        print(f'Error uploading {fname}: {e}')

out_json = r'c:\Users\Admin\Desktop\newsletter\newsletter07sept2026\uploaded_urls.json'
with open(out_json, 'w') as f:
    json.dump(urls, f, indent=2)

print('--- FINISHED ---')
