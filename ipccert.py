import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n,m,k=map(int,input().split())
count=0
for _ in range(n):
	arr=list(map(int,input().split()))
	if sum(arr[:k])>=m and arr[-1]<=10:
		count+=1
print(count)