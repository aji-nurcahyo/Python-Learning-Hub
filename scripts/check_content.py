"""Regression checks for preservation, placeholder status and runnable Python contracts."""
from pathlib import Path
import re, json, html, importlib.util
root=Path(__file__).resolve().parents[1]
for n in [9,10]:
    original=(root/f'legacy/pertemuan-{n:02}/index.html').read_text(encoding='utf-8')
    titles=[html.unescape(t) for t in re.findall(r'<h[12]>(.*?)</h[12]>',original)]
    slides=json.loads((root/f'src/decks/pertemuan-{n:02}.json').read_text(encoding='utf-8'))
    assert all(t in [s['title'] for s in slides] for t in titles), 'Original slide omitted'
    for file in ['tugas.md','contoh.py']:
        assert (root/f'legacy/pertemuan-{n:02}/{file}').read_bytes()==(root/f'pertemuan-{n:02}/{file}').read_bytes()
    task=(root/f'src/decks/tugas-{n:02}.md').read_text(encoding='utf-8')
    assert task==(root/f'legacy/pertemuan-{n:02}/tugas.md').read_text(encoding='utf-8')
    for slide in slides:
        if 'example' in slide:
            assert (root/f'src/code/{slide["example"]}.py').is_file()
    spec=importlib.util.spec_from_file_location(f'example{n}',root/f'pertemuan-{n:02}/contoh.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    if n==9:
        assert module.rata_rata([]) is None
        assert module.rata_rata([-80,-100])==-90
        assert [module.kategori_rsrp(v) for v in [-90,-91,-105,-106]]==['Baik','Sedang','Sedang','Buruk']
    else:
        for data in [[],[1],[3,1,3,-2],[5,4,3,2,1]]:
            before=data.copy();assert module.selection_sort(data)==sorted(data);assert before==data
        assert module.cari_sensor([], 'missing') is None
        assert module.ringkasan([]) is None
        assert module.filter_lemah([{'rsrp':-100},{'rsrp':-101}])==[{'rsrp':-101}]
    print(f'Meeting {n}: {len(titles)} original slides, tasks, source and edge cases verified.')
assert len(list(root.glob('pertemuan-*/index.html')))==16
assert len(list((root/'src/decks').glob('pertemuan-*.json')))==2
print('16 entry routes; only two published decks.')
