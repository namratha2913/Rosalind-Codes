f= open("rosalind_tran.txt")

temp =''
seq =[]

for l in  f:
	if l.startswith('>'):
		if temp:
			seq.append(temp)
		temp =''
	else :
		temp = temp + l.strip()

seq.append(temp)

print(seq)

transit =0.0
transin =0.0
for c1,c2 in zip(seq[0],seq[1]):
	if(c1,c2)==('A','G') or (c1,c2)==('G','A'):
		transit = transit+1
	elif (c1,c2) == ('C','T') or (c1,c2)==('T','C'):
		transit = transit+1
	elif (c1,c2)==('A','T') or (c1,c2)==('T','A') or (c1,c2)==('T','G') or (c1,c2)==('G','T'):
		transin = transin+1
	elif (c1,c2)==('C','G') or (c1,c2)==('G' ,'C') or (c1,c2)==('C','A')or (c1,c2)==('A','C'):
		transin = transin+1

print(transit/transin)
