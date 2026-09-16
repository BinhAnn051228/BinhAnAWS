import os
import glob
import re
import shutil
import struct
import zlib

def make_placeholder_png(width=800, height=450):
    pixels = []
    for y in range(height):
        row = bytearray()
        for x in range(width):
            if y < 36:
                # AWS Navy header
                row.extend((35, 47, 62))
            elif y == 36:
                # AWS Orange line
                row.extend((255, 153, 0))
            elif x < 2 or x >= width - 2 or y >= height - 2:
                # Outer border
                row.extend((209, 213, 219))
            elif (70 <= y <= 380) and (x == 50 or x == width - 50 or y == 70 or y == 380):
                # Inner container border
                row.extend((180, 195, 210))
            elif (70 < y < 380) and (50 < x < width - 50):
                # Inner area light background
                row.extend((248, 250, 252))
            else:
                # Canvas background
                row.extend((255, 255, 255))
        pixels.append(b'\x00' + bytes(row))

    raw = b''.join(pixels)
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    idat = zlib.compress(raw, level=6)
    png = (
        b'\x89PNG\r\n\x1a\n'
        + struct.pack('>I', len(ihdr)) + b'IHDR' + ihdr + struct.pack('>I', zlib.crc32(b'IHDR' + ihdr) & 0xffffffff)
        + struct.pack('>I', len(idat)) + b'IDAT' + idat + struct.pack('>I', zlib.crc32(b'IDAT' + idat) & 0xffffffff)
        + struct.pack('>I', 0) + b'IEND' + struct.pack('>I', zlib.crc32(b'IEND') & 0xffffffff)
    )
    return png

def main():
    base_dir = os.path.abspath('.')
    workshop_content_dir = os.path.join(base_dir, 'content', '5-Workshop')
    static_images_base = os.path.join(base_dir, 'static', 'images', '5-Workshop')

    placeholder_bytes = make_placeholder_png()

    vi_pattern = re.compile(r'(> \*\*\[📝 Ảnh chụp đề xuất\]\*\*\s*\n>\s*(.*?))(\n\n!\[.*?\]\(.*?\))?(\s*)$', re.DOTALL)
    en_pattern = re.compile(r'(> \*\*\[📝 Recommended Screenshot\]\*\*\s*\n>\s*(.*?))(\n\n!\[.*?\]\(.*?\))?(\s*)$', re.DOTALL)

    subdirs = sorted([p for p in glob.glob(os.path.join(workshop_content_dir, '*', '*')) if os.path.isdir(p)])
    print(f'Processing {len(subdirs)} sub-lessons...')

    arch_src = os.path.join(base_dir, 'static', 'images', '2-Proposal', 'FCAJ_AWS_DevSecOps_Recommended_Architecture_v6.png')

    count_folders = 0
    count_images = 0
    count_vi_updated = 0
    count_en_updated = 0

    for s in subdirs:
        chap = os.path.basename(os.path.dirname(s))
        sub = os.path.basename(s)

        img_dir = os.path.join(static_images_base, chap, sub)
        os.makedirs(img_dir, exist_ok=True)
        count_folders += 1

        img_file = os.path.join(img_dir, 'screenshot.png')
        if not os.path.exists(img_file):
            if sub == '5.1.4-overall-architecture' and os.path.exists(arch_src):
                shutil.copyfile(arch_src, img_file)
            else:
                with open(img_file, 'wb') as f:
                    f.write(placeholder_bytes)
            count_images += 1

        img_rel_url = f'/images/5-Workshop/{chap}/{sub}/screenshot.png'

        # Update _index.vi.md
        vi_file = os.path.join(s, '_index.vi.md')
        if os.path.exists(vi_file):
            with open(vi_file, 'r', encoding='utf-8') as f:
                content = f.read()

            m = vi_pattern.search(content)
            if m:
                desc = m.group(2).strip()
                # Check if image tag is already there pointing to screenshot.png
                if f'({img_rel_url})' not in content:
                    new_tag = f'\n\n![{desc}]({img_rel_url})\n'
                    # Replace the screenshot block
                    updated_content = content[:m.start()] + m.group(1).rstrip() + new_tag
                    with open(vi_file, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    count_vi_updated += 1

        # Update _index.md
        en_file = os.path.join(s, '_index.md')
        if os.path.exists(en_file):
            with open(en_file, 'r', encoding='utf-8') as f:
                content = f.read()

            m = en_pattern.search(content)
            if m:
                desc = m.group(2).strip()
                if f'({img_rel_url})' not in content:
                    new_tag = f'\n\n![{desc}]({img_rel_url})\n'
                    updated_content = content[:m.start()] + m.group(1).rstrip() + new_tag
                    with open(en_file, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    count_en_updated += 1

    print(f'Done!')
    print(f'Folders created/verified: {count_folders}')
    print(f'Screenshot placeholder files created: {count_images}')
    print(f'Vietnamese markdown files updated: {count_vi_updated}')
    print(f'English markdown files updated: {count_en_updated}')

if __name__ == '__main__':
    main()
