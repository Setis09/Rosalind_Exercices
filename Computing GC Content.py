"""
In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.

This script finds the ID and GC_percentage from the sequence with maximum GC content, in a series of DNA sequences in a FASTA file (input).
"""
#pip install biopython # This package have to be installed previously
#! pip install biopython # This is the way to download and install the package in Google Colab

from Bio import SeqIO
from Bio.SeqUtils import GC
max_GC= 0
for record in SeqIO.parse("/content/rosalind_gc.txt","fasta"): # Here we add the input (/path/to/file)
  GC_cont= GC(record.seq)
  if GC_cont > max_GC:
    max_GC = GC_cont
    name= record.id

print(name)
print(max_GC)
