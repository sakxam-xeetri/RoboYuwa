import glob
import re

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Update programs link
    content = re.sub(r'href="[^"]*#programs"', r'href="programs.html"', content)
    
    # Update contact.html email and phone
    content = re.sub(r'contact@roboyuwa\.org', 'roboyuwa@gmail.com', content)
    
    # Update footer dummy links
    content = re.sub(r'<div class="footer-col">\s*<h4>Quick Links.*?</ul>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="footer-col">\s*<h4>Resources.*?</ul>\s*</div>', '', content, flags=re.DOTALL)

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
print("Updated programs links, contact email, and removed footer dummy links.")
