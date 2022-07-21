import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	s=input()
	p=input()
	l=len(p)
	z=list(p)
	sorts=sorted(s)
	sortp=sorted(p)
	n=[]
	ans=[]
	ind=0
	for i in sorts:
		if ind<l:
			if i==sortp[ind]:
				ind+=1
				continue
			else:
				n.append(i)
		else:
			n.append(i)
	r=0
	for i in n:
		if p[0]<i:
			ans=n[:r]+z+n[r:]
			break
		else:
			ans=n+z
		r+=1
	print(''.join(str(x) for x in ans))



