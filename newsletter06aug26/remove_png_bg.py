import re

with open('generate.py', 'r', encoding='utf-8') as f:
    code = f.read()

# We need to remove the url('data:image/png;base64,...') from the background-image, leaving only the radial-gradient.
# And fix the background-size, background-position, background-repeat back to single values.

# The string we want to replace starts with:
# radial-gradient(circle at 108% -15%, rgba(210, 65, 0, 0.82) 0%, rgba(160, 38, 0, 0.45) 32%, rgba(100, 20, 0, 0.12) 55%, transparent 72%), url('data:image/png;base64,
# and ends with ')

# Let's just use regex to clean up the background-image and its associated properties.
pattern = r"background-image:\s*radial-gradient\([^)]+\),\s*url\('data:image/png;base64,[A-Za-z0-9+/=]+'\)"
match = re.search(pattern, code)

if match:
    # Just keep the radial-gradient part
    # Wait, the radial-gradient itself has parentheses. Let's just do a string replacement.
    
    # Find the start of url('
    url_start = match.group(0).find("url('")
    new_bg_image = match.group(0)[:url_start].strip().rstrip(',')
    code = code[:match.start()] + new_bg_image + code[match.end():]
    
    # Fix the properties
    code = code.replace("background-size: 100% 100%, cover;", "background-size: 100% 100%;")
    code = code.replace("background-position: center center, center center;", "background-position: center center;")
    code = code.replace("background-repeat: no-repeat, no-repeat;", "background-repeat: no-repeat;")

    with open('generate.py', 'w', encoding='utf-8') as f:
        f.write(code)
    print("Successfully removed base64 PNG and kept only the radial gradient!")
else:
    print("Could not find the pattern. Let's check if the base64 URL is there without radial gradient.")
    # If fix_glow wasn't run correctly or something else happened
    pattern2 = r"background-image:\s*url\('data:image/png;base64,[A-Za-z0-9+/=]+'\)"
    match2 = re.search(pattern2, code)
    if match2:
        new_bg_image = "background-image: radial-gradient(circle at 108% -15%, rgba(210, 65, 0, 0.82) 0%, rgba(160, 38, 0, 0.45) 32%, rgba(100, 20, 0, 0.12) 55%, transparent 72%)"
        code = code[:match2.start()] + new_bg_image + code[match2.end():]
        with open('generate.py', 'w', encoding='utf-8') as f:
            f.write(code)
        print("Replaced base64 PNG with pure radial gradient!")
    else:
        print("Could not find any base64 background-image either.")

