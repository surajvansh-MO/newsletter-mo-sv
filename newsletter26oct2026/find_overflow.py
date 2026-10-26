# Let's check widths of each row inside the hero table:
# Row 1: Logo (align=right)
# Row 2: Live Webinar pill (align=left)
# Row 3: Headline 'Every Shipment Carries Personal Data'
# Row 4: Subtitle 'DPDP readiness for logistics, from pickup to proof of delivery'
# Row 5: Date-Time bar
# Row 6: CTA button

# Let's inspect Row 5 (Date-Time bar):
# <table class=\"date-time-bar\" ...>
# <tr class=\"date-time-row\">
# <td class=\"time-box-td\" style=\"padding: 10px 18px;\">... THURSDAY ...</td>
# <td class=\"time-box-sep\" style=\"padding: 0;\"><div style=\"width: 1px; ...\"></div></td>
# <td class=\"time-box-td\" style=\"padding: 10px 18px;\">... 29th OCTOBER 2026 ...</td>
# <td class=\"time-box-sep\" style=\"padding: 0;\"><div style=\"width: 1px; ...\"></div></td>
# <td class=\"time-box-td\" style=\"padding: 10px 18px;\">... 4:00 PM IST ...</td>
# </tr></table>

# What style does date-time-bar have inline?
# border: 1px solid rgba(255, 255, 255, 0.14); border-radius: 9.5px;
# And in CSS:
# .date-time-bar { width: auto !important; max-width: 100% !important; display: inline-table !important; }
# .time-box-td { display: table-cell !important; width: auto !important; padding: 7px 10px !important; text-align: center !important; }
# .time-box-text { font-size: 9.5px !important; letter-spacing: 0.05em !important; white-space: nowrap !important; }

# Let's calculate:
# 'THURSDAY' at 9.5px + 20px pad = ~75px
# '29th OCTOBER 2026' at 9.5px + 20px pad = ~130px
# '4:00 PM IST' at 9.5px + 20px pad = ~80px
# Total date-time-bar width = ~285px!
# 285px < 339px, so Date-Time bar is 285px.

# Now what about the rest of the page?
# What about 'What we will cover' card or Speaker card?
# Let's check in the rest of the page:
from PIL import Image
im = Image.open('newsletter26oct2026/test_375_current.png')
w, h = im.size
for y in range(0, h, 50):
    for x in range(w-1, -1, -1):
        if im.getpixel((x, y))[:3] != (242, 242, 242): # non-outer background
            if x > 360:
                print(f"Content reaches right edge x={x} at y={y}")
            break
