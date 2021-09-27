f = open("rosalind_revp.txt")
seq = ''
for l in f:
	if not l.startswith('>'):
		seq=seq+l.strip()

#seq = "TCAATGCATGCGGGTCTATATGCAT"

def revc(l):
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
	return newl

length = list(range(4,13))
#print(length)
#print(len(seq))
#print(seq[25-6:])
for j in length:
	#print(j)
	for i in range(0,len(seq)-j+1):
		#print(seq[i:i+j])
		if seq[i:i+j] == revc((seq[i:i+j])[::-1]):
			print(str(i+1)+' '+str(j))
