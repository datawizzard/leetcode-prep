import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	freq={}
	flag=0
	for i in arr:
		freq[i]=0
	for i in range(0,n):
		freq[arr[i]]=freq[arr[i]]+1
		x=max(freq.values())
		if x>=3:
			flag=1
		if i!=0:
			if freq[arr[i]]==2 and arr[i-1]!=arr[i]:
				flag=1
	if flag==1:
		print("YES")
	else:
		print("NO")