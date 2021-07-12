import random
nucleotides = ['A', 'C', 'G', 'T']


# check and make sure string is a DNA STRING
def validate_sequence(dna_seq):
    tempseq = dna_seq.upper()
    for nuc in tempseq:
        if nuc not in nucleotides:
            return False
    return True


def random_dna_string(length=20):
    dna = ''.join([random.choice(nucleotides) for i in range(length)])
    return dna


def count_nucleotides_frequency(sequence):
    check_valid_sequence = validate_sequence(sequence)
    sequence_frequency = {}
    if check_valid_sequence:
        for nuc in sequence:
            if nuc in sequence_frequency:
                sequence_frequency[nuc] += 1
            else:
                sequence_frequency[nuc] = 1
    return sequence_frequency
