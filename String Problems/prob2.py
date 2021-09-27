f = open("rosalind_rna.txt")
for l in f:
	l= str(l)

l=l.replace("T","U")

print (l)


