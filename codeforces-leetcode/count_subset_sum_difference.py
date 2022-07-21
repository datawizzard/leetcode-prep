import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# A recursive solution for subarr sum1
# problem

# Returns true if there is a subarr
# of arr[] with sun equal to given sum1
# Logic :
# target diff=given
# total sum of array = we can find
# sum(s1)+sum(s2)=sum(arr)
# sum(s1)-sum(s2)= target diff

# Equating both above equation we get:
# sum(s1)=(sum(arr)+target diff)/2
# means we have to find taget sum s1 to find subset sum difference count
# for target diff.As we have already done count_subset_sum.This problem changed
# to that one with some minor changes.
# Recursive Solution
def isSubsetSum(arr, n, sum1,s,diff):
	sys.setrecursionlimit(1000000000)
	# Base Cases
	if (sum1 == 0):
		return 1
	if (n == 0):
		return 0
	if diff>s:
		return 0
	# If last element is greater than
	# sum1, then ignore it
	if (arr[n - 1] > sum1):
		return isSubsetSum(arr, n - 1, sum1,s,diff)

	# else, check if sum1 can be obtained
	# by any of the following
	# (a) including the last element
	# (b) excluding the last element
	# here we are using "+" because we have to find all subset recursively
	# and sum up if we find desired subset(either by choosing element or
	# either not choosing that element)
	return isSubsetSum(arr,n-1,sum1,s,diff) + isSubsetSum(arr,n-1,sum1-arr[n-1],s,diff)
diff=int(input())
arr=list(map(int,input().split()))
s=sum(arr)
r=int((s+diff)/2)
n = len(arr)
print(isSubsetSum(arr, n,r,s,diff))

# Dynamic Approach
# Logic :
# target diff=given
# total sum of array = we can find
# sum(s1)+sum(s2)=sum(arr)
# sum(s1)-sum(s2)= target diff

# Equating both above equation we get:
# sum(s1)=(sum(arr)+target diff)/2
# means we have to find taget sum s1 to find subset sum difference count
# for target diff.As we have already done count_subset_sum.This problem changed
# to that one with some minor changes.
def isSubset(arr,n,diff):
	s=sum(arr)
	sum1=(s+diff+1)//2
	a=[[0 for j in range(sum1+1)]for i in range(n+1)]
	for i in range(n + 1):
		a[i][0] = 1
	for j in range(1,sum1 + 1):
		a[0][j] = 0
	i,j=0,0
	for i in range(1,n+1):
		for j in range(1,sum1+1):
			if arr[i-1] > j:
				a[i][j]= a[i-1][j]
			elif j>=arr[i-1]:
				a[i][j]=(a[i-1][j] + a[i-1][j-arr[i-1]])
	# for i in range(n+1):
	# 	for j in range(sum1+1):
	# 		print(a[i][j],end=" ")
	# 	print()
	return a[i][j]

	# return a[n][sum1];
diff=int(input())
arr=list(map(int,input().split()))
n=len(arr)
print(isSubset(arr,n,diff))


