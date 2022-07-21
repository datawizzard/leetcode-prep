import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	a=arr[:]
	b=arr[::-1]
	for i in range(1,n):
		if a[i-1] !=0:
			a[i] *= a[i-1]
		if b[i-1] != 0:
			b[i] *= b[i-1]
	print(a)
	print(b)
	print(max(a+b))

