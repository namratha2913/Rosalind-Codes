f = open("rosalind_mrna.txt")

for l in f:
	seq=l.strip()

print(seq)
#seq="MA"

AA_dict = {'A':4,'C':2,'D':2,'E':2,'F':2,'G':4,'H':2,'I':3,'K':2,'L':6,'M':1,'N':2,'P':4,'Q':2,'R':6,'S':6,'T':4,'V':4,'W':1,'Y':2}
#Stop = 3

total = 3
for c in list(seq) :
	#print (c)
	total = total * AA_dict[c]

print(total)
print(total % 1000000)
