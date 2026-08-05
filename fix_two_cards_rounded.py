with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Update Card 1 & Card 2 table styles with border-collapse: separate to ensure crisp rounded corners
code = code.replace(
    'style="background-color: #ffffff; border-radius: 16px; border: 1px solid #e4e4e7; height: 100%; box-shadow: 0 2px 8px rgba(0,0,0,0.02);"',
    'style="background-color: #ffffff; border-radius: 16px; border: 1px solid #e4e4e7; border-collapse: separate; height: 100%;"'
)

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated Card table styles with border-collapse: separate!")
