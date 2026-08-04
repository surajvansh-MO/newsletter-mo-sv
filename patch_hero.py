import base64, re

with open('hero_b64.txt', 'r') as f:
    hero_b64 = f.read().strip()

hero_data_uri = 'data:image/png;base64,' + hero_b64

with open('generate.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any existing data URI inside the hero banner td background-image
# The hero td has background-color: #050505 or #080808
pattern = r"(background-color: #0[58]0[58]0[68]; padding: 35px 35px 40px 35px; background-image: )url\('[^']*'\)(; background-size: cover; background-position: center center; background-repeat: no-repeat;)"

replacement = r"\g<1>url('" + hero_data_uri + r"')\g<2>"

new_content, count = re.subn(pattern, replacement, content)

if count > 0:
    print(f'Replaced {count} occurrence(s) via regex!')
else:
    # Broader match
    pattern2 = r"url\('data:image/png;base64,[A-Za-z0-9+/=]*'\)(; background-size: cover; background-position: center center; background-repeat: no-repeat;)\n                    <!-- END HERO"
    # Even simpler: just replace all data URIs - identify hero vs cta by context
    # Find the hero td specifically
    hero_start = content.find('background-color: #050505; padding: 35px 35px 40px 35px')
    if hero_start == -1:
        hero_start = content.find('padding: 35px 35px 40px 35px')
    
    if hero_start > 0:
        # Find the url() within 500 chars of this position
        segment = content[hero_start:hero_start+700]
        url_match = re.search(r"url\('data:image/png;base64,[A-Za-z0-9+/=]*'\)", segment)
        if url_match:
            old_url = url_match.group(0)
            new_url = "url('" + hero_data_uri + "')"
            new_content = content.replace(old_url, new_url, 1)
            print('Replaced hero background via positional search!')
        else:
            print('url() not found near hero section')
            print(repr(segment[:200]))
    else:
        print('Hero td not found at all')
        new_content = content

with open('generate.py', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('generate.py updated.')
