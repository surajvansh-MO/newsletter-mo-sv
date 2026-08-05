import base64, os

def get_base64_uri(filepath):
    with open(filepath, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    ext = os.path.splitext(filepath)[1].lower().replace('.', '')
    if ext == 'jpg': ext = 'jpeg'
    return f"data:image/{ext};base64,{encoded_string}"

logo_b64 = get_base64_uri("miniorange-logo-transparent.png")
calendar_b64 = get_base64_uri("icon-calendar.png")
clock_b64 = get_base64_uri("icon-clock.png")

# Read generate.py
with open("generate.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace file paths with Base64 data URIs in generate.py
content = content.replace('src="miniorange-logo-transparent.png"', f'src="{logo_b64}"')
content = content.replace('src="icon-calendar.png"', f'src="{calendar_b64}"')
content = content.replace('src="icon-clock.png"', f'src="{clock_b64}"')

with open("generate.py", "w", encoding="utf-8") as f:
    f.write(content)

print("generate.py updated with embedded Base64 image URIs!")
