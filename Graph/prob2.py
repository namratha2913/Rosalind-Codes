f = open("rosalind_tree.txt")

vert = 0
edge = 0

for l in f:
	vert = int(l)
	break
	
for l in f:
	edge = edge+1

print (vert-1-edge)



