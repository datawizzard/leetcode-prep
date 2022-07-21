import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n=int(input())
index=0
arr=[0]*(n*(n-1)//2)
sum1=list(map(int,input().split()))
for i in range(0,n-1):
	for j in range(i+1,n):
		arr[index]=sum1[i]+sum1[j]
		index+=1
for i in range(1,len(arr)):
	arr[i]=arr[i]^arr[i-1]
print(arr[-1])