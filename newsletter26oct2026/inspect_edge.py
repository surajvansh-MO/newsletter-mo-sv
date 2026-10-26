from PIL import Image

im = Image.open('newsletter26oct2026/test_375_current.png')
w, h = im.size

# Let's inspect rows in hero section (y=0 to 300)
# Look at x=350 to 374 to see what has non-dark pixels (scrollbars, borders, or text overflow)
for y in range(0, 350, 20):
    edge_pixels = [im.getpixel((x, y))[:3] for x in range(350, 375)]
    print(f'Hero y={y}: x=350..374={edge_pixels[0]}, {edge_pixels[-5:]}')
