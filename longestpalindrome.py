import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n,m=map(int,input().split())
a=[]
r=s=''
for _ in range(n):
	x=input()
	y="".join(reversed(x))
	if y in a:
 		r+=x
	#print(r)
	a.append(x)
	#print(a)
	if x==y:
 		s=x
r=r+s+"".join(reversed(r))
print(len(r),r)
