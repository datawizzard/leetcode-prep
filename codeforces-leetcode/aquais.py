import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	s = input()
	l = 'abacaba'
	if s.find(l) != -1 and s.find(l) == s.rfind(l):
		print('YES', s.replace('?','x'),sep='\n')
		continue
	for ind in range(0,n):
		w = s[ind:ind+7]
		print(w)
		w = ''.join([a for a, b in zip(w,l) if a == b or a is '?'])
		print(w)
		if len(w)==7: 
			b= s[:ind]+l+s[ind + 7:]
			print(b)
			if b.find(l) !=-1 and b.find(l)==b.rfind(l):
				print('YES', b.replace('?', 'x'),sep='\n')
				break
	else:
		print('NO')
