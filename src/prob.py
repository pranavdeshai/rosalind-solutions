# PROB: Introduction to random strings
from math import log10


with open('/PATH/TO/DATASET') as f:
    dna_string = f.readline().strip()
    gc_contents = [float(i) for i in f.readline().strip().split(" ")]

prob = [round(sum(log10((1-gc)/2) if i in 'AT' else log10(gc/2)
              for i in dna_string), 3) for gc in gc_contents]

for i in prob:
    print(i, end=' ')
