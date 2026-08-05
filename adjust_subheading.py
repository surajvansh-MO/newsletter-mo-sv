with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Update Subheading font-size from 22px to 25px
code = code.replace(
    "font-size: 22px; line-height: 130%; color: #a1a1aa;",
    "font-size: 25px; line-height: 130%; color: #a1a1aa;"
)

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated Subheading font-size to 25px in generate.py!")
