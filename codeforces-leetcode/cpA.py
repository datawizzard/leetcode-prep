import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n=int(input())
for i in range(n):
	a=int(input())
	a=str(a)
	s,r=0,0
	for j in a:
		if int(j)%2==0:
			s+=int(j)
		else:
			r+=int(j)
	# print(s,r)
	if (s%2==0 and s%4==0) or (r%2==1 and r%3==0) or (r%2==0 and r%3==0):
		print("Yes")
	else:
		print("No")
