import base64
from PIL import Image, ImageDraw

# Create 32x32 transparent PNG for Sun icon (Thursday)
img = Image.new("RGBA", (32, 32), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# Orange color #eb5423
color = (235, 84, 35, 255)

# Center circle
draw.ellipse([10, 10, 21, 21], outline=color, width=2)

# Rays
rays = [
    [(16, 4), (16, 7)],
    [(16, 24), (16, 27)],
    [(4, 16), (7, 16)],
    [(24, 16), (27, 16)],
    [(7, 7), (10, 10)],
    [(21, 21), (24, 24)],
    [(7, 24), (10, 21)],
    [(21, 10), (24, 7)]
]

for r in rays:
    draw.line(r, fill=color, width=2)

img.save("c:/Users/Admin/Desktop/newsletter/newsletter08aug26/icon-sun.png")

with open("c:/Users/Admin/Desktop/newsletter/newsletter08aug26/icon-sun.png", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

print("SUN_ICON_B64:")
print(f"data:image/png;base64,{b64}")
