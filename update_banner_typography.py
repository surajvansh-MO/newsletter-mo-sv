with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Heading: font-size 28px
code = code.replace(
    "font-size: 32px; line-height: 130%; font-weight: 700;",
    "font-size: 28px; line-height: 130%; font-weight: 700;"
)

# 2. Update Subheading: font-size 28px (same font size as heading!)
code = code.replace(
    "font-size: 22px; line-height: 130%; color: #a1a1aa;",
    "font-size: 28px; line-height: 130%; color: #a1a1aa;"
)

# 3. Update CTA Button: smaller size (font-size 13px, padding 10px 22px)
code = code.replace(
    "font-size: 15px; font-family: 'Sora', 'Poppins', Arial, sans-serif; font-weight: 600; color: #ffffff; text-decoration: none; padding: 14px 32px;",
    "font-size: 13px; font-family: 'Sora', 'Poppins', Arial, sans-serif; font-weight: 600; color: #ffffff; text-decoration: none; padding: 10px 22px;"
)

# 4. Stat badges: border-radius 8px with 1px solid #383d49
code = code.replace(
    "style=\"background-color: #1A1A1A; border-radius: 14px; border-collapse: separate;\"",
    "style=\"background-color: #1A1A1A; border-radius: 8px; border: 1px solid #383d49; border-collapse: separate;\""
)

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated banner typography and button size successfully in generate.py!")
