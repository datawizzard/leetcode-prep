import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
sys.setrecursionlimit(100000000)
# Logic behind the solution 
	# we can only partition array in two equal part if the sum of the 
	# array is of even length.If the array is of odd length
	# it is not possible to partition in two equal subset.
	# So if the sum of the array is even we have to only check for 
	# s//2 i.e if any part of subset form the sum=s//2 that means other
	# partition will lead to sum other part of s//2.So if s//2 is found after
	# summed up of any subset it will return true.
# Recursive method
# def equalsum(arr,n,sum1):
# 	if (sum1 == 0):
# 		return True
# 	if (n == 0):
# 		return False
# 	if arr[n-1]>sum1:
# 		return equalsum(arr,n-1,sum1)
# 	else:
# 		return equalsum(arr,n-1,sum1-arr[n-1]) or equalsum(arr,n-1,sum1)
# for _ in range(int(input())):
# 	# n=int(input())
# 	arr=list(map(int,input().split(",")))
# 	s=sum(arr)
# 	print(s)
# 	n=len(arr)
# 	if s%2==1:
# 		print(False)
# 	else:
# 		print(equalsum(arr,n,s//2))

# Dynamic Approach

def equalsum(arr):
	n=len(arr)
	if sum(arr)%2!=0:
		return False
	else:
		sum1=sum(arr)//2
		a=[[False for j in range(sum1+1)] for i in range(n+1)]	
		for i in range(n+1):
			for j in range(sum1 + 1):
				if i==0 and j==0:
					a[i][j]=True
				elif j==0:
					a[i][j]=True
				elif i==0:
					a[i][j]=False
		for i in range(1,n+1):
			for j in range(1,sum1 + 1):
				if arr[i-1]>j:
					a[i][j]=a[i-1][j]
				else:
					a[i][j]=a[i-1][j] or a[i-1][j-arr[i-1]]
		return a[n][sum1]
		# for i in range(n+1):
		# 	for j in range(sum1+1):
		# 		print(a[i][j],end=" ")
		# 	print()
		
for _ in range(int(input())):
	# n=int(input())
	arr=list(map(int,input().split()))
	n=len(arr)
	#print(s)
	print(equalsum(arr))

