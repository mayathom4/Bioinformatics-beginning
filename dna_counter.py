# My first Bioinformatics Script: DNA Base Counter
# This script counts the occurrences of each nucleotide in a DNA string.

def count_nucleotides(dna):
    # Convert string to uppercase just in case
    dna = dna.upper()
    
    a = dna.count('A')
    c = dna.count('C')
    g = dna.count('G')
    t = dna.count('T')
    # Calculate the total length and the GC percentage
    total_length = a + c + g + t
    gc_percent = ((g + c) / total_length) * 100
    
    return a, c, g, t, gc_percent


    

# Sample DNA sequence to test
test_dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGT"

# Run the function
a, c, g, t, gc = count_nucleotides(test_dna)

# Print results
print(f"DNA Analysis Results:")
print(f"A: {a}, C: {c}, G: {g}, T: {t}")
print(f"GC Content: {gc:.2f}%")
