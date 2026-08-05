import re

with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# The hero banner td currently has background-image as a single PNG.
# We need to add a radial orange glow as a second background layer,
# positioned at top-right matching Figma: X:1516/1714px canvas = ~89% from left, Y:-397 = above top.
# For a 760px wide email, glow center ~105% right, ~-20% top.
# Opacity 80%, radial, warm orange (#C84000 → transparent).

# Find the style attribute of the hero banner td (it starts with background-color: #050505)
# and inject a radial-gradient as the first background-image layer.

old_bg_style = "background-size: cover; background-position: center center; background-repeat: no-repeat;"
new_bg_style = (
    "background-size: 100% 100%, cover; "
    "background-position: center center, center center; "
    "background-repeat: no-repeat, no-repeat;"
)

# Prepend the radial glow gradient before the existing url(...) background-image
# Strategy: replace 'background-image: url(' with 'background-image: radial-gradient(...), url('
old_bi_prefix = "background-image: url('"
new_bi_prefix = (
    "background-image: "
    "radial-gradient(circle at 108% -15%, rgba(210, 65, 0, 0.82) 0%, rgba(160, 38, 0, 0.45) 32%, rgba(100, 20, 0, 0.12) 55%, transparent 72%), "
    "url('"
)

if old_bi_prefix in code:
    code = code.replace(old_bi_prefix, new_bi_prefix, 1)
    print("Radial glow gradient injected successfully!")
else:
    print("ERROR: Could not find background-image prefix in generate.py")

# Also fix background-size/position/repeat to handle two layers
if old_bg_style in code:
    code = code.replace(old_bg_style, new_bg_style, 1)
    print("Background size/position/repeat updated for two layers!")
else:
    print("WARNING: Could not find old bg style — manually verify background-size etc.")

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Done!")
