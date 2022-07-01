"""
Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""

from Bio.Seq import Seq

dna_seq="GATGGAACTTGACTACGTAAATT"

my_seq= Seq(dna_seq)
my_seq_trs=my_seq.transcribe()
print(my_seq_trs)  #This step is neccesary, because if its called only "my_seq_trs" only could be seen the first characteres and the lastest.

