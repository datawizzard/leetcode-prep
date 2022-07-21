import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# logic behind code:
 # Aditya Verma DP playist
 # This questions resembles the equal partititon sum problem and 
 # subset sum problem.First we have to form table for all subset sum problem
 # Subset sum problem return true when subset->sum gives the sum of any
 # particular subset.s is the total sum of the array and it is maximum range of
 # sum that any subset sum could have.So it return when there is sum within the
 # range else return false.We have to find min(s2-s1) and s2 is nothing
 # but s-s1.So the equation became s-2*s1.So, now we have s given
 # constant so we only have to maximize s1 so that s-2*s1 become minimum.
 # In order to maximize s1 we have to find sum of subset which is maximum
 # till s//2 as other s//2 sum will be in s2 subset.So check the dp table
 # of subset_sum having maximum sum of a subset till s//2 for the last
 # row of table as last row give output taken n element as consideration.


def find_min(arr,n):
	s=0
	s=sum(arr)
	dp=[[False for j in range(s+1)] for i in range(n+1)]
	for i in range(n+1):
		for j in range(s+1):
			if i==0 and j==0:
				dp[i][j]=True
			elif j==0:
				dp[i][j]=True
			elif i==0:
				dp[i][j]=False
		for i in range(1,n+1):
			for j in range(1,s+1):
				if arr[i-1]>j:
					dp[i][j]=dp[i-1][j]
				else:
					dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
	dif=sys.maxsize
	for j in range(s//2,-1,-1):
		if dp[n][j]==True:
			dif=s-2*j
			break;
	return dif
for _ in range(int(input())):
	arr=list(map(int,input().split()))
	n=len(arr)
	print(find_min(arr,n))


