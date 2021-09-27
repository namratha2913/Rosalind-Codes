import math

x = 56
n = int(math.log(x)/math.log(2))
#print (n)
ans = int(x*(pow(0.5,n)-1)*(-1)+0.5)
print(ans-1)

## number of internal nodes in unrooted tree = n-2, if leaf nodes =n
