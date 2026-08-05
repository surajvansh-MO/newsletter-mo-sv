import re

with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Pattern to find radial-gradient + base64 png url in hero banner
pattern = r"background-image:\s*radial-gradient\([^)]+\),\s*url\('data:image/png;base64,[A-Za-z0-9+/=]+'\)"
match = re.search(pattern, code)

if match:
    # Keep only radial-gradient part
    url_idx = match.group(0).find(", url('")
    only_radial = match.group(0)[:url_idx]
    code = code[:match.start()] + only_radial + code[match.end():]
    
    # Fix background properties
    code = code.replace("background-size: 100% 100%, cover;", "background-size: 100% 100%;")
    code = code.replace("background-position: center center, center center;", "background-position: center center;")
    code = code.replace("background-repeat: no-repeat, no-repeat;", "background-repeat: no-repeat;")

    with open('generate.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Hero background successfully cleaned up in generate.py!")
else:
    print("Pattern not found! Checking if already clean...")

