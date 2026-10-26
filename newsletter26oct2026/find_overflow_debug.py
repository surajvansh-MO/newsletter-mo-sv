with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

debug_script = """
<div id="overflow-debug" style="position:fixed; top:0; left:0; background:yellow; color:black; z-index:99999; font-size:11px; max-height:100vh; overflow:auto; padding: 10px;"></div>
<script>
window.addEventListener('DOMContentLoaded', () => {
    const list = [];
    document.querySelectorAll('*').forEach(el => {
        if (el.id !== 'overflow-debug' && el.offsetWidth > 375) {
            list.push(el.tagName + (el.className ? '.' + el.className : '') + ' (offset=' + el.offsetWidth + ', scroll=' + el.scrollWidth + ') ' + (el.id ? '#' + el.id : ''));
        }
    });
    document.getElementById('overflow-debug').innerHTML = '<b>Overflowing elements:</b><br>' + list.slice(0, 30).join('<br>');
});
</script>
"""

temp_html = content.replace('</body>', debug_script + '</body>')
with open('temp_debug.html', 'w', encoding='utf-8') as f:
    f.write(temp_html)

import subprocess
cmd = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "--headless",
    "--disable-gpu",
    "--window-size=375,1200",
    "--screenshot=temp_debug.png",
    "temp_debug.html"
]
subprocess.run(cmd, check=True)
print("Rendered temp_debug.png successfully")
