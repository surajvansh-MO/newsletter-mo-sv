with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update text of bottom CTA to be a bit larger (from 20px to 23px)
code = code.replace(
    "font-size: 20px; line-height: 28px; font-weight: 600; color: #ffffff; font-family: 'Sora', 'Segoe UI', Arial, sans-serif; text-align: center; max-width: 440px; letter-spacing: -0.01em;",
    "font-size: 23px; line-height: 32px; font-weight: 600; color: #ffffff; font-family: 'Sora', 'Segoe UI', Arial, sans-serif; text-align: center; max-width: 460px; letter-spacing: -0.01em;"
)

# 2. Update button styling to have less corner radius (border-radius: 8px instead of 100px)
code = code.replace(
    'style="background: linear-gradient(90deg, #FF7A42 0%, #EE5A24 55%, #D44E1C 100%); border-radius: 100px; box-shadow: 0 4px 12px rgba(235, 84, 35, 0.3);"',
    'style="background: linear-gradient(90deg, #FF7A42 0%, #EE5A24 55%, #D44E1C 100%); border-radius: 8px; box-shadow: 0 4px 12px rgba(235, 84, 35, 0.3);"'
)
code = code.replace(
    'style="font-size: 13px; font-family: \'Sora\', \'Segoe UI\', Arial, sans-serif; font-weight: 600; color: #ffffff; text-decoration: none; padding: 10px 24px; border-radius: 100px; display: inline-block;"',
    'style="font-size: 13px; font-family: \'Sora\', \'Segoe UI\', Arial, sans-serif; font-weight: 600; color: #ffffff; text-decoration: none; padding: 10px 24px; border-radius: 8px; display: inline-block;"'
)

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Adjusted bottom CTA text size to 23px and button border radius to 8px!")
