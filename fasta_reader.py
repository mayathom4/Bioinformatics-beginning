# Project 3: FASTA File Reader
# This script opens a real genomic file and extracts the sequence data.

def read_fasta(filename):
    sequence = ""
    
    # Open the file for reading ('r')
    with open(filename, 'r') as file:
        for line in file:
            # Skip the header line that starts with '>'
            if not line.startswith(">"):
                # .strip() removes hidden 'new line' characters at the end
                sequence += line.strip()
    
    return sequence

# Run the reader
fasta_file = "/Users/mayathomas/Desktop/sample.fasta"
extracted_dna = read_fasta(fasta_file)

# Results
print(f"File '{fasta_file}' read successfully.")
print(f"Cleaned Sequence: {extracted_dna}")
print(f"Total length: {len(extracted_dna)} bases")
