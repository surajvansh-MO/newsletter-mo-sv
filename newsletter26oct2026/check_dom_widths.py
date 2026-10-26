import subprocess, json

script = """
const all = document.querySelectorAll('*');
const wide = [];
all.forEach(el => {
    if (el.scrollWidth > 375) {
        wide.push({
            tag: el.tagName,
            id: el.id,
            cls: el.className,
            scrollWidth: el.scrollWidth,
            offsetWidth: el.offsetWidth,
            text: (el.innerText || '').substring(0, 30)
        });
    }
});
console.log(JSON.stringify(wide));
"""

# Let's run edge with --dump-dom or evaluate
# Or write a small html with a script that writes to a div, or just inspect
