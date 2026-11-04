"""One-time migration; original material is retained under legacy/."""
from pathlib import Path
import re, json, html, shutil

root = Path(__file__).resolve().parents[1]
if (root/'src/decks/pertemuan-09.json').exists():
    raise SystemExit('Migration already completed. Restore a backup to migrate again; existing content will not be overwritten.')
for folder in ['legacy', 'src/decks', 'src/code', 'src/ui', 'src/layouts', 'src/theme', 'src/deck-shell', 'slides', 'public/downloads', 'docs']:
    (root / folder).mkdir(parents=True, exist_ok=True)
for name in ['index.html','README.md','assets','pertemuan-09','pertemuan-10']:
    src, dst = root/name, root/'legacy'/name
    if not dst.exists():
        shutil.copytree(src,dst) if src.is_dir() else shutil.copy2(src,dst)
for n in [9,10]:
    folder=f'pertemuan-{n:02}'
    shutil.copytree(root/'legacy'/folder,root/'public/downloads'/folder,dirs_exist_ok=True)
    source=(root/'legacy'/folder/'index.html').read_text(encoding='utf-8')
    slides=[]
    for i, section in enumerate(re.findall(r'<section>(.*?)</section>',source,re.S)):
        title_match=re.search(r'<h[12]>(.*?)</h[12]>',section,re.S)
        title=html.unescape(title_match[1])
        body=re.sub(r'<div class="eyebrow">.*?</div>|<h[12]>.*?</h[12]>','',section,flags=re.S)
        codes=re.findall(r'<pre><code>(.*?)</code></pre>',body,re.S)
        body=re.sub(r'<pre><code>.*?</code></pre>','',body,flags=re.S)
        item={'title':title,'body':body,'kind':'cover' if i==0 else ('exercise' if 'Latihan' in title or 'Tugas' in title else 'content'), 'notes':f'Bahas {title.lower()}. Minta mahasiswa menjelaskan alasan jawabannya sebelum melanjutkan.'}
        if codes:
            code=html.unescape(codes[0]).replace('\r\n','\n')
            if 'Membuat modul' in title:
                d=root/'src/code/p09-module'; d.mkdir(exist_ok=True)
                a,b=code.split('# file: main.py')
                (d/'statistik.py').write_text(a+'\n',encoding='utf-8')
                (d/'main.py').write_text(b.strip()+'\n',encoding='utf-8')
                item['files']=[{'name':'statistik.py','code':a.strip()},{'name':'main.py','code':b.strip()}]
                item['example']='p09-module/main'
            else:
                if n==10 and title=='Pencarian linear (linear search)':
                    code+='\n\nprint(cari_sensor([{ "id": "S01", "rsrp": -82 }], "S01"))\nprint(cari_sensor([], "S99"))'
                if n==10 and title=='Cari data: contoh penggunaan':
                    code='from contoh import PENGUKURAN as pengukuran, cari_sensor\n\n'+code
                    shutil.copy2(root/'legacy/pertemuan-10/contoh.py',root/'src/code/contoh.py')
                    item['dependency']='contoh.py'
                if 'Selection sort:' in title:
                    code+='\n\nprint(selection_sort([5, 2, 9, 1]))'
                key=f'p{n:02}-{i:02}'
                (root/'src/code'/f'{key}.py').write_text(code+'\n',encoding='utf-8')
                item['example']=key
            item['kind']='code'
            if not body.strip(): item['body']='<p>Jalankan contoh Python 3, lalu bandingkan hasilnya dengan output di samping.</p>'
        slides.append(item)
    question={'title':'Cek pemahaman','body':'<p>Prediksi dahulu, kemudian buka pembahasan.</p>','kind':'question','question':'Mengapa return lebih sesuai untuk fungsi pengolahan data?' if n==9 else 'Apakah sorted(data) mengubah list data semula?', 'answer':'return mengembalikan nilai untuk dipakai, dikombinasikan, dan diuji. print hanya menampilkan teks.' if n==9 else 'Tidak. sorted menghasilkan list baru. Gunakan list.sort() jika ingin mengubah list di tempat.', 'notes':'Beri waktu satu menit untuk berpikir dan diskusi berpasangan.'}
    slides.insert(-1,question)
    (root/f'src/decks/pertemuan-{n:02}.json').write_text(json.dumps(slides,ensure_ascii=False,indent=2),encoding='utf-8')
    (root/f'src/decks/tugas-{n:02}.md').write_text((root/'legacy'/folder/'tugas.md').read_text(encoding='utf-8'),encoding='utf-8')
shutil.copy2(root/'legacy/assets/Materi_Pengkom_Pertemuan_9_10_Python.pptx',root/'public/downloads/Materi_Pengkom_Pertemuan_9_10_Python.pptx')
ref=root.parent/'ref-pengkom'
for name in ['highlight.ts','Math.tsx']:
    shutil.copy2(ref/'src/ui'/name,root/'src/ui'/name)
shutil.copy2(ref/'LICENSE',root/'LICENSE.upstream')
for i in range(17):
    page=root/'index.html' if i==0 else root/f'pertemuan-{i:02}/index.html'
    script='/src/main.tsx'
    page.write_text(f'<!doctype html><html lang="id"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#1556c0"><meta name="description" content="Materi perkuliahan algoritma dan pemrograman Python — Telekomunikasi"><title>{"Alpro Python" if i==0 else f"Pertemuan {i} · Alpro Python"}</title></head><body><div id="root"></div><script type="module" src="{script}"></script></body></html>',encoding='utf-8')
for n in [9,10]:
    shutil.copy2(root/f'pertemuan-{n:02}/index.html',root/f'pertemuan-{n:02}/tugas.html')
shutil.copy2(root/'index.html',root/'404.html')
print('Migrated original content and preserved legacy files.')
