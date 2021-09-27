f = open("rosalind_dna.txt")
for l in f:
	l= str(l)

A = G = C = T = 0

#print (f)
print (l)
for i in l:
	if i == 'A' :
		A=A+1
	if i == 'G' :
		G=G+1
	if i == 'C' :
		C=C+1
	if i == 'T' :
		T=T+1

print (str(A)+" "+str(C)+" "+str(G)+" "+str(T))


