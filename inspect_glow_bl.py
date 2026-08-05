from PIL import Image
import os

brain_path = r"C:\Users\Admin\.gemini\antigravity-ide\brain\ea507e46-9aa2-4fae-b913-5643054f2eaa"
glow_bl_path = os.path.join(brain_path, "media__1785915350140.png")

img = Image.open(glow_bl_path)
print("glow_bl size:", img.size)
print("glow_bl mode:", img.mode)
