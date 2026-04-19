import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# add link after programs-grid
replacement = r'\1\n            <div style="text-align: center; margin-top: 3rem;">\n                <a href="programs.html" class="btn btn-primary" style="padding: 0.8rem 2rem; border-radius: 30px;">Explore All Programs &amp; Initiatives</a>\n            </div>'
content = re.sub(r'(<div class="programs-grid">.*?</div>\s*</div>)', replacement, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html to link to programs.html")