f = open("rosalind_revc.txt")
for l in f:
	l= str(l)
#l="AAAACCCGGT"
newl = []
for i in range(0,len(l)):
	#print(l[i])
	if l[i]=='A' :
		newl.append("T")
	elif l[i]=='T' :
		newl.append('A')
	elif l[i]=='G' :
		newl.append('C')
	elif l[i]=='C' :
		newl.append('G')

newl=''.join(newl)
print (newl[::-1])


