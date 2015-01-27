#Restriction fragment lengths p.40

dna_seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

cut = dna_seq.find("ATTC")
EcoR1_1 = len(dna_seq[0:cut])
print(EcoR1_1)

EcoR1_2 = len(dna_seq[cut:5000])
print(EcoR1_2)

#Check the answer
length = len(dna_seq)
print(length)

add = EcoR1_1 + EcoR1_2
print(add)
