## LCSM :http://rosalind.info/problems/lcsq/
f = open("rosalind_lcsq.txt")

temp =''
string=[]
for l in f:
	if not  l.startswith('>'):
		temp =temp+l.strip()
	if l.startswith('>') and temp:
		string.append(temp)
		temp=''	
string.append(temp)
#print(string)

m = len(string[0]) +1
n = len(string[1]) +1

final = ''
Mat = [[0 for x in range(n)] for y in range(m)]
 
for i in range(1,m):
	for j in range(1,n):
		if string[0][i-1]==string[1][j-1]:
			Mat[i][j] = Mat[i-1][j-1] + 1
			#final = final + string[1][j-1]
		else :
			Mat[i][j] = max(Mat[i][j-1],Mat[i-1][j])
while (i > 0 and j > 0): 
	if (string[0][i-1] == string[1][j-1]) : 
		final=final+(string[0][i-1]) 
		i = i-1 
		j = j-1 
		  
	elif (Mat[i-1][j] > Mat[i][j-1]): 
		i=i-1 
	else :
		j=j-1
  
	
print(final[::-1])
