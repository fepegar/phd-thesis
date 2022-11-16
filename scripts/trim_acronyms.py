from pathlib import Path
import re


all_tex_paths = list(Path().rglob('*.tex'))
all_text = '\n'.join(fp.read_text() for fp in all_tex_paths)
acronyms_lines = [
    line for line in Path('tex/acronyms.tex').read_text().splitlines()
    if r'\acro{' in line
]
plurals = ['RC', 'SUDEP']
acronyms = [line[8:line.find('}')] for line in acronyms_lines] + plurals
ac_freq = {
    ac: len(re.findall(r'\\[aA]c[\w+]?{' + ac + '}', all_text))
    for ac in acronyms
}

print(sorted(ac_freq.items(), key=lambda x: x[1]))
