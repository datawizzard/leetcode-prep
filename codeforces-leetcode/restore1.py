import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def Siev(n): 
	prime = [True for i in range(n+1)] 
	p = 2
	while (p * p <= n):  
		if (prime[p] == True): 
			for i in range(p * p, n+1, p): 
				prime[i] = False
		p += 1
	arr1=[]
	for p in range(2, n+1): 
		if prime[p]: 
			arr1.append(p)
	return arr1
x=Siev(4000000)
for _ in range(int(input())):
	c=int(input())
	arr=list(map(int,input().split()))
	m=x[:c]
	a=[]
	for i in arr:
		a.append(m[i-1])
	print(*a)
