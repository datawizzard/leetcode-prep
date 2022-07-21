import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
z=input
for _ in range(int(z())):
	n=int(input())
	arr=list(map(int,input().split()))
	# arr.sort()
	# i=0
	# while i<n-1:
	# 	for j in range(i+1,n):
	# 		if arr[j]==arr[i]:
	# 			arr[j]+=1
	# 			i+=1
	# 	i+=1
	# print(arr)
	# print(len(set(arr)))
	s=set()
	for i in arr:
		if i in s:
			i=i+1
		s.add(i)
	print(len(s))
