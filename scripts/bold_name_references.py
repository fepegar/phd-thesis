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
    # 'Pérez-García',
)

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
