f = open("rosalind_kmp.txt")

temp =''
for l in f:
	if not  l.startswith('>'):
		temp =temp+l.strip()

#temp="012345678901234567890"
#temp="CAGCATGGTATCACAGCAGAG"		

p=[-1,0]

for k in range (1,len(temp)):
	#print(k)
	flag=1
	i = k
	while i!=-1:
		#print(i)	
		if temp[p[i]]==temp[k]:
			p.append(p[i]+1)
			flag = 0
			break
		else:
			i=p[i]
	#if i==0:
	#	if temp[p[i]]==temp[k]:
	#		p.append(p[i]+1)
	if flag:
		p.append(0)
	#print(p)

#p[0]=0

print(' '.join(str(ele) for ele in p[1:]))
