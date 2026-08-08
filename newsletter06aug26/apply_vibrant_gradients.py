import base64
import re
import subprocess

# Let's get the original background image from git
git_cmd = ["git", "show", "9626ad9:generate.py"]
res = subprocess.run(git_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
code = res.stdout.decode('utf-8')

# Find first base64 url
matches = re.findall(r"url\('data:image/png;base64,([^\'\)]+)\'\)", code)
if not matches:
    print("Error: Could not find original base64 background image from git!")
    exit(1)

grid_base64 = matches[0]

with open("generate.py", "r", encoding="utf-8") as f:
    gen_code = f.read()

# Fallback replacement to be safe and avoid regex errors
lines = gen_code.split('\n')
replaced = False
for i, line in enumerate(lines):
    if '<!-- HERO BANNER SECTION' in line:
        for j in range(i+1, i+6):
            if '<td align="left"' in lines[j] and 'background-color: #050505' in lines[j]:
                lines[j] = f'                        <td align="left" style="background-color: #050505; background-image: radial-gradient(circle 396px at 0px 220px, rgba(238, 90, 36, 0.45) 0%, rgba(238, 90, 36, 0.2) 50%, rgba(238, 90, 36, 0) 100%), radial-gradient(circle 396px at 760px 40px, rgba(238, 90, 36, 0.45) 0%, rgba(238, 90, 36, 0.2) 50%, rgba(238, 90, 36, 0) 100%), url(\'data:image/png;base64,{grid_base64}\'); background-position: left top, left top, center; background-repeat: no-repeat, no-repeat, no-repeat; background-size: auto, auto, 100% 100%; padding: 24px 28px 30px 28px;" class="mobile-padding">'
                replaced = True
                break
        if replaced:
            break

if replaced:
    gen_code = '\n'.join(lines)
    print("Successfully replaced in generate.py!")
else:
    print("Error: Pattern replacement failed!")
    exit(1)

with open("generate.py", "w", encoding="utf-8") as f:
    f.write(gen_code)

print("generate.py successfully updated with figma-accurate vibrant glows!")
