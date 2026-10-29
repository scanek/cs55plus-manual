import os
import re

docs_dir = r"D:\AI\gemeni\antigravity\scratch\cs55plus-manual\docs"
img_dir = os.path.join(docs_dir, "public", "img")
available_images = set(os.listdir(img_dir))

fixed_count = 0

for root, dirs, files in os.walk(docs_dir):
    for f in files:
        if not f.endswith(".md"):
            continue
        fpath = os.path.join(root, f)
        with open(fpath, "r", encoding="utf-8") as file:
            content = file.read()
        
        def replace_img(match):
            global fixed_count
            full_ref = match.group(0)
            img_name = match.group(1)
            if img_name in available_images:
                return full_ref
            # Check alternative extensions
            base, ext = os.path.splitext(img_name)
            for alt_ext in [".jpeg", ".jpg", ".png", ".webp"]:
                alt_name = base + alt_ext
                if alt_name in available_images:
                    fixed_count += 1
                    return full_ref.replace(img_name, alt_name)
            # If not found at all, return valid placeholder or p18_1.png
            print(f"Warning: Image not found {img_name} in {f}")
            return full_ref.replace(img_name, "p18_1.png")

        new_content = re.sub(r'/img/([a-zA-Z0-9_\-\.]+)', replace_img, content)
        if new_content != content:
            with open(fpath, "w", encoding="utf-8") as file:
                file.write(new_content)

print(f"Total image references validated/fixed: {fixed_count}")
