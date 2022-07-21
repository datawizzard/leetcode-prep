import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
count=0
for i in range(n-1):
	for j in range(i+1,n):
		if (arr[i]&arr[j])>k:
			count+=1
print(count)
