with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the Featured Card block (from line 245 to 315)
old_card_block = '''                    <!-- FEATURED WEBINAR CARD HIGHLIGHT (EXACT MATCH TO ORIGINAL PDF IMAGE 2) -->
                    <tr>
                        <td align="center" style="padding: 0 35px 30px 35px; background-color: #ffffff;" class="mobile-padding">
                            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #fdf8f4; border-radius: 16px;">
                                <tr>
                                    <td style="padding: 28px 30px;">
                                        <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                                            <tr>
                                                <!-- LEFT COLUMN: TITLE & SUBTITLE -->
                                                <td valign="top" class="mobile-stack" style="padding-right: 20px;">
                                                    <h2 style="margin: 0 0 10px 0; font-size: 22px; line-height: 28px; font-weight: 600; color: #3d2c1e; font-family: 'Segoe UI', Arial, Helvetica, sans-serif;">
                                                        Beyond Consent:
                                                    </h2>
                                                    <p style="margin: 0; font-size: 17px; line-height: 26px; font-weight: 400; color: #7a8694; font-family: 'Segoe UI', Arial, Helvetica, sans-serif;">
                                                        Data Discovery, Retention &amp;<br />Compliance Under DPDP
                                                    </p>
                                                </td>

                                                <!-- RIGHT COLUMN: WHITE SUB-CARD -->
                                                <td valign="top" width="200" class="mobile-stack" align="right">
                                                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="background-color: #ffffff; border-radius: 12px; border: 1px solid #f1f1f4; width: 100%; box-shadow: 0 2px 8px rgba(0,0,0,0.02);">
                                                        <tr>
                                                            <td style="padding: 16px 18px;">
                                                                <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                                                                    
                                                                    <!-- ROW 1: DATE WITH CALENDAR ICON -->
                                                                    <tr>
                                                                        <td style="padding-bottom: 12px; border-bottom: 1px solid #f1f1f4;">
                                                                            <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                                                                <tr>
                                                                                    <td valign="middle" style="padding-right: 8px;">
                                                                                        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAb0lEQVR4nO3V0QmAMAwE0MuRFZzAlRzTlZzAIfRXBGvR0PtI3mcbaMgFCpTs7K1gX+bjfjatm0XVE2JM34D1ZBjtuhNMH4H3juqvp2hZEeDD2CJRHYG3LmsJR+CQV6qBBkKM1QDEHNn/AqobKFA7AX8mGPvWsFJ2AAAAAElFTkSuQmCC" alt="Date" width="16" height="16" style="display: block; width: 16px; height: 16px;" />
                                                                                    </td>
                                                                                    <td valign="middle" style="font-size: 11px; font-weight: 600; color: #3d3d3d; font-family: 'Segoe UI', Arial, Helvetica, sans-serif; letter-spacing: 0.3px; white-space: nowrap;">
                                                                                        13TH AUGUST 2026
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>

                                                                    <!-- ROW 2: TIME WITH CLOCK ICON -->
                                                                    <tr>
                                                                        <td style="padding-top: 12px; padding-bottom: 14px; border-bottom: 1px solid #f1f1f4;">
                                                                            <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                                                                <tr>
                                                                                    <td valign="middle" style="padding-right: 8px;">
                                                                                        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAsklEQVR4nO1XwQ2EMAxLLFZgAlZiTFa6CW4I7otQQ3ESlEqHn01iu6GtgsiLf4d6ir7rsluxeftQnJol7DWi2cKsEfWIX5Gy+cqIM9/3bq1GCI45vbiVA8tArzCrDq3F3s68JlrnA1IMPLn7O12AFGPKImLv/zAdQKQ444xMUYKoCUgxwD4cHlxdbUgx0FrM7ELvYQNL4hW3ACtwdsuaCM8DQ0xEQ8yEQ0zFT/4XvJBq/ACb7XNrggw5AgAAAABJRU5ErkJggg==" alt="Time" width="16" height="16" style="display: block; width: 16px; height: 16px;" />
                                                                                    </td>
                                                                                    <td valign="middle" style="font-size: 11px; font-weight: 600; color: #3d3d3d; font-family: 'Segoe UI', Arial, Helvetica, sans-serif; letter-spacing: 0.3px; white-space: nowrap;">
                                                                                        4:00 PM IST
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>

                                                                    <!-- ROW 3: REGISTER NOW BUTTON -->
                                                                    <tr>
                                                                        <td style="padding-top: 14px;" align="left">
                                                                            <a href="https://www.miniorange.com/webinar-register" target="_blank" style="font-size: 11px; font-weight: 600; color: #ffffff; background-color: #eb5423; text-decoration: none; padding: 10px 18px; border-radius: 6px; display: inline-block; letter-spacing: 0.3px; text-transform: uppercase; font-family: 'Segoe UI', Arial, Helvetica, sans-serif;">
                                                                                REGISTER NOW
                                                                            </a>
                                                                        </td>
                                                                    </tr>

                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>'''

