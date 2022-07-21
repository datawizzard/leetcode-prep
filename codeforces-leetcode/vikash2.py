import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	t= [[j for j in input().split()] for i in range(n)]
	newm=[[] for i in range(2*n-1)] 
	for i in range(n): 
		for j in range(n): 
			add=i+j 
			if(add%2==0): 
				newm[add].insert(0,t[i][j]) 
				#print(newm)
			else: 
				newm[add].append(t[i][j]) 
	#print(newm)
	for i in newm: 
		for j in i: 
			print(j,end=" ") 
