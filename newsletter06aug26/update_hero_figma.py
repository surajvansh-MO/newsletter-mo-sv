import re

with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update container width to 760px
code = code.replace('min-width: 700px;', 'min-width: 760px;')
code = re.sub(r'width="700"([^>]*email-container[^>]*)width: 700px; max-width: 700px;', r'width="760"\1width: 760px; max-width: 760px;', code)

# 2. Ensure Google Fonts link is included in head
if 'fonts.googleapis.com' not in code:
    code = code.replace('<title>What Happens After Consent? Exploring the Next Layer of DPDP</title>',
                         '<title>What Happens After Consent? Exploring the Next Layer of DPDP</title>\n    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet" />')

# 3. Hero Heading: Sora Bold 700, 32px, 130% line height, -0.02em letter spacing, white
code = re.sub(r'(<!-- HEADLINE -->.*?<h1 style=")[^"]*(")',
              r'\1margin: 0; font-size: 32px; line-height: 130%; font-weight: 700; color: #ffffff; text-align: left; font-family: \'Sora\', Arial, Helvetica, sans-serif; letter-spacing: -0.02em;\2',
              code, flags=re.DOTALL)

# 4. Hero Subheading: Sora Regular 400, 22px, 130% line height, -0.02em letter spacing, #a1a1aa
code = re.sub(r'(<!-- SUB-HEADLINE.*?<p style=")[^"]*(")',
              r'\1margin: 0; font-size: 22px; line-height: 130%; color: #a1a1aa; text-align: left; font-family: \'Sora\', Arial, Helvetica, sans-serif; font-weight: 400; letter-spacing: -0.02em;\2',
              code, flags=re.DOTALL)

# 5. Stat Badges: Background #1A1A1A, Stroke #383D49, Corner Radius 14px (Figma spec 19), border-collapse: separate
code = re.sub(r'style="background-color: #[0-9a-fA-F]+; border-radius: \d+px; border: 1px solid #[0-9a-fA-F]+;"',
              r'style="background-color: #1A1A1A; border-radius: 14px; border: 1px solid #383D49; border-collapse: separate;"',
              code)

# 6. Hero CTA Button: linear-gradient(90deg, #FF7A42 0%, #EE5A24 55%, #D44E1C 100%), border-radius 100px (Figma spec 1665)
code = re.sub(r'(<!-- HERO CTA PILL BUTTON -->.*?<td align="center" style=")[^"]*(")',
              r'\1background: linear-gradient(90deg, #FF7A42 0%, #EE5A24 55%, #D44E1C 100%); border-radius: 100px; box-shadow: 0 4px 14px rgba(235, 84, 35, 0.45);\2',
              code, flags=re.DOTALL)

code = re.sub(r'(<!-- HERO CTA PILL BUTTON -->.*?<a href="[^"]*" target="_blank" class="button-a" style=")[^"]*(")',
              r'\1font-size: 15px; font-family: \'Sora\', \'Poppins\', Arial, sans-serif; font-weight: 600; color: #ffffff; text-decoration: none; padding: 14px 32px; border-radius: 100px; display: inline-block;\2',
              code, flags=re.DOTALL)

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Hero Banner updated with exact Figma specs!")
