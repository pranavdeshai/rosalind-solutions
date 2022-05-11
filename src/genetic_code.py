string = """
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G """

rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"


def translate(rna, string):
    genetic_code = {}

    # Load genetic code into memory
    lines = string.splitlines()
    for line in lines:
        words = line.split()
        for i in range(0, len(words), 2):
            genetic_code[words[i]] = words[i + 1]

    # Translation
    protein = ""
    for i in range(0, len(rna), 3):
        codon = rna[i : i + 3]
        amino_acid = genetic_code[codon]
        if amino_acid == "Stop":
            break
        protein += amino_acid

    return protein


print(translate(rna, string))