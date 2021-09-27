import math as m
from itertools import permutations 

def check(p_res):
	#print(p_res)
	flag =0
	for i in p_res :
		#print(i)
		if (p_res.count(i)+p_res.count(str(-1*int(i))))>1 :
			flag =1
			break
	if flag:
		return 0
	else:
		return 1	

def print_permute(new_q):
	res = list(permutations(new_q,n))
	#print(res)
	final_res=[]
	for j in list(res):
		p_res = []
		for k in j: 
			#print(k)
			p_res.append(str(k))
		if check(p_res):
			final_res.append(' '.join(p_res))
	print(len(final_res))

	print(*final_res,sep='\n')

n= 4
tot = 2*n
den = tot-n

#print(tot*(m.factorial(tot-2)/m.factorial(tot-n-1)))

q_list = list(range(-(n),0))+list(range(1,n+1))
#print(q_list)
print_permute(q_list)

