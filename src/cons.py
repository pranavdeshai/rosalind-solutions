with open("/Users/pranavdeshai/Downloads/rosalind_cons.txt") as f:
    dnas = []
    lines = f.readlines()
    for line in lines:
        if line.startswith(">"):
            dnas.append("")
        else:
            dnas[-1] += line.strip()
    l = len(dnas[0])
    profile = [
        [[dna[i] for dna in dnas].count(base) for i in range(l)] for base in "ACGT"
    ]
    to_string = {i: base for (i, base) in enumerate("ACGT")}
    consensus = [None for i in range(len(profile[0]))]
    for i in range(l):
        max_rep = -1
        for n, base in enumerate(profile):
            if base[i] > max_rep:
                max_rep = base[i]
                consensus[i] = to_string[n]
    print("".join(base for base in consensus))
