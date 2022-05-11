# mendel.py
# Rosalind bioinformatics problem ID: IPRB

import random
import sys

required_genotype = sys.argv[1]
male_genotype = sys.argv[2]
female_genotype = sys.argv[3]

male_gametes = list(set(male_genotype))
female_gametes = list(set(female_genotype))

zygotes = []
for male_gamete in male_gametes:
    for female_gamete in female_gametes:
        zygotes.append(male_gamete + female_gamete)

counter = 0
for zygote in zygotes:
    if sorted(zygote) == sorted(required_genotype):
        counter += 1
probability = counter / len(zygotes)

n = 1000
results = {"pp": 0, "pq": 0, "qp": 0, "qq": 0}
for i in range(n):
    results[random.choice(zygotes)] += 1

print(f"Possible genotypes for progeny: {sorted(zygotes)}")
print(f'Probability of genotype "{required_genotype}" = {probability}')
print(f"Results of simulation: {results}")
