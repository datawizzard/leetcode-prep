import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	arr1=[]
	def compute_gcd(x, y):
		while(y):
			x, y = y, x % y
		return x
	def compute_lcm(x, y):
		lcm = (x*y)//compute_gcd(x,y)
		return lcm
	for i in range(0,n,2):
		x=compute_lcm(arr[i],arr[i+1])
		x1=x//arr[i]
		x2=x//arr[i+1]
		arr1.append(int(x1))
		arr1.append(int(-x2))
	print(*arr1)
