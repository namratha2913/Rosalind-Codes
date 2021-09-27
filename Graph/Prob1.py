f = open("rosalind_grph.txt")
k = 3

file_list =[]
flag = 0
code_list = []
code = ''

for l in f:
	if l.startswith('>'):
		if flag:
			code_list.append(code)
			flag = 0
		if not flag:
			file_list.append(l.strip())
			flag = 1
			code = ''
	else :
		code = code + l.strip()	
		
code_list.append(code)
#print(code_list[0][-3:])

for i in range(0,len(file_list)) :
	for j in range(0,len(file_list)) :		
		if code_list[i][-k:] == code_list[j][0:k] and i!=j:
			#print(code_list[i][-k:])
			print(file_list[i][1:]+" "+file_list[j][1:])
		 
