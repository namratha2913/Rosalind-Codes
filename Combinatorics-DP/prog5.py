import math
from itertools import permutations 


n = 5


permute_res = []
def printPermut(n):
	seq=''
	for i in range(1,n+1):
		seq = seq+str(i)
	#print(seq)
	res = permutations(seq) 
	return res

print(math.factorial(n))
res= printPermut(n)

for i in list(res):
	#print(i)
	permute_res.append(' '.join(i))

print(*permute_res,sep='\n')

