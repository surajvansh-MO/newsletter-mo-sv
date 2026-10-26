from PIL import Image

im = Image.open('newsletter26oct2026/test_375_current.png')
w, h = im.size

# Find logo in test_375_current.png
for y in range(0, 80):
    for x in range(w-1, -1, -1):
        p = im.getpixel((x, y))[:3]
        if p[0] > 230 and p[1] > 230 and p[2] > 230:
            print(f"White logo pixel found at x={x}, y={y}")
            break
