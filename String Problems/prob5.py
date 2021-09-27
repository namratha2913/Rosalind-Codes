f = open("rosalind_subs.txt")
for line in f:
	l= line.strip()
	break

for line in f:
	motif = line.strip()

#print(motif.strip())

ind_size = len(motif)

res=[]
for i in range(0,(len(l)-ind_size)):
	if l[i:i+ind_size] == motif:
		res.append(i+1)

print(*res, sep=' ')


