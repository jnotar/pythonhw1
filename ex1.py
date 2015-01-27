#Calculating AT content (p.39)

from __future__ import division

dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

AT = dna_seq.count("A") + dna_seq.count("T")

ACTG = len(dna_seq)

AT_con = AT/ACTG

print("AT content of the sequence is " + str(AT_con))
