import glob
import re

html_files = glob.glob("*.html")

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace broken onerror attributes with a bulletproof template literal version
    # We will match the whole onerror string and replace it.
    
    # 1. Image slash fallback
    bad_slash = r'onerror="this\.outerHTML=\\\'<i class=\\\'fa-duotone fa-solid fa-image-slash\\\' style=\\\'font-size: (\d+)rem; color: var\(--gray-400\); width: 100%; display: flex; align-items: center; justify-content: center; min-height: 100px;\\\'></i>\\\'"'
    # Or maybe they look like this now:
    # onerror="this.outerHTML='<i class=\'fa-duotone fa-image-slash\' ... ></i>'"
    
    # Let's just blindly regex replace the entire onerror attribute with something clean.
    content = re.sub(
        r'onerror="this\.outerHTML=[^"]+"',
        lambda m: m.group(0).replace(r"\'", "'").replace(r"\'", "'"),  # Clean up multiple escapes if exist
        content
    )
    
    # Let's do a more robust cleanup: remove ANY current onerror related to these icons, and rebuild it perfectly.
    content = re.sub(r'\s*onerror="this\.outerHTML=[^"]+"', '', content)
    
    # Add back the correct onerror
    def add_onerror(match):
        img_tag = match.group(0)
        # If it's a team avatar placeholder
        if 'assets/placeholder.png' in img_tag:
            return img_tag[:-1] + r' onerror="this.outerHTML=\`<i class=\'fa-duotone fa-solid fa-user\' style=\'font-size: 4rem; color: var(--primary-color); display: flex; align-items: center; justify-content: center; height: 100%;\'></i>\`">'
        # Otherwise normal image
        return img_tag[:-1] + r' onerror="this.outerHTML=\`<i class=\'fa-duotone fa-solid fa-image-slash\' style=\'font-size: 2rem; color: var(--gray-400); width: 100%; display: flex; align-items: center; justify-content: center; min-height: 100px;\'></i>\`">'
        
    content = re.sub(r'<img\s+[^>]+>', add_onerror, content)
    
    # Fix the index.html curve
    if file_path == "index.html":
        content = re.sub(
            r'<div class="hero-divider" aria-hidden="true">\s*<i class="fa-solid fa-arrow-down"></i>\s*</div>',
            r'''<div class="hero-divider" aria-hidden="true">
            <svg viewBox="0 0 1440 120" preserveAspectRatio="none">
                <path d="M0,64L80,80C160,96,320,128,480,122.7C640,117,800,75,960,58.7C1120,43,1280,53,1360,58.7L1440,64L1440,120L1360,120C1280,120,1120,120,960,120C800,120,640,120,480,120C320,120,160,120,80,120L0,120Z"></path>
            </svg>
        </div>''',
            content
        )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Done fixing HTML")
