from itertools import permutations 
import math as m

n = 98
k = 9

#l = list(range(1,22))
#perm = list(permutations(l,k))

print((m.factorial(n)/m.factorial(n-k))%1000000)
