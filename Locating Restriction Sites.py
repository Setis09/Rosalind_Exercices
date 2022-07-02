"""
Problem

A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC.
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
"""
#!pip install biopython 
#or
#pip install biopython

from Bio.Seq import Seq

def Palindromesearch(seq):
  my_seq= Seq(seq)
  for w in range(4,13):
    for i in range(len(my_seq)+1-w):
      seq_w= my_seq[i:i+w]
      rev_seq_w= seq_w.reverse_complement()
      if seq_w == rev_seq_w:
        print(i+1,w)
  
sequence= "TCAATGCATGCGGGTCTATATGCAT" # Here goes the input sequence

Palindromesearch(sequence)
