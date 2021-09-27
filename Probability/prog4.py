import math as m

f = open("rosalind_prob.txt")

seq =''
prob_list = []
for l in f:
	if ord(str(l.strip())[0])>64 :
		seq = l.strip()
	else :
		prob_list = l.strip().split()

res = []

a_cnt = seq.count('A') + seq.count('T') 
c_cnt = seq.count('C') + seq.count('G') 
#print(a_cnt)
#print(c_cnt)

for i in prob_list :
	c_prob = float(i)/2.0
	a_prob = 0.5 - c_prob
	#print(c_prob)
	#print(a_prob)
	res.append(m.log10((c_prob**c_cnt)*(a_prob**a_cnt)))
	
print(*res, sep=' ' )
