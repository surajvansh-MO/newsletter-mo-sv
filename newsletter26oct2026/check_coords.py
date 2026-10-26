from PIL import Image

im = Image.open('test_375_current.png')
w, h = im.size
print(f"Image size: {w}x{h}")

# Check row around y = 400 (which is in the white body copy area)
# In test_375_current.png, where does white background begin and end?
white_pixels = []
for x in range(w):
    pixel = im.getpixel((x, 350))
    if pixel[0] > 250 and pixel[1] > 250 and pixel[2] > 250:
        white_pixels.append(x)

if white_pixels:
    print(f"White background at y=350 spans from x={min(white_pixels)} to x={max(white_pixels)} (width={max(white_pixels)-min(white_pixels)+1})")
else:
    print("No white background at y=350")
