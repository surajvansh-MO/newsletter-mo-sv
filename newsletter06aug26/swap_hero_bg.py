import base64, re

with open('hero_b64.txt', 'r') as f:
    new_b64 = f.read().strip()

new_data_uri = 'data:image/png;base64,' + new_b64
new_url_str = "url('" + new_data_uri + "')"

with open('generate.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find ALL data URI occurrences and replace only the FIRST (hero banner)
pattern = r"url\('data:image/png;base64,[A-Za-z0-9+/=]+'\)"
matches = list(re.finditer(pattern, content))
print(f'Found {len(matches)} data URI occurrences')

if len(matches) >= 1:
    m = matches[0]
    content = content[:m.start()] + new_url_str + content[m.end():]
    print('Hero banner data URI replaced!')

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
