import re

with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

with open('cta_b64.txt', 'r') as f:
    cta_b64 = f.read().strip()

# 1. Fix the CTA banner. It currently has a radial-gradient because of my previous bug.
# The CTA banner is near the bottom. Let's find it.
# It should be around line 430. We can just find the second radial-gradient and replace it.
matches = list(re.finditer(r'background-image:\s*radial-gradient\([^)]+\)', code))
if len(matches) == 2:
    m = matches[1]
    new_bg = "background-image: url('data:image/png;base64," + cta_b64 + "')"
    code = code[:m.start()] + new_bg + code[m.end():]
    print("Fixed CTA banner back to original base64.")
else:
    print("Warning: Did not find exactly 2 radial-gradients. Found:", len(matches))

# 2. Fix the Hero banner. It currently has radial-gradient AND url('data...')
# Let's find the hero banner line (starts with background-color: #050505)
hero_pattern = r'background-color: #050505; padding: 24px 28px 30px 28px; background-image: radial-gradient\([^)]+\), url\([^)]+\); background-size: 100% 100%, cover; background-position: center center, center center; background-repeat: no-repeat, no-repeat;'
match = re.search(hero_pattern, code)
if match:
    new_hero = 'background-color: #050505; padding: 24px 28px 30px 28px; background-image: radial-gradient(circle at 108% -15%, rgba(210, 65, 0, 0.82) 0%, rgba(160, 38, 0, 0.45) 32%, rgba(100, 20, 0, 0.12) 55%, transparent 72%); background-size: 100% 100%; background-position: center center; background-repeat: no-repeat;'
    code = code[:match.start()] + new_hero + code[match.end():]
    print("Fixed Hero banner to ONLY have radial-gradient.")
else:
    print("Hero banner pattern not found!")

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Done fixing background issues.")
