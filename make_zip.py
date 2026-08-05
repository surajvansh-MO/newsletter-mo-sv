import re, os, zipfile

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all img src references
srcs = set(re.findall(r'src=["\']([^"\']+)["\']', html))
print('Image assets referenced in index.html:')
for s in srcs:
    print(' -', s)

# Create a clean ZIP archive with index.html and its required assets
zip_filename = 'newsletter_package.zip'
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write('index.html')
    for img in srcs:
        if not img.startswith('data:') and not img.startswith('http'):
            if os.path.exists(img):
                zf.write(img)

print(f'\nPackage created successfully: {zip_filename}')
