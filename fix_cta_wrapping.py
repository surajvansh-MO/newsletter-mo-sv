with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Update max-width of bottom CTA text to 580px so it wraps perfectly into exactly 2 lines
code = code.replace(
    "max-width: 460px; letter-spacing: -0.01em;",
    "max-width: 580px; letter-spacing: -0.01em;"
)

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated bottom CTA text max-width to 580px for clean 2-line layout!")
