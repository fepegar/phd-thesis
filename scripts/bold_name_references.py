import time

from utils import get_repo_dir


references_dir = get_repo_dir() / 'references'
src_path = references_dir / 'phd.bib'
dst_path = references_dir / 'phd_bold.bib'

patterns = (
    r"P{\'e}rez-Garc{\'i}a",
    # 'Fernando',
    'Fernando Perez-Garcia',
    'Fernando Pérez-García',
    'Pérez-García, Fernando',
    'Pérez‐García, Fernando',
    # 'Pérez-García',
)

is_changing = True
src_size = src_path.stat().st_size
while is_changing:
    print('File size:', src_size)
    time.sleep(0.5)
    new_size = src_path.stat().st_size
    is_changing = new_size != src_size
    src_size = new_size

lines = []
for line in src_path.read_text().splitlines():
    if 'garc' in line.lower():
        # print(line)
        pass
    for p in patterns:
        if 'Tharindu' not in line:
            line = line.replace(p, '\\textbf{%s}' % p)
    lines.append(line)
text = '\n'.join(lines)
dst_path.write_text(text)
