from PIL import Image

im = Image.open('newsletter26oct2026/test_375_current.png')
# Find Live Webinar red dot: r > 180, g < 100
for y in range(50, 100):
    for x in range(0, 100):
        p = im.getpixel((x, y))[:3]
        if p[0] > 180 and p[1] < 100:
            print(f'Red dot at x={x}, y={y}')
            break
