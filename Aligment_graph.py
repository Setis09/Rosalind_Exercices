def LCS_matrix(v,w):
  """
  This script creates an aligment matrix between two character sequences "v" and
  "w".
  
  Input: v= "programming"  w= "gaming" 
  Output:
  array([[0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0.],
       [0., 0., 1., 1., 1., 1.],
       [0., 0., 1., 2., 2., 2.],
       [0., 0., 1., 2., 3., 3.]])

  Input: v= "printer"  w= "riper" 
  Output:
  array([[0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 1., 1.],
       [0., 1., 1., 1., 1., 2.],
       [0., 1., 2., 2., 2., 2.],
       [0., 1., 2., 2., 2., 2.],
       [0., 1., 2., 2., 2., 2.],
       [0., 1., 2., 2., 3., 3.],
       [0., 1., 2., 2., 3., 4.]])    
  """
  import numpy as np
  assert v is not None
  assert w is not None

  n= len(v)+1
  m= len(w)+1

  Align_matrix= np.zeros((n,m))

  for i in range(1,n):
    for j in range(1,m):
      if v[i -1] == w[j - 1]:
        match = 1
      else:
        match= 0

      Align_matrix[i,j] = max(Align_matrix[i - 1,j], 
                              Align_matrix[i,j -1],
                              Align_matrix[i - 1, j - 1] + match)

  return Align_matrix

################
LCS_matrix("AACCTTGG","ACACTGTGA")
