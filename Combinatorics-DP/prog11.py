import math as m

f = open("rosalind_mmch.txt")


seq =''
for l in f:
	if not l.startswith('>'):
		seq = seq + l.strip()

def nPr(n, r): 
  
    return int(m.factorial(n) /m.factorial(n - r)) 

a = seq.count('A')
u = seq.count('U')
c = seq.count('C')
g = seq.count('G')
print(a,u,g,c)

print(nPr(max(a,u),min(a,u))*nPr(max(g,c),min(g,c))) 
