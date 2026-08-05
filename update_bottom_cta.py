with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the button style in the bottom CTA to make it a pill shape with border-radius: 100px
old_button_bg = '<td align="center" style="background-color: #eb5423; border-radius: 6px;">'
new_button_bg = '<td align="center" style="background: linear-gradient(90deg, #FF7A42 0%, #EE5A24 55%, #D44E1C 100%); border-radius: 100px; box-shadow: 0 4px 12px rgba(235, 84, 35, 0.3);">'

code = code.replace(old_button_bg, new_button_bg)

# Replace the button link style to make it compact pill button
old_button_a = 'class="button-a" style="font-size: 14px; font-family: \'Segoe UI\', Arial, Helvetica, sans-serif; font-weight: 600; color: #ffffff; text-decoration: none; padding: 12px 32px; border-radius: 6px; border: 1px solid #eb5423; display: inline-block; letter-spacing: 0.2px;">'
new_button_a = 'class="button-a" style="font-size: 13px; font-family: \'Sora\', \'Segoe UI\', Arial, sans-serif; font-weight: 600; color: #ffffff; text-decoration: none; padding: 10px 24px; border-radius: 100px; display: inline-block;">'

code = code.replace(old_button_a, new_button_a)

# Replace the text padding and styling to match font sizes and weights of original
old_text_p = '<p style="margin: 0; font-size: 18px; line-height: 28px; font-weight: 700; color: #ffffff; font-family: \'Segoe UI\', Arial, Helvetica, sans-serif; text-align: center; max-width: 380px;">'
new_text_p = '<p style="margin: 0; font-size: 20px; line-height: 28px; font-weight: 600; color: #ffffff; font-family: \'Sora\', \'Segoe UI\', Arial, sans-serif; text-align: center; max-width: 440px; letter-spacing: -0.01em;">'

code = code.replace(old_text_p, new_text_p)

# Let's adjust the padding of the bottom dark card to make its height and width exact match to Image 2 (less tall)
code = code.replace(
    'style="padding: 38px 40px 34px 40px; background-color: #0e1117;',
    'style="padding: 26px 40px 26px 40px; background-color: #0e1117;'
)

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated bottom CTA section styling to match Image 2 original!")
