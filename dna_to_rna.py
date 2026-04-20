# Project 2: DNA to RNA Transcription
# This script converts a DNA sequence into an RNA sequence 
# by replacing all Thymine (T) with Uracil (U).

def transcribe_dna(dna):
    # Standardize to uppercase
    dna = dna.upper()
    
    # The 'replace' method swaps every 'T' for a 'U'
    rna = dna.replace('T', 'U')
    
    return rna

# Sample Data
dna_sample = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGT"

# Run the function
rna_result = transcribe_dna(dna_sample)

# Print the results
print(f"Original DNA: {dna_sample}")
print(f"RNA Sequence: {rna_result}")
