import re

with open('/Users/pranavdeshai/Downloads/rosalind_subs.txt') as f:
    text = f.read().splitlines()
    dna = text[0]
    motif = text[1]

m = re.finditer(f'(?={motif})', dna)
for match in m:
    print(match.start() + 1, end=' ')
