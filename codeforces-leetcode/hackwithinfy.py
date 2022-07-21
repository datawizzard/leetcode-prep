import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n,k=map(int,input().split())
flag=0
l=[]
for i in range(k):
	p,q=map(int,input().split())
	l.append((p,q))
l.sort()
print(l)
for i in l:
	if i[0]>n:
		print("NO")
		exit()
	n=n+i[1]
print("YES")