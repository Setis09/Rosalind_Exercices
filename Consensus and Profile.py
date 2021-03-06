"""
A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.
DNA Strings:

A T C C A G C T
G G G C A A C T
A T G G A T C T
A A G C A A C C
T T G G A A C T
A T G C C A T T
A T G G C A C T

Profile:

A:  5 1 0 0 5 5 0 0
C:  0 0 1 4 2 0 6 1
G:  1 1 6 3 0 1 0 0
T:  1 5 0 0 0 1 1 6

Consensus	A T G C A A C T

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""
#! pip install biopython
#or
#pip install biopython
import pandas as pd # for doing Data Frames
from Bio import SeqIO # for reading FASTA files
import numpy as np # To create numpy arrays (matrices)

def Consensus_string(seqs): # This function takes a FASTA file with many sequences with equal length, constructs consensus matrix and then finds the consensus sequence.
  sequences= SeqIO.index(seqs,"fasta") # This line reads the FASTA file and creates a dictionary for the sequences.
  length= len(sequences[next(iter(sequences))]) # The length of the first sequence (all sequences have the same length)
  cons_matrix= np.zeros((4,length)) # Create a matrix with 4 rows and m columns (m = length of sequences)

  for i in range(length): # For iteraiting by each item on the sequences
    for rec in secuences.values(): # For iteraiting over each sequence (moving fordward by columns)
      if rec.seq[i] == "A": # sums 1 to A
        cons_matrix[0,i]+= 1
      elif rec.seq[i] == "C": # sums 1 to C
        cons_matrix[1,i]+= 1
      elif rec.seq[i] == "G": # sums 1 to G
        cons_matrix[2,i]+= 1
      else:
        cons_matrix[3,i]+= 1 # sums 1 to T
  
df_cons_matrix= pd.DataFrame(cons_matrix.astype(int),index=["A","C","G","T"])
  
  cons_seq=''
  for col in df_cons_matrix:
    greater= df_cons_matrix[[col]].idxmax()
    cons_seq+= str(list(greater)[0])
    
  with open("cons_out","w+") as handle: #cons_out is the name of the output file
    handle.write(cons_seq + "\n")

    A= "A: "+ str(cons_matrix.astype(int)[0]).replace("[","").replace("]","")
    handle.write(A.replace("\n","") + "\n")
    
    C= "C: "+ str(cons_matrix.astype(int)[1]).replace("[","").replace("]","")
    handle.write(C.replace('\n',"")+ "\n")

    G= "G: "+ str(cons_matrix.astype(int)[2]).replace("[","").replace("]","")
    handle.write(G.replace("\n","")+ "\n")

    T= "T: "+ str(cons_matrix.astype(int)[3]).replace("[","").replace("]","")
    handle.write(T.replace("\n","")+ "\n")

  handle.close()

  
seqs_path= "/content/File_PCRs.txt" #Here goes the path to the file with the sequences in FASTA format
Consensus_string(seqs_path)


