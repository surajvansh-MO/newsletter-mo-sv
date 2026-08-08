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

# Current style pattern in generate.py
# style="background-color: #050505; background-image: url('data:image/png;base64,...'), url('data:image/png;base64,...'); background-position: right top, left bottom; background-repeat: no-repeat, no-repeat; background-size: 180px 176px, 180px 274px; padding: 24px 28px 30px 28px;"
# Let's write a robust regex to replace it

pattern = r'style="background-color:\s*#050505;\s*background-image:\s*url\(\'data:image/png;base64,[^\']+\'\),\s*url\(\'data:image/png;base64,[^\']+\'\);\s*background-position:\s*right\s+top,\s*left\s+bottom;\s*background-repeat:\s*no-repeat,\s*no-repeat;\s*background-size:\s*\d+px\s+\d+px,\s*\d+px\s+\d+px;\s*padding:\s*24px\s+28px\s+30px\s+28px;"'

new_style = f'style="background-color: #050505; background-image: radial-gradient(circle 396px at 0px 591px, rgba(238, 90, 36, 0.5) 0%, rgba(238, 90, 36, 0) 100%), radial-gradient(circle 396px at 760px -100px, rgba(238, 90, 36, 0.5) 0%, rgba(238, 90, 36, 0) 100%), url(\'data:image/png;base64,{grid_base64}\'); background-position: left top, left top, center; background-repeat: no-repeat, no-repeat, no-repeat; background-size: auto, auto, 100% 100%; padding: 24px 28px 30px 28px;"'

code_new, count = re.subn(pattern, new_style, gen_code)
print(f"Replaced {count} occurrences in generate.py")

with open("generate.py", "w", encoding="utf-8") as f:
    f.write(code_new)

print("generate.py successfully updated with Figma-accurate radial gradients!")
