n=34
k=3

gen =[0]*n

for i in range(0,n):
	#print (i)
	if i==0 or i==1:
		gen[i] = 1

	else :
		gen[i] = k*gen[i-2]+gen[i-1]
	#print (gen[i])

print (gen[n-1])		

