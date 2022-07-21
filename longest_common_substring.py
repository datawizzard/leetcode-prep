import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

# Logic : By Aditya Verma
	
def lcs(X,Y,n,m,count):
	# Base Case
	# if len of n or m is zero return 0
	if n==0 or m==0:
		return count;
	# both the element have same character(starting from last)
	elif X[n-1]==Y[m-1]:
		return max(count,1+lcs(X,Y,n-1,m-1,count))
	# if the character are different we have two choice
	# keep the first string as it is and move 1 step left in 2nd 
	# string and 2nd choice is vice versa.It is done recursively
	# you can see i have decrease m-1 i.e len of string 2 in first 
	# case and n-1 in second case and return the max of both.
	else:
		return max(count,max(lcs(X,Y,n,m-1,count),(lcs(X,Y,n-1,m,count))))
X=input()
Y=input()
print(lcs(X,Y,len(X),len(Y),0))


# Memoization Approach

def lcs(X,Y,n,m):
	# Base Case
	# if len of n or m is zero return 0
	if n==0 or m==0:
		return 0;
	# if value is not -1 it means it is already fiiled in the
	# and table value for that n and m is already stored in the table 
	# and we don't have to calculate it again.
	if dp[n][m]!=-1:
		return dp[n][m]
	# both the element have same character(starting from last)
	elif X[n-1]==Y[m-1]:
		dp[n][m]=1+lcs(X,Y,n-1,m-1)
		return dp[n][m]
	# if the character are different we have two choice
	# keep the first string as it is and move 1 step left in 2nd 
	# string and 2nd choice is vice versa.It is done recursively
	# you can see i have decrease m-1 i.e len of string 2 in first 
	# case and n-1 in second case and return the max of both.
	else:
		dp[n][m]=0
		return dp[n][m]
X=input()
Y=input()
dp=[[-1 for j in range(len(Y)+1)] for i in range(len(X)+1)]
print(lcs(X,Y,len(X),len(Y)))

# Dynamic Approach
def lcs(X,Y,n,m,res):
	for i in range(n+1):
		for j in range(m+1):
			if i==0 or j==0:
				dp[i][j]=0
	for i in range(1,n+1):
		for j in range(1,m+1):
			if X[i-1]==Y[j-1]:
				dp[i][j]=1+dp[i-1][j-1]
				res=max(res,dp[i][j])
			else:
				dp[i][j]=0
	return res
X=input()
Y=input()
dp=[[0 for j in range(len(Y)+1)] for i in range(len(X)+1)]
print(lcs(X,Y,len(X),len(Y)))