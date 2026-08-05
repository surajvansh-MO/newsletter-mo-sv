with open('generate.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '<td align="left" style="background-color: #050505;' in line:
        lines[i] = '                        <td align="left" style="background-color: #050505; padding: 24px 28px 30px 28px;" class="mobile-padding">\n'

with open('generate.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Removed orange glow from Hero Banner in generate.py!")
