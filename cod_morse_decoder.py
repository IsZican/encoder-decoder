g='Ubt"@*ŃĬQhuhEhuhQ.uĬw:Qk]8un\\:w.'
d=7
cod_morsee={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-','L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
  'Z': '--..','a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-','l': '.-..',
  'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
  'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  ':': '---...',',': '--..--','/': '-..-.', '?': '..--..', '=': '-...-','.': '.-.-.-', ' ':' ','': '','(': '-.--.',')': '-.--.-'}

cod_morse=dict([reversed(i) for i in cod_morsee.items()])
print('#decoder')
print(g)
aa=0
bb=''
cc=0
dd=''
for i in g:
	cc+=1
	aa=ord(i)
	if aa>=300:
		aa-=300
	while aa>0:
		bb+=str(aa%2)
		aa//=2
	while len(bb)<7 and cc!=len(g):
		bb+='0'
	while len(bb)<d and cc==len(g):
		bb+='0'	
	bb=bb[::-1]
	dd+=bb
	print(bb,end=' ')
	bb=''

print()
print()
print(dd)

n=0
m=0
l=''
for i in dd:
	if i=='1':
		m+=1
	else:
		n+=1
	if m>0 and n==1:
		if m==3:
			l+='-'
		else:
			l+='.'
		m=0
		n=0
	if n>1:
		l+=' '
		n=0
print(l)
aaa=''
for i in l.split(' '):
	if i=='':
		aaa+=' '
	else:
		aaa+=cod_morse[i]
print(aaa)