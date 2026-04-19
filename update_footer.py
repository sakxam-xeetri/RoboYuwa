import glob
import re

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Footer dummy links
    content = re.sub(r'<div class="footer-links">\s*<h4>Quick Links</h4>.*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<li><a href="[^"]*">Project Gallery</a></li>\s*', '', content)
    content = re.sub(r'<li><a href="[^"]*">Our Team</a></li>\s*', '', content)
    
    # Fix the other nav links
    content = content.replace('href="#programs"', 'href="programs.html"')
    content = content.replace('href="index.html#programs"', 'href="programs.html"')
    content = content.replace('href="#contact"', 'href="contact.html"')
    content = content.replace('href="index.html#contact"', 'href="contact.html"')

    # Fix contact
    content = content.replace("contact@roboyuwa.org", "roboyuwa@gmail.com")
    content = content.replace("+977 980-0000000", "+977 9749464658")
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Updated footer links and general links/emails")