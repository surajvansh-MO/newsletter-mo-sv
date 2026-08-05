with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Remove border from outer cream card
code = code.replace(
    'style="background-color: #fdf8f4; border-radius: 20px; border: 1px solid #fcefe6;"',
    'style="background-color: #fdf8f4; border-radius: 20px;"'
)

# 2. Remove border from inner white sub-card
code = code.replace(
    'style="background-color: #ffffff; border-radius: 12px; border: 1px solid #e4e4e7; width: 100%; box-shadow: 0 2px 8px rgba(0,0,0,0.02);"',
    'style="background-color: #ffffff; border-radius: 14px; width: 100%; box-shadow: 0 2px 8px rgba(0,0,0,0.04);"'
)

# 3. Increase font size of Beyond Consent to 22px and Data Discovery to 20px
code = code.replace(
    'font-size: 20px; line-height: 26px; font-weight: 700; color: #18181b;',
    'font-size: 22px; line-height: 28px; font-weight: 700; color: #18181b;'
)
code = code.replace(
    'font-size: 19px; line-height: 26px; font-weight: 600; color: #71717a;',
    'font-size: 20px; line-height: 28px; font-weight: 600; color: #71717a;'
)

# 4. Change Register Now button from 700 (bold) to 600 (semibold)
code = code.replace(
    'font-size: 11px; font-weight: 700; color: #ffffff; background-color: #eb5423;',
    'font-size: 11px; font-weight: 600; color: #ffffff; background-color: #eb5423;'
)

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated generate.py with clean rounded borders and updated typography!")
