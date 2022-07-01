"""
When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n. This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""

def Fibo_rabbit(time,offspring): # Here initiates the function
  inmature=1 # We assumme that ourfirst generation is inmature
  mature=1 
  for i in range(time - 1):
    # Es necesario poner ambas instrucciones en la misma linea, para que ocurra de manera simultanea el cambio. Si se modifica primero inmature y despues mature, esto
    # va a causar que inmature cambie mas rapido y asi el aumento de mature va a crecer aun mas rapido.
    
    # It's neccesary write both instructions at the same line to make the change of both variables simultaneously. If "inmature" is modified first and the "mature",
    # the inmature is going to increase wrongly and then mature too.
    inmature,mature= mature, mature + (inmature * offspring)  
  
  # Inmarute nos da la poblacion en el mes actual (evaluado). Mature nos da la poblacion del siguiente mes.
  
  # inmature give us the population at current month. Mature give us the next. 
  return inmature

## Now here we introduce the input of time and offspring, respectively.
months= 5
pairs= 3

Fibo_rabbit(months,pairs)
