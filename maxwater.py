import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	maxi=0
	i=0
	j=n-1
	while(i<j):
		if arr[i]<=arr[j]:
			maxi=max(maxi,arr[i]*(j-i))
			i+=1
		elif arr[i]>arr[j]:
			maxi=max(maxi,arr[j]*(j-i))
			j-=1
		# else:
		# 	maxi = max(maxi, (j-i) * arr[i])
		# 	i += 1
		# 	j -= 1
	print(maxi)
