f = open("rosalind_lcsm1.txt")


temp =''
dna_set = []
for l in f:
	if l.startswith('>') :
		if temp != '':
			dna_set.append(temp)
			temp = ''
	if not  l.startswith('>'):
		temp =temp+l.strip()
dna_set.append(temp)	

#print(dna_set)

def gen_substring(string):
	substring_set=[]
	j=len(string)
	for i in range(0,j) :
		k=j
		while k>i:
			if string[i:k] not in substring_set:
				substring_set.append(string[i:k])
			k=k-1
	substring_set = sorted(substring_set, key=len, reverse=True)
	return(substring_set)

ss = gen_substring(dna_set[0])
#print(ss)

def LCS(dna_set):
	for s in ss:
		flag=1
		for string in dna_set[1:]:
			if (string.find(s) == -1):
				flag=0
				break
		if flag==1:
			print(s)
			break 

LCS(dna_set)
