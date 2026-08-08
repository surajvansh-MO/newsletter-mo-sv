with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Heading "This session is split into two parts:"
code = code.replace(
    "<h3 style=\"margin: 0; font-size: 17px; line-height: 24px; font-weight: 700; color: #18181b; font-family: 'Segoe UI', Arial, Helvetica, sans-serif;\">",
    "<h3 style=\"margin: 0; font-size: 24px; line-height: 32px; font-weight: 700; color: #18181b; font-family: 'Sora', 'Segoe UI', Arial, sans-serif; letter-spacing: -0.01em;\">"
)

# Update Card 1 & Card 2 border-radius to 16px and border to 1px solid #e4e4e7
code = code.replace(
    "style=\"background-color: #ffffff; border-radius: 12px; border: 1px solid #ebebeb; height: 100%;\"",
    "style=\"background-color: #ffffff; border-radius: 16px; border: 1px solid #e4e4e7; height: 100%; box-shadow: 0 2px 8px rgba(0,0,0,0.02);\""
)

# Update Card titles to 17px font-size
code = code.replace(
    "<h4 style=\"margin: 0 0 8px 0; font-size: 15px; line-height: 22px; font-weight: 700; color: #18181b; font-family: 'Segoe UI', Arial, Helvetica, sans-serif;\">",
    "<h4 style=\"margin: 0 0 8px 0; font-size: 17px; line-height: 24px; font-weight: 700; color: #18181b; font-family: 'Sora', 'Segoe UI', Arial, sans-serif;\">"
)

# Update Card paragraph text to 14px and #71717a
code = code.replace(
    "<p style=\"margin: 0; font-size: 13px; line-height: 21px; color: #52525b; font-family: 'Segoe UI', Arial, Helvetica, sans-serif;\">",
    "<p style=\"margin: 0; font-size: 14px; line-height: 22px; color: #71717a; font-family: 'Segoe UI', Arial, Helvetica, sans-serif;\">"
)

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated Two-Part section heading and card rounded corners in generate.py!")
