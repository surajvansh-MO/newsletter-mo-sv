# Let's inspect what happened in test_375_current.png:
from PIL import Image

im = Image.open('newsletter26oct2026/test_375_current.png')
# find top right where logo is:
# In test_375_current.png, where is the logo?
# Let's find all white pixels in y=0..60:
w, h = im.size
print('Width is', w)
white_xs = []
for y in range(15, 60):
    for x in range(w):
        if im.getpixel((x, y))[:3] > (230, 230, 230):
            white_xs.append(x)
print('White pixels x range in header:', min(white_xs) if white_xs else None, 'to', max(white_xs) if white_xs else None)
