### Superstring == Try to reduce time limit

f = open("rosalind_long.txt")

seq =[]
s=''
for l in f :
	if l.startswith('>'):
		if s:
			seq.append(s)
			s =''	

	else :
		s = s + l.strip()

seq.append(s)

#print(seq)

def find_sim(a,b):
	pos = 0
	m = len(a)+1
	n = len(b)+1
	LCS = [[0 for x in range(n)] for y in range(m)]
	#print(len(LCS))
	for i in range(1,m):
		for j in range(1,n):
			#print(i)
			#print(j)
			if a[i-1]==b[j-1]:
				LCS[i][j] = LCS[i-1][j-1] + 1
			else:
				LCS[i][j] = 0
			#print (LCS[i])
		#print(LCS)
	pos = max(LCS[m-1][:])	
	return pos
	

final_seq = seq[0]
for i in range(1,len(seq)):
	if final_seq.find(seq[i])==-1:
		pos = find_sim(final_seq,seq[i])
		#print(pos)
		final_seq = final_seq + seq[i][pos:]
print(final_seq)
