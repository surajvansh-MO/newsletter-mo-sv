with open('generate.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '<td align="left" style="background-color: #050505;' in line:
        lines[i] = '                        <td align="left" style="background-color: #050505; padding: 24px 28px 30px 28px; background-image: radial-gradient(circle at 108% -15%, rgba(210, 65, 0, 0.82) 0%, rgba(160, 38, 0, 0.45) 32%, rgba(100, 20, 0, 0.12) 55%, transparent 72%); background-size: 100% 100%; background-position: center center; background-repeat: no-repeat;" class="mobile-padding">\n'

with open('generate.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Updated generate.py line 113 successfully!")
