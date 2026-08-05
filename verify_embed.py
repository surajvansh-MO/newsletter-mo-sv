import re, zipfile

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

srcs = re.findall(r'src=["\']([^"\']+)["\']', html)
non_base64 = [s for s in srcs if not s.startswith('data:')]

print("Non-Base64 images remaining:", non_base64)
print(f"Total Base64 images embedded: {len(srcs) - len(non_base64)}")

# Re-zip cleanly
with zipfile.ZipFile('newsletter_package.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write('index.html')

print("newsletter_package.zip updated!")
