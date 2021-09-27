f =open("rosalind_cons.txt")

strand = ''
matrix =[]
bases = ['A','C','G','T']

for l in f:
	if l.startswith(">"):
		if len(strand)>0 :
			matrix.append(strand)
		strand=''
	else:
		strand = strand+l.strip()

if len(strand)>0 :
			matrix.append(strand)
#print (matrix)
B_Cnt=[[0]*len(matrix[0]),[0]*len(matrix[0]),[0]*len(matrix[0]),[0]*len(matrix[0])]

max_base=['O']*len(matrix[0])
val =[-1]*len(matrix[0])
#print (val)
#print(int(B_Cnt[0][0]))
b_i =0
for b in bases :
	for i in range(0,len(matrix[0])):
		B_Cnt[b_i][i]=(list(zip(*matrix))[i].count(b))
		#print(B_Cnt[b_i])
		if B_Cnt[b_i][i]>int(val[i]) :
			max_base[i]=b
			val[i]=B_Cnt[b_i][i]
	b_i = b_i +1

#print(B_Cnt)
print(''.join(max_base))

for i in range(0,4):
	B_Cnt[i].insert(0,bases[i]+':')
	print(*B_Cnt[i], sep=' ')

#print(B_Cnt)


		
