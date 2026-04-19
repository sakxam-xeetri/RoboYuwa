import glob
import re

def fix_contact():
    with open('contact.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Remove inline background style that prevents rendering correctly and add page-header-bg div if missing
    # Search for: <section class="page-header" style="padding: 140px 0 60px; background: var(--dark); color: white; text-align: center;">
    # It seems there's no page-header-bg inside section in contact.html
    if '<div class="page-header-bg"></div>' not in content:
        content = re.sub(
            r'<section class="page-header"[^>]*>',
            '<section class="page-header">\n        <div class="page-header-bg"></div>',
            content
        )
    
    # Just to be safe, replace the inline style if it exists
    content = re.sub(r'style="padding:\s*140px[^"]*"', '', content)
    
    # Let's choose an image for contact.html: 'assets/homepage.jpg' or similar. 
    # Let's just fix the CSS in head:
    content = content.replace("url('assets/group photo.jpeg')", "url('assets/homepage.jpg')")

    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(content)

def fix_about_team_programs():
    # about.html -> 'assets/workshop.png'
    with open('about.html', 'r', encoding='utf-8') as f:
        about = f.read()
    about = about.replace("url('assets/group photo.jpeg')", "url('assets/workshop.png')")
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(about)

    # team.html -> 'assets/group photo.jpeg' (Keep as is, but encode spaces if needed. URL with spaces are fine in quotes)
    
    # programs.html -> 'assets/hackathon radar 2026.jpeg'
    with open('programs.html', 'r', encoding='utf-8') as f:
        prog = f.read()
    prog = prog.replace("url('assets/group photo.jpeg')", "url('assets/hackathon radar 2026.jpeg')")
    with open('programs.html', 'w', encoding='utf-8') as f:
        f.write(prog)

fix_contact()
fix_about_team_programs()
print("Images fixed!")
