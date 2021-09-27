n=89
m=16

gen =[0]*n

for i in range(0,m):
	#print (i)
	if i==0 or i==1:
		gen[i] = 1

	else :
		gen[i] = gen[i-2]+gen[i-1]
	#print (gen[i])

for i in range(m,n):
	if i==m :
		gen[i]= gen[i-1]+gen[i-2]-1
	else :
		gen[i]= gen[i-1]+gen[i-2]-gen[i-1-m]
	#print (gen[i])


print (gen[n-1])		

