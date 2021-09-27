from itertools import permutations as pt

f = open("rosalind_lexv.txt")

symbol = [' ']
value = ['A']
for l in f:
	l = l.strip()
	if len(l) == 1:
		if ord(l)>48 and ord(l)<53:
			n = int(l)
			break
	k = 0
	for i in range(0,len(l)):
		if l[i] not in symbol:
			symbol.append(l[i])
			value.append(chr(ord('a')+k))
			k=k+1
to_permute = symbol * n
tp1 = value*n
#print(symbol)
#print(n)

answer = list(pt(to_permute,n))
answer1= list(pt(tp1,n))

final = []
final1 = []
for ans in answer :
	s = (''.join(ans)).strip()
	s = s.replace(' ','') 
	if s not in final and s :
		final.append(s)

for ans in answer1 :
	s = (''.join(ans)).strip()
	s = s.replace('A','') 
	if s not in final1 and s :
		final1.append(s)

#print(final,len(final))
#print(final1,len(final1))

lex_dic ={}
for i in range(0,len(final)):
	lex_dic[final1[i]] = final[i]

lex = sorted(lex_dic.keys())
print('\n'.join([lex_dic[a] for a in lex]))
