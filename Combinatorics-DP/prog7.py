import math as m

f = open("rosalind_pmch.txt")


seq =''
for l in f:
	if not l.startswith('>'):
		seq = seq + l.strip()

#seq = 'AGCUAGUCAU'

a_count = seq.count('A')
g_count = seq.count('C')
print(a_count,g_count)

print(m.factorial(a_count)*m.factorial(g_count)) 
