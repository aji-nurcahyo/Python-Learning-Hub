"""Execute every published example in CPython; verify committed output in --check mode."""
from pathlib import Path
import subprocess, sys, os, json, shutil
root=Path(__file__).resolve().parents[1]
check='--check' in sys.argv
env={**os.environ,'PYTHONHASHSEED':'0','PYTHONIOENCODING':'utf-8'}
outputs={}
for file in sorted((root/'src/code').rglob('*.py')):
    if file.name in ['statistik.py','contoh.py']: continue
    run=subprocess.run([sys.executable,str(file)],cwd=file.parent,env=env,capture_output=True,text=True,encoding='utf-8',timeout=10)
    if run.returncode: raise SystemExit(f'{file}:\n{run.stderr}')
    key=file.relative_to(root/'src/code').with_suffix('').as_posix()
    outputs[key]=run.stdout
for n, ch in [(9, 10), (10, 8)]:
    file = root / f'content/foundations/chapter-{ch:02d}/assignments/contoh.py'
    run = subprocess.run([sys.executable, str(file)], cwd=file.parent, env=env, capture_output=True, text=True, encoding='utf-8', timeout=10)
    if run.returncode: raise SystemExit(run.stderr)
    outputs[f'original-{n}'] = run.stdout
target=root/'src/code/outputs.json'
if check:
    if not target.exists() or json.loads(target.read_text(encoding='utf-8'))!=outputs:
        raise SystemExit('Output changed. Run npm run gen:outputs and review.')
else:
    target.write_text(json.dumps(outputs,ensure_ascii=False,indent=2),encoding='utf-8')
    shutil.copytree(root/'src/code',root/'public/downloads/examples',dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','outputs.json','spec-outputs.json'))
print(f'{len(outputs)} Python examples executed successfully; output '+('verified.' if check else 'generated.'))
