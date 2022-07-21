import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,x=map(int,input().split())
	arr=list(map(int,input().split()))
	a=arr[:]
	s,i=sum(arr),0
	while arr[i]%x==0:
		s += a[i]
		arr[i]=arr[i]//x
		i = (i +1) % n
	print(s)

