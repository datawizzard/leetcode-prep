import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# Question 
# Given two string find whether one whole string is subsequence
# of other or not
def lcs(X,Y,n,m):
	for i in range(n+1):
		for j in range(m+1):
			if i==0 or j==0:
				dp[i][j]=0
	for i in range(1,n+1):
		for j in range(1,m+1):
			# The idea is to find the LCS(X,X)where X
			# is the input string with the restriction that 
			# when both the characters are same, they shouldn’t
			#  be on the same index in the two strings.
			if X[i-1]==Y[j-1] and i!=j:
				dp[i][j]=1+dp[i-1][j-1]
			else:
				dp[i][j]=max(dp[i][j-1],dp[i-1][j])
	# for i in range(n+1):
	# 	for j in range(m+1):
	# 		print(dp[i][j],end=" ")
	# 	print()

	# if lcs is equal to length of smaller string 
	# it means one whole string is subsequence
	# of other else not
	if dp[i][j]=min(n,m):
		return True
	else:
		return False
X=input()
Y=X[:]
dp=[[0 for j in range(len(Y)+1)] for i in range(len(X)+1)]
print(lcs(X,Y,len(X),len(Y)))