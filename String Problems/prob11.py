import math
from itertools import permutations 

f =open("rosalind_lexf.txt")

#alpa =[]

for l in f:
	if ord(str(l.strip())[0]) >=65 :
		alpa=l.strip().split(' ')
	else :
		n = int(l.strip())

alpa = alpa *n
#print(alpa)
#print(n) 

list_str = permutations(alpa,n)

res =[]
for i in list(list_str) :
	#print(list(list_str))
	res.append(''.join(i))
	#print(res)
res = list(dict.fromkeys(res))

print(*sorted(res) , sep ='\n')
