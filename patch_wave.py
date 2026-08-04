import base64, re

# Read new base64
with open('cta_b64.txt', 'r') as f:
    new_b64 = f.read().strip()

new_data_uri = 'data:image/png;base64,' + new_b64

# Read generate.py
with open('generate.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any existing data:image/png;base64,... inside the CTA td background-image
# Use regex to find and replace the old base64 data URI
pattern = r"url\('data:image/png;base64,[^']*'\)"
replacement = "url('" + new_data_uri + "')"

new_content, count = re.subn(pattern, replacement, content)

if count > 0:
    print(f'Replaced {count} occurrence(s) successfully!')
else:
    print('Pattern not found!')
    idx = content.find('data:image')
    print('data:image found at:', idx)
    print(repr(content[idx:idx+60]) if idx > 0 else 'NOT FOUND')

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('generate.py updated.')
