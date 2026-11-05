#!/usr/bin/env python3
"""Tự động tạo media.js từ thư mục ảnh và videos.txt (chạy bởi GitHub Actions)."""
import os, re, shutil, json, urllib.parse

IMG = ('.jpg', '.jpeg', '.png', '.webp', '.gif')

def nat(s):
    return [int(x) if x.isdigit() else x.lower() for x in re.split(r'(\d+)', s)]

def q(p):
    return '/'.join(urllib.parse.quote(x) for x in p.split('/'))

def imgs(d):
    return sorted([f for f in os.listdir(d) if f.lower().endswith(IMG)], key=nat)

# --- Chạy một lần: chuyển ảnh cũ ở thư mục gốc vào albums/ và hero/ ---
legacy = re.compile(r'^PN88967547 \((\d+)\)\.jpg$')
HERO = [30, 38, 80, 87]
for f in sorted(os.listdir('.')):
    m = legacy.match(f)
    if not m:
        continue
    n = int(m.group(1))
    if 21 <= n <= 55:
        dest = 'albums/1. Tông hồng · Áo dài trắng'
    elif 71 <= n <= 99:
        dest = 'albums/2. Tông đỏ · Lễ cưới'
    else:
        continue
    os.makedirs(dest, exist_ok=True)
    if n in HERO:
        os.makedirs('hero', exist_ok=True)
        shutil.copy(f, 'hero/%d.jpg' % (HERO.index(n) + 1))
    shutil.move(f, os.path.join(dest, f))

# --- Albums: mỗi thư mục con của albums/ là một album ---
albums = []
if os.path.isdir('albums'):
    for name in sorted(os.listdir('albums'), key=nat):
        d = os.path.join('albums', name)
        if not os.path.isdir(d):
            continue
        fs = imgs(d)
        if not fs:
            continue
        title = re.sub(r'^\s*\d+\s*[.\-_)]+\s*', '', name) or name
        items = [{'link': q('albums/%s/%s' % (name, f)), 'ten': ''} for f in fs]
        albums.append({'ten': title, 'cover': items[0], 'anh': items})

# --- Ảnh đầu trang: thư mục hero/ ---
slides = []
if os.path.isdir('hero'):
    slides = [{'link': q('hero/' + f), 'ten': ''} for f in imgs('hero')]

# --- Video: videos.txt, mỗi dòng "link | tên" ---
video = []
if os.path.exists('videos.txt'):
    for line in open('videos.txt', encoding='utf-8'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        link, _, ten = line.partition('|')
        video.append({'link': link.strip(), 'ten': ten.strip()})

M = {'slides': slides, 'hero': [], 'albums': albums, 'anh': [], 'video': video}
with open('media.js', 'w', encoding='utf-8') as fh:
    fh.write('window.MEDIA=' + json.dumps(M, ensure_ascii=True) + ';\n')
print('albums', len(albums), 'slides', len(slides), 'video', len(video))
