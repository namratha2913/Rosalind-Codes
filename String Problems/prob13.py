from itertools import permutations as pm

f = open("rosalind_kmer.txt")

temp =''
for l in f:
	if not  l.startswith('>'):
		temp =temp+l.strip()		
#print(temp)

bases='AAAAGGGGCCCCTTTT'
kmers_list = list(pm(bases,4))
#print(kmers_list)

dct ={}
for item in kmers_list:
	kmer = str(''.join(item))
	#print(kmer)
	if kmer not in dct.keys():
		dct[kmer] = 0
#print(dct)

for i in range(0,len(temp)-3):
	kmer = str(temp[i:i+4])
	#print(kmer)
	dct[kmer] = dct[kmer] +1


ans =[]
#print(sorted(list(dct.keys())))

for key in sorted(list(dct.keys())):
	ans.append(dct[key])

print(' '.join(str(i) for i in ans))


