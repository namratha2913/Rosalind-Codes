f = open("rosalind_iev.txt")

n=[]

for val in f.read().split():
	n.append(int(val))
f.close()

Exp_val = 2*(n[0]+n[1]+n[2]+n[3]*0.75+n[4]*0.5)

print(Exp_val)
	

