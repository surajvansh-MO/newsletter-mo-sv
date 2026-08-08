import re

# Read current generate.py
with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update container width to 760px
code = code.replace('min-width: 700px;', 'min-width: 760px;')
code = re.sub(r'width="700"([^>]*email-container[^>]*)width: 700px; max-width: 700px;', r'width="760"\1width: 760px; max-width: 760px;', code)

# 2. Add Google Fonts link if not present
if 'fonts.googleapis.com' not in code:
    code = code.replace('<title>What Happens After Consent? Exploring the Next Layer of DPDP</title>',
                         '<title>What Happens After Consent? Exploring the Next Layer of DPDP</title>\n    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet" />')

# 3. Hero Heading (Sora 700/800, 32px, 130% line height, -0.02em letter spacing)
code = re.sub(r'(<!-- HEADLINE -->.*?<h1 style=")[^"]*(")',
              r'\1margin: 0; font-size: 32px; line-height: 130%; font-weight: 700; color: #ffffff; text-align: left; font-family: \'Sora\', Arial, Helvetica, sans-serif; letter-spacing: -0.02em;\2',
              code, flags=re.DOTALL)

# 4. Hero Subheading (Sora 400, 22px, 130% line height, -0.02em letter spacing)
code = re.sub(r'(<!-- SUB-HEADLINE.*?<p style=")[^"]*(")',
              r'\1margin: 0; font-size: 22px; line-height: 130%; color: #a1a1aa; text-align: left; font-family: \'Sora\', Arial, Helvetica, sans-serif; font-weight: 400; letter-spacing: -0.02em;\2',
              code, flags=re.DOTALL)

# 5. Stat Badges (12px border-radius + border-collapse: separate)
code = code.replace('border-radius: 8px; border: 1px solid #28282b;', 'border-radius: 12px; border: 1px solid #28282b; border-collapse: separate;')

# 6. Hero CTA Button (Gradient + 100px pill)
code = code.replace('background-color: #eb5423; border-radius: 20px;', 'background: linear-gradient(90deg, #FF7A42 0%, #EE5A24 55%, #D44E1C 100%); border-radius: 100px;')

# 7. Featured Webinar Card ("Beyond Consent")
code = code.replace('border-radius: 16px;"', 'border-radius: 20px; border-collapse: separate;"')
code = code.replace('border-radius: 12px; border: 1px solid #f1f1f4;', 'border-radius: 16px; border: 1px solid #f1f1f4; border-collapse: separate;')

# 8. SVG Icons for Date & Time in Featured Card
cal_svg_b64 = "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNFQjU0MjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48cmVjdCB4PSIzIiB5PSI0IiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHJ4PSIyIiByeT0iMiI+PC9yZWN0PjxsaW5lIHgxPSIxNiIgeTE9IjIiIHgyPSIxNiIgeTI9IjYiPjwvbGluZT48bGluZSB4MT0iOCIgeTE9IjIiIHgyPSI8IiB5Mj0iNiI+PC9saW5lPjxsaW5lIHgxPSIzIiB5MT0iMTAiIHgyPSIyMSIgeTI9IjEwIj48L2xpbmU+PC9zdmc+"
clk_svg_b64 = "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgaGVpZ2h0PSI0MCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiNFQjU0MjQiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCI+PC9jaXJjbGU+PHBvbHlsaW5lIHBvaW50cz0iMTIgNiAxMiAxMiAxNiAxNCI+PC9wb2x5bGluZT48L3N2Zz4="

code = re.sub(r'alt="Date" width="16" height="16" style="display: block; width: 16px; height: 16px;"', 'alt="Date" width="22" height="22" style="display: block; width: 22px; height: 22px;"', code)
code = re.sub(r'alt="Time" width="16" height="16" style="display: block; width: 16px; height: 16px;"', 'alt="Time" width="22" height="22" style="display: block; width: 22px; height: 22px;"', code)

# 9. Section Heading ("This session is split into two parts:")
code = re.sub(r'(This session is split into two parts:.*?</h3>)', r'This session is split into two parts:\n                                        </h3>', code)
code = re.sub(r'(<!-- TWO-PART BREAKDOWN SECTION -->.*?<h3 style=")[^"]*(")',
              r'\1margin: 0; font-size: 22px; line-height: 28px; font-weight: 600; color: #18181b; font-family: \'Poppins\', Arial, Helvetica, sans-serif; letter-spacing: 0.02em;\2',
              code, flags=re.DOTALL)

# 10. Split Cards (Part 1 and Part 2)
code = code.replace('border-radius: 12px; border: 1px solid #ebebeb;', 'border-radius: 20px; border: 1px solid #d4d4d8; border-collapse: separate;')
code = code.replace('<h4 style="margin: 0 0 8px 0; font-size: 15px; line-height: 22px; font-weight: 700; color: #18181b; font-family: \'Poppins\', \'Segoe UI\', Arial, Helvetica, sans-serif;">',
                    '<h4 style="margin: 0 0 8px 0; font-size: 16px; line-height: 150%; font-weight: 600; color: #242424; font-family: \'Poppins\', Arial, Helvetica, sans-serif; letter-spacing: 0;">')

# 11. Dark CTA Card (Background #050c16, Corner radius 24px, Padding 55px top / 50px bottom for tall height, Button corner radius 12px, Padding 18px 41px)
code = code.replace('background-color: #0e1117; border-radius: 14px; overflow: hidden;', 'background-color: #050c16; border-radius: 24px; border-collapse: separate; overflow: hidden;')
code = code.replace('padding: 38px 40px 34px 40px; background-color: #0e1117;', 'padding: 55px 40px 50px 40px; background-color: #050c16;')

# CTA Text
code = re.sub(r'(<p style="[^"]*max-width: 380px;[^"]*">.*?Registrants will receive the recording, so<br />sign up even if the timing is tight\.</p>)',
              r'<p style="margin: 0; font-size: 22px; line-height: 124%; font-weight: 600; color: #ffffff; font-family: \'Sora\', Arial, Helvetica, sans-serif; text-align: center; letter-spacing: 0; max-width: 500px;">Registrants will receive the recording, so<br />sign up even if the timing is tight.</p>',
              code, flags=re.DOTALL)

# CTA Button (12px corner radius, padding 18px 41px)
code = re.sub(r'(<td align="center" style="background-color: #eb5423; border-radius: 6px;">.*?Register Today.*?</a>\s*</td>)',
              r'<td align="center" style="background: linear-gradient(90deg, #FF7A42 0%, #EE5A24 55%, #D44E1C 100%); border-radius: 12px; box-shadow: 0 4px 14px rgba(235, 84, 35, 0.35);">\n                                                                <a href="https://www.miniorange.com/webinar-register" target="_blank" class="button-a" style="font-size: 15px; font-family: \'Poppins\', Arial, Helvetica, sans-serif; font-weight: 600; color: #ffffff; text-decoration: none; padding: 18px 41px; border-radius: 12px; display: inline-block;">Register Today</a>\n                                                            </td>',
              code, flags=re.DOTALL)

# All body fonts -> Poppins
old_font = "'Segoe UI', Arial, Helvetica, sans-serif"
new_font_body = "'Poppins', 'Segoe UI', Arial, Helvetica, sans-serif"
code = code.replace(old_font, new_font_body)

# Write patched generate.py
with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("generate.py successfully patched with all Figma specs!")
