import os
import re

DOCS_DIR = r"D:\AI\gemeni\antigravity\scratch\cs55plus-manual\docs"

fixed_files = 0
for root, dirs, files in os.walk(DOCS_DIR):
    for f in files:
        if f.endswith(".md"):
            fpath = os.path.join(root, f)
            with open(fpath, "r", encoding="utf-8") as file:
                content = file.read()

            # Regex to find <div class="step-title">...<span>...</span></div> spanning multiple lines
            pattern = re.compile(r'(<div class="step-title"><span class="step-badge">[^<]+</span>\s*<span>)([\s\S]*?)(</span></div>)')
            
            def repl(m):
                prefix = m.group(1)
                body = m.group(2)
                suffix = m.group(3)
                if "\n" in body:
                    clean_body = re.sub(r"\s+", " ", body).strip()
                    return f"{prefix}{clean_body}{suffix}"
                return m.group(0)

            new_content, count = pattern.subn(repl, content)
            if count > 0 and new_content != content:
                with open(fpath, "w", encoding="utf-8") as file:
                    file.write(new_content)
                fixed_files += 1
                print(f"Fixed {count} instances in {f}")

print(f"Done. Sanitized {fixed_files} files.")
