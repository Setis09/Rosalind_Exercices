def Longest_common_Subquence(v,w):
  """
  This script finds one of the longest common subsequences between two character sequences "v" and "w". Also find the length of this sequence.
  
  How it function?
  First creates an aligment graph (or matrix) between both sequences (by the use of the function LCS_matrix). 
  Then, creates a string named "seq" to store the longest common subsequence. This value is going to be updated on the following steps;
  after that, start checking at backtracking from the last row and column to the origin, when there is a match between "v" and "w".
  
  Then if there i a match, match = 1 either match = 0 and proceeds to compare if the current i,j = to previous nodes (diagonal node, up node or left node).
  If the node score == to the diagonal, then, the backtrack goes diagonal,
  if the node score == to the up node, then backtrack goes to the up node.
  And last if neither of the conditions is acomplished, then the backtrack goes to the left.
  
  This procees occurs until the position arrives to 0 in "i" or "j".
  
  Examples:
  
  Input: v= "Programming", w= "gaming"
  Output: 6, "gaming"
  
  Input: v="printer", w= "riper"
  Output: 4, "rier" 
  """
  
  Align_matrix= LCS_matrix(v,w) # Here we have to use a function created previously. This is available on this repository as "Aligment_graph.py"
                                # https://github.com/Setis09/Rosalind_Exercices/blob/main/Aligment_graph.py
  
  seq= ""
  
  i,j= len(v), len(w) 
  n,m = i,j
  while i > 0 and j > 0:
    if v[i - 1] == w[j -1]:
      match = 1
    else:
      match = 0
    
    if Align_matrix[i,j] == Align_matrix[i-1,j-1] + match:
      if match == 1:
        seq+= v[i - 1]
      i-= 1
      j-= 1

    elif Align_matrix[i,j] == Align_matrix[i-1,j]:
      i-= 1

    else:
      j-= 1
  
  return int(Align_matrix[n,m]),seq[::-1] 

  
########################
Longest_common_Subquence("AACCTTGG","ACACTGTGA")
