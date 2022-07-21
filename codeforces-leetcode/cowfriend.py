import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	f=0
	n,x=arr=map(int,input().split())
	fav=list(map(int,input().split()))
	f=max(fav)
	if f==x or x in fav:
		print(1)
	else:
		print(max(2,(x+f-1)//f))
