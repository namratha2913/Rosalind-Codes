#from /home/user/Documents/Rosalind/Combinatorics-DP/prog4 import dic_prt

PrtDict = { "TTT": 'F' ,"CTT": 'L' ,"ATT": 'I', "GTT": 'V', "TTC": 'F', "CTC": 'L', "ATC": 'I' , "GTC": 'V', "TTA": 'L' ,"CTA": 'L' , "ATA": 'I' , "GTA": 'V', "TTG": 'L' , "CTG": 'L' , "ATG": 'M' , "GTG":'V' , "TCT": 'S' , "CCT": 'P' , "ACT": 'T' , "GCT": 'A', "TCC": 'S' , "CCC": 'P' , "ACC": 'T' ,"GCC": 'A',"TCA": 'S', "CCA": 'P' , "ACA": 'T', "GCA": 'A', "TCG": 'S', "CCG": 'P' , "ACG": 'T', "GCG":'A', "TAT":'Y' ,"CAT":'H' , "AAT":'N' , "GAT":'D', "TAC":'Y' , "CAC":'H' , "AAC":'N' , "GAC":'D' ,"TAA":'Stop' , "CAA":'Q' , "AAA":'K' , "GAA":'E' ,"TAG":'Stop' , "CAG":'Q' , "AAG":'K' , "GAG":'E' , "TGT":'C' , "CGT":'R' , "AGT":'S' ,  "GGT": 'G', "TGC":'C' , "CGC":'R' ,  "AGC":'S' , "GGC":'G',"TGA":'Stop' , "CGA":'R' , "AGA":'R' , "GGA":'G',"TGG":'W' , "CGG": 'R' , "AGG":'R' , "GGG":'G' } 


def revc(l):
	l=l[::-1]
	newl = []
	for i in range(0,len(l)):
		#print(l[i])
		if l[i]=='A' :
			newl.append("T")
		elif l[i]=='T' :
			newl.append('A')
		elif l[i]=='G' :
			newl.append('C')
		elif l[i]=='C' :
			newl.append('G')
	newl=''.join(newl)
	return newl


def transln(seq) :
	#seq = revc(seq)
	p = ''
	i=0
	while i<len(seq)-3:
		#print(seq[i:i+3])
		if PrtDict[seq[i:i+3]]=='Stop' :
			break
		else :
			p=p+PrtDict[seq[i:i+3]]
			i=i+3
	return p

f = open("rosalind_splc.txt")


seq =[]
line =''
flg = 0
for l in f:
	
	if not l.startswith('>'):
		line=line+l.strip()
		flg=1
	elif flg:
		seq.append(line)
		line =''
		flg=0

seq.append(line)
#print(seq)
code = seq[0]
#print(code)
seq = seq[1:]

for c in seq:
	flg =1
	while flg :
		if c in code:
			#print(c)	
			code = code[:code.find(c)]+code[code.find(c)+len(c):]
			#print(len(code))
		else :
			flg = 0
		

#print(len(code))
#print(code)
#code =revc(code)



for i in range(0,len(code)-3):
	if PrtDict[code[i:i+3]] == 'M' :
		prt = transln(code[i:])
		break

print(prt)
