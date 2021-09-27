k=18.0
m=18.0
n=27.0

Total = k+m+n

P1 = (k/Total)*(k-1+m+n)/(Total-1)
P2 = (m/Total)*(k+(m-1)*0.75+n*0.5)/(Total-1)
P3 = (n/Total)*(k+m*0.5)/(Total-1)

P = P1+P2+P3

print (P) 
