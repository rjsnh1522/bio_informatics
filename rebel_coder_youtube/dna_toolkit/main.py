from dna_toolkit.DNAToolkit import *

rndString = "agttattgattgagt"

# print(validate_sequence(rndString))

# print("dna string", random_dna_string(12))
dna_seq = random_dna_string(998)
print(dna_seq)
freq_count = count_nucleotides_frequency(dna_seq)
print(freq_count)
