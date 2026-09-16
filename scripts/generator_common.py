import os
from pathlib import Path

BASE_DIR = Path(r"c:\Users\ASUS\Desktop\Năm cuối\Prj thực tập\BinhAnAWS\content\5-Workshop")

# Helper to write index files
def write_section(subdir, num, title_vi, title_en, source, body_vi, body_en, images_vi=None, images_en=None, screenshot_vi=None, screenshot_en=None, weight=1):
    os.makedirs(subdir, exist_ok=True)
    if images_vi is None and screenshot_vi:
        images_vi = screenshot_vi
    if images_en is None and screenshot_en:
        images_en = screenshot_en
    
    # VI
    vi_path = subdir / "_index.vi.md"
    vi_content = f"""---
title: "{title_vi}"
date: 2026-08-25
weight: {weight}
chapter: false
pre: " <b> {num}. </b> "
---

# {num}. {title_vi}

"""
    vi_content += body_vi.strip() + "\n\n"
    if images_vi:
        vi_content += "---\n\n"
        if isinstance(images_vi, list):
            for cap, url in images_vi:
                vi_content += f"![{cap}]({url})\n\n*{cap}*\n\n"
        else:
            vi_content += images_vi.strip() + "\n\n"
    vi_path.write_text(vi_content, encoding="utf-8")

    # EN
    en_path = subdir / "_index.md"
    en_content = f"""---
title: "{title_en}"
date: 2026-08-25
weight: {weight}
chapter: false
pre: " <b> {num}. </b> "
---

# {num}. {title_en}

"""
    en_content += body_en.strip() + "\n\n"
    if images_en:
        en_content += "---\n\n"
        if isinstance(images_en, list):
            for cap, url in images_en:
                en_content += f"![{cap}]({url})\n\n*{cap}*\n\n"
        else:
            en_content += images_en.strip() + "\n\n"
    en_path.write_text(en_content, encoding="utf-8")
    print(f"Generated: {num} -> {subdir.name}")

def write_parent(chapter_dir, num, title_vi, title_en, desc_vi, desc_en, sub_list, weight):
    # VI
    vi_path = chapter_dir / "_index.vi.md"
    toc_vi = "\n".join([f"- [**{item['num']}. {item['title_vi']}**](./{item['dir']}/): {item.get('summary_vi', '')}" for item in sub_list])
    vi_content = f"""---
title: "{title_vi}"
date: 2026-08-25
weight: {weight}
chapter: false
pre: " <b> {num}. </b> "
---

# {num}. {title_vi}

{desc_vi.strip()}

---

### Danh sách các bước triển khai trong mục {num}:

{toc_vi}

---
*Vui lòng chọn từng mục con ở menu bên trái hoặc liên kết phía trên để xem hướng dẫn chi tiết kèm mã nguồn và lệnh thực thi.*
"""
    vi_path.write_text(vi_content, encoding="utf-8")

    # EN
    en_path = chapter_dir / "_index.md"
    toc_en = "\n".join([f"- [**{item['num']}. {item['title_en']}**](./{item['dir']}/): {item.get('summary_en', '')}" for item in sub_list])
    en_content = f"""---
title: "{title_en}"
date: 2026-08-25
weight: {weight}
chapter: false
pre: " <b> {num}. </b> "
---

# {num}. {title_en}

{desc_en.strip()}

---

### Step-by-Step Implementation in Section {num}:

{toc_en}

---
*Please select each sub-section from the left sidebar or the links above to view detailed instructions, source code, and verification commands.*
"""
    en_path.write_text(en_content, encoding="utf-8")
    print(f"Generated parent: {num} -> {chapter_dir.name}")
