import re

with open('newsletter26oct2026/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    # Check for width > 300 or white-space nowrap
    if 'width=' in line or 'width:' in line or 'nowrap' in line:
        for match in re.finditer(r'(?:width=[\"\']?(\d+)[\"\']?|(?:width|min-width):\s*(\d+)px|nowrap)', line):
            val = match.group(0)
            num = match.group(1) or match.group(2)
            if num and int(num) > 300:
                print(f"Line {i+1} [wide: {num}]: {line.strip()[:100]}")
            elif 'nowrap' in val:
                print(f"Line {i+1} [nowrap]: {line.strip()[:100]}")
