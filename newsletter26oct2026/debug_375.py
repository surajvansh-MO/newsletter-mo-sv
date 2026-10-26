from PIL import Image

im = Image.open('newsletter26oct2026/test_375_current.png')
w, h = im.size
print('Image width, height:', w, h)

# Let's see the width of the email container at 375px:
# In test_375_current.png, where is the body background #FFFFFF?
# Body has text 'Hi there,'. Let's see where the white background extends to on the right.
for y in range(400, 600, 50):
    row_colors = [im.getpixel((x, y))[:3] for x in range(w)]
    print(f'y={y}: left 5={row_colors[:5]}, right 5={row_colors[-5:]}')
