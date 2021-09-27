f = open("rosalind_gc.txt")

read = 0
res = -1.000
new_res=-1.000
final_read = ["",0.000]
read_name=''
lr=''

def cal_GC_percent(l) :
	#l=l.replace("\n",'')
	#print(len(l))
	if len(l)>0:
		return ((l.count('C')+l.count('G'))/len(l))*100
	else :
		return -1.0000

for l in f:
	
	if l.startswith(">")  :
		new_res= cal_GC_percent(lr.strip())
		#read = 0
		if new_res >= res:
			res= new_res
			final_read[0]=read_name
			final_read[1]= new_res
		#read = 1
		read_name =  l[1:].strip()
		lr=''
	elif not l.startswith(">") :
		lr =lr+ l.strip()

new_res= cal_GC_percent(lr.strip())
if new_res >= res:
	res= new_res
	final_read[0]=read_name
	final_read[1]= new_res
		

print (final_read[0])
print (final_read[1])
