with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Revert card corner radius to 20px
code = code.replace('border-radius: 24px;', 'border-radius: 20px;')

# Revert card padding to 38px 40px 34px 40px
code = code.replace('padding: 55px 40px 50px 40px;', 'padding: 38px 40px 34px 40px;')

# Revert button corner radius to 100px pill
code = code.replace('border-radius: 12px; box-shadow: 0 4px 14px rgba(235, 84, 35, 0.35);', 'border-radius: 100px; box-shadow: 0 4px 14px rgba(235, 84, 35, 0.35);')
code = code.replace('padding: 18px 41px; border-radius: 12px;', 'padding: 14px 41px; border-radius: 100px;')

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("generate.py CTA card styles reverted successfully!")
