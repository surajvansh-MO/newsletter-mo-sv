with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Restore Headline font-size to 32px (matching Image 1 original)
code = code.replace(
    "font-size: 28px; line-height: 130%; font-weight: 700;",
    "font-size: 32px; line-height: 130%; font-weight: 700;"
)

# Restore Subheadline font-size to 22px (matching Image 1 original)
code = code.replace(
    "font-size: 28px; line-height: 130%; color: #a1a1aa;",
    "font-size: 22px; line-height: 130%; color: #a1a1aa;"
)

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated generate.py to match Image 1 original font sizes!")
