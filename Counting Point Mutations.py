"""
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""
def Counting_mutations(s,t):
  mutations= 0
  for i in range(len(s)):
    if s[i] != t[i]:
      mutations+=1
  return mutations

Counting_mutations("GAGCCTACTAACGGGAT",
                   "CATCGTAATGACGGCCT")
