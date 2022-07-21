import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,k=map(int,input().split())
	arr=["a","b","c"]
	s=""
	l=2
	while n-k>len(s):
		if l<0:
			l=2
		s=s+arr[l]
		l-=1
	print(arr[0]*k+s)
	print(len(s))