new_card_block = '''                    <!-- FEATURED WEBINAR CARD HIGHLIGHT (EXACT MATCH TO ORIGINAL PDF IMAGE 2) -->
                    <tr>
                        <td align="center" style="padding: 0 35px 25px 35px; background-color: #ffffff;" class="mobile-padding">
                            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #fdf8f4; border-radius: 20px; border: 1px solid #fcefe6;">
                                <tr>
                                    <td style="padding: 18px 24px;">
                                        <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                                            <tr>
                                                <!-- LEFT COLUMN: TITLE & SUBTITLE -->
                                                <td valign="middle" class="mobile-stack" style="padding-right: 20px;">
                                                    <h2 style="margin: 0 0 6px 0; font-size: 20px; line-height: 26px; font-weight: 700; color: #18181b; font-family: 'Sora', 'Segoe UI', Arial, sans-serif; letter-spacing: -0.01em;">
                                                        Beyond Consent:
                                                    </h2>
                                                    <p style="margin: 0; font-size: 19px; line-height: 26px; font-weight: 600; color: #71717a; font-family: 'Sora', 'Segoe UI', Arial, sans-serif; letter-spacing: -0.01em;">
                                                        Data Discovery, Retention &amp;<br />Compliance Under DPDP
                                                    </p>
                                                </td>

                                                <!-- RIGHT COLUMN: WHITE SUB-CARD -->
                                                <td valign="middle" width="210" class="mobile-stack" align="right">
                                                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="background-color: #ffffff; border-radius: 12px; border: 1px solid #e4e4e7; width: 100%; box-shadow: 0 2px 8px rgba(0,0,0,0.02);">
                                                        <tr>
                                                            <td style="padding: 12px 14px;">
                                                                <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">
                                                                    
                                                                    <!-- ROW 1: DATE WITH CALENDAR ICON -->
                                                                    <tr>
                                                                        <td style="padding-bottom: 8px; border-bottom: 1px solid #f4f4f5;">
                                                                            <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                                                                <tr>
                                                                                    <td valign="middle" style="padding-right: 8px;">
                                                                                        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAb0lEQVR4nO3V0QmAMAwE0MuRFZzAlRzTlZzAIfRXBGvR0PtI3mcbaMgFCpTs7K1gX+bjfjatm0XVE2JM34D1ZBjtuhNMH4H3juqvp2hZEeDD2CJRHYG3LmsJR+CQV6qBBkKM1QDEHNn/AqobKFA7AX8mGPvWsFJ2AAAAAElFTkSuQmCC" alt="Date" width="16" height="16" style="display: block; width: 16px; height: 16px;" />
                                                                                    </td>
                                                                                    <td valign="middle" style="font-size: 11px; font-weight: 700; color: #18181b; font-family: 'Sora', 'Segoe UI', Arial, sans-serif; letter-spacing: 0.3px; white-space: nowrap;">
                                                                                        13TH AUGUST 2026
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>

                                                                    <!-- ROW 2: TIME WITH CLOCK ICON -->
                                                                    <tr>
                                                                        <td style="padding-top: 8px; padding-bottom: 10px; border-bottom: 1px solid #f4f4f5;">
                                                                            <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                                                                <tr>
                                                                                    <td valign="middle" style="padding-right: 8px;">
                                                                                        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAsklEQVR4nO1XwQ2EMAxLLFZgAlZiTFa6CW4I7otQQ3ESlEqHn01iu6GtgsiLf4d6ir7rsluxeftQnJol7DWi2cKsEfWIX5Gy+cqIM9/3bq1GCI45vbiVA8tArzCrDq3F3s68JlrnA1IMPLn7O12AFGPKImLv/zAdQKQ444xMUYKoCUgxwD4cHlxdbUgx0FrM7ELvYQNL4hW3ACtwdsuaCM8DQ0xEQ8yEQ0zFT/4XvJBq/ACb7XNrggw5AgAAAABJRU5ErkJggg==" alt="Time" width="16" height="16" style="display: block; width: 16px; height: 16px;" />
                                                                                    </td>
                                                                                    <td valign="middle" style="font-size: 11px; font-weight: 700; color: #18181b; font-family: 'Sora', 'Segoe UI', Arial, sans-serif; letter-spacing: 0.3px; white-space: nowrap;">
                                                                                        4:00 PM IST
                                                                                    </td>
                                                                                </tr>
                                                                            </table>
                                                                        </td>
                                                                    </tr>

                                                                    <!-- ROW 3: REGISTER NOW BUTTON -->
                                                                    <tr>
                                                                        <td style="padding-top: 10px;" align="left">
                                                                            <a href="https://www.miniorange.com/webinar-register" target="_blank" style="font-size: 11px; font-weight: 700; color: #ffffff; background-color: #eb5423; text-decoration: none; padding: 8px 14px; border-radius: 8px; display: inline-block; letter-spacing: 0.3px; text-transform: uppercase; font-family: 'Sora', 'Segoe UI', Arial, sans-serif;">
                                                                                REGISTER NOW
                                                                            </a>
                                                                        </td>
                                                                    </tr>

                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>'''

if old_card_block in code:
    code = code.replace(old_card_block, new_card_block)
    with open('generate.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Featured Card updated successfully in generate.py!")
else:
    print("Old block not matched exactly, applying regex replace...")
    import re
    code = re.sub(
        r'<!-- FEATURED WEBINAR CARD HIGHLIGHT.*?<!-- END FEATURED WEBINAR CARD HIGHLIGHT',
        new_card_block.strip() + '\n                    <!-- END FEATURED WEBINAR CARD HIGHLIGHT',
        code,
        flags=re.DOTALL
    )
    with open('generate.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Featured Card updated via regex!")

