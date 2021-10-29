# I obviously should learn more about regex

import re
import sys
from pathlib import Path

replacements = {
    r'\Glspl{': r'\Acp{',
    r'\glspl{': r'\acp{',
    r'\Gls{': r'\Ac{',
    r'\gls{': r'\ac{',
}

patterns = (
    r'\\Acp(\{\w+\})',
    r'\\acp(\{\w+\})',
    r'\\Ac(\{\w+\})',
    r'\\ac(\{\w+\})',
)

input_dir = sys.argv[1]
input_dir = Path(input_dir)
for fp in input_dir.rglob('*.tex'):
    lines = []
    for line in fp.read_text().splitlines():
        for k, v in replacements.items():
            line = line.replace(k ,v)
        for pattern in patterns:
            all_matches = re.findall(pattern, line)
            for match in all_matches:
                line = line.replace(match, match.upper())
        line = line.replace(r'~\citep', r' \cite')
        line = line.replace(r'~\cite', r' \cite')
        line = line.replace(r'\citep', r'\cite')
        lines.append(line)
    fp.write_text('\n'.join(lines))
