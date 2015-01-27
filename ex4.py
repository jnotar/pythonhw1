#Splicing out introns p.40-1

#	a) 

dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon1 = dna[0:62]
exon2 = dna[90:5000]
intron = dna[63:89]

print(exon1 + exon2)

#	b)

#calculate the percentage of the dna that is coding

from __future__ import division

(len(exon1)+len(exon2)) / len(dna)

#	c)

#coding bases in uppercase, introns in lowercase

print(exon1.upper() + intron.lower() + exon2.upper())
