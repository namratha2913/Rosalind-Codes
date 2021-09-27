f = open("rosalind_orf.txt")
seq = ''
for l in f:
	if not l.startswith('>'):
		seq=seq+l.strip()

#seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
#print(seq)

PrtDict = { "TTT": 'F' ,"CTT": 'L' ,"ATT": 'I', "GTT": 'V', "TTC": 'F', "CTC": 'L', "ATC": 'I' , "GTC": 'V', "TTA": 'L' ,"CTA": 'L' , "ATA": 'I' , "GTA": 'V', "TTG": 'L' , "CTG": 'L' , "ATG": 'M' , "GTG":'V' , "TCT": 'S' , "CCT": 'P' , "ACT": 'T' , "GCT": 'A', "TCC": 'S' , "CCC": 'P' , "ACC": 'T' ,"GCC": 'A',"TCA": 'S', "CCA": 'P' , "ACA": 'T', "GCA": 'A', "TCG": 'S', "CCG": 'P' , "ACG": 'T', "GCG":'A', "TAT":'Y' ,"CAT":'H' , "AAT":'N' , "GAT":'D', "TAC":'Y' , "CAC":'H' , "AAC":'N' , "GAC":'D' ,"TAA":'Stop' , "CAA":'Q' , "AAA":'K' , "GAA":'E' ,"TAG":'Stop' , "CAG":'Q' , "AAG":'K' , "GAG":'E' , "TGT":'C' , "CGT":'R' , "AGT":'S' ,  "GGT": 'G', "TGC":'C' , "CGC":'R' ,  "AGC":'S' , "GGC":'G',"TGA":'Stop' , "CGA":'R' , "AGA":'R' , "GGA":'G',"TGG":'W' , "CGG": 'R' , "AGG":'R' , "GGG":'G' } 

def revc(l):
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


pr_seq_list = []
seq1 = seq[::-1]

seq1 = revc(seq1)


def ORF(seq) :
	for i in range(0,len(seq)-3) :
		flag = 0
		stop_fl = 0	
		pr_seq =''
		j = i
		if PrtDict[seq[i:i+3]] == 'M' :
			#print ( PrtDict[seq[i:i+3]])
			flag = 1
		#if PrtDict(seq[i:i+3]) == 'Stop' :
		#flag = 0
		if flag :
			while j <len(seq)-3 :
				if PrtDict[seq[j:j+3]] == 'Stop' :
					stop_fl =1
					break
				else:
					pr_seq = pr_seq + PrtDict[seq[j:j+3]]
					j=j+3
			if not pr_seq in pr_seq_list and stop_fl:
				pr_seq_list.append(pr_seq)

ORF(seq1)
ORF(seq)

print(*pr_seq_list, sep='\n')
		
	
	


