import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# for _ in range(int(input())):
# 	n=int(input())
# 	a=[]
# 	arr=[]
# 	x=[i for i in range(n,0,-1)]
# 	for pos,i in enumerate(x,1):
# 		if pos==i:
# 			a.append(i)
# 		else:
# 			arr.append(i)
# 	print(*arr+a)
for _ in range(int(input())):
	n=int(input())
	x=[i for i in range(1,n+1)]
	print(x[-1],*x[0:n-1])