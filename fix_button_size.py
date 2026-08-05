with open('generate.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Reserve your spot' in line or ('font-size: 15px;' in line and 'padding: 14px 32px;' in line):
        lines[i] = lines[i].replace('font-size: 15px;', 'font-size: 13px;').replace('padding: 14px 32px;', 'padding: 10px 22px;')

with open('generate.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("CTA Button size updated successfully!")
