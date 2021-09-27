
f = open("rosalind_sseq.txt")


template =''
temp =''
for l in f:
	if l.startswith('>') :
		template = template+temp
		temp =''
	if not  l.startswith('>'):
		temp =temp+l.strip()		

sseq = temp

print(len(sseq))
#print(template)
res=[]
i=0
for l in sseq:
	while i < len(template):
		if l == template[i] :
			res.append(i+1)
			i=i+1
			break
		i =i+1

print(len(res))
print(*res,sep=' ') 

