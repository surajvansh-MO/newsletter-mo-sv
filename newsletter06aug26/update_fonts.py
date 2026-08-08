import re

with open('generate.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Count occurrences
old_font = "'Segoe UI', Arial, Helvetica, sans-serif"
new_font_body = "'Poppins', 'Segoe UI', Arial, Helvetica, sans-serif"

# Don't replace the ones already updated (Sora heading and Poppins subheading)
count = content.count(old_font)
print(f"Found {count} occurrences of Segoe UI font-family")

# Replace all remaining plain Segoe UI with Poppins
content = content.replace(old_font, new_font_body)
print(f"Replaced all with Poppins")

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! All body text now uses Poppins.")
