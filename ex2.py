#Complementing DNA p.39

from __future__ import division

dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

dna1 = dna_seq.replace("A", "t")
print(dna1)
dna2 = dna1.replace("T", "a")
print(dna2)
dna3 = dna2.replace("C", "g")
print(dna3)
dna4 = dna3.replace("G", "c")
print(dna4)
print(dna4.upper())
