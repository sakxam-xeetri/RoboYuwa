import glob
import re

for file in glob.glob("*.html"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove the team link
    content = re.sub(r'\s*<li><a href="team\.html"[^>]*>Our Team</a></li>', '', content)
    
    # Change "Support Us" link to "Our Team"
    content = re.sub(r'<li><a href="[^"]*contact"[^>]*>Support Us</a></li>', r'<li><a href="team.html" class="btn btn-primary btn-sm">Our Team</a></li>', content)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
print("Updated navbars in all HTML files.")
