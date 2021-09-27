## Finding a Protein Motif  ##

from bs4 import BeautifulSoup
import urllib.request as ur

f =open("rosalind_mprt.txt")

#seq_list = []
#motif = N{P}[ST]{P}

def find_motif(seq):
	res=[]
	for i in range(0,len(seq)-4):
		if seq[i]=='N' and seq[i+1]!='P' and (seq[i+2] == 'S' or seq[i+2] == 'T') and seq[i+3]!='P' :
			res.append(i+1)
	return res
			

for l in f:
	res= []
	prot_link = 'https://www.uniprot.org/uniprot/'+l.strip()+'.fasta'
	page = ur.urlopen(prot_link)
	soup = BeautifulSoup(page)
	fasta = soup.get_text()
	prot_seq = ''.join(fasta.split('\n')[1:])
	#print(prot_seq)
	res = find_motif(prot_seq)
	if res:
		print (l.strip())
		print (*res , sep=' ')
	

