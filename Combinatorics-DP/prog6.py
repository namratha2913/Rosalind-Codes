#######Longest Increasing Subsequence

n = 5
permt  = [5,1,4,2,3]

LIS = [1]*n
LDS = [1]*n
lis_seq =[]
lds_seq =[]
temp_is =[]
temp_ds =[]

for i in range(0,n):
	#print(permt[i])
	#print(lis_seq)
	temp_is =[]
	temp_ds =[]
	for j in range(0,i) :
		#print(permt[j])
		if permt[j]<permt[i] :
			if LIS[i]<(1+LIS[j]):
				temp_is.append(permt[j])
			LIS[i] = max(LIS[i],1+LIS[j])
			
			
		else :
			if LDS[i]<(1+LDS[j]):
				temp_ds.append(permt[j])
			LDS[i] = max(LIS[i],1+LDS[j])
	temp_is.append(permt[i])
	temp_ds.append(permt[i])
	#print(temp_is)
	if len(temp_is)>len(lis_seq) :
		lis_seq=temp_is
	if len(temp_ds)>len(lds_seq) :
		lds_seq=temp_ds
	

#print(max(LIS))
#print(max(LDS))
print(*lis_seq,sep=' ')
print(*lds_seq, sep=' ')
		 
