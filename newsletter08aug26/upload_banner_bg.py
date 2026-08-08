import urllib.request
import urllib.parse
import uuid

file_path = 'C:/Users/Admin/.gemini/antigravity-ide/brain/ca787d38-4853-44dd-bfa5-469e95afe5f8/media__1786182202731.png'
boundary = '----WebKitFormBoundary' + uuid.uuid4().hex

with open(file_path, 'rb') as f:
    file_bytes = f.read()

body = []
body.append(f'--{boundary}'.encode())
body.append(b'Content-Disposition: form-data; name="reqtype"')
body.append(b'')
body.append(b'fileupload')

body.append(f'--{boundary}'.encode())
body.append(b'Content-Disposition: form-data; name="fileToUpload"; filename="hero_banner_bg.png"')
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
    result = resp.read().decode('utf-8')
    print("HERO_BANNER_BG_CATBOX_URL:", result.strip())
