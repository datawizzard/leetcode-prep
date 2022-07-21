import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

# This is the same question as lcs just we have to print string
# instead of length of the string.
# so we have to do same thing just lookup the table from reverse
# and check when the items are same in the table.
# concatenate the empty string after each iteration when both the 
# character of string are same in the table .

# LCS Table Part
def lcs(X,Y,n,m):
	for i in range(n+1):
		for j in range(m+1):
			if i==0 or j==0:
				dp[i][j]=0
	for i in range(1,n+1):
		for j in range(1,m+1):
			if X[i-1]==Y[j-1]:
				dp[i][j]=1+dp[i-1][j-1]
			else:
				dp[i][j]=max(dp[i][j-1],dp[i-1][j])
	# for i in range(n+1):
	# 	for j in range(m+1):
	# 		print(dp[i][j],end=" ")
	# 	print()
	# return dp[i][j]

	# Printing part for longest common subsequence.
	s=""
	while i>0 and j>0:
		if X[i-1]==Y[j-1]:
			s=s+X[i-1]
			i-=1
			j-=1
		elif dp[i-1][j]<dp[i][j-1]:
			j-=1
		else:
			i-=1
	return s[::-1]
X=input()
Y=input()
dp=[[0 for j in range(len(Y)+1)] for i in range(len(X)+1)]
print(lcs(X,Y,len(X),len(Y)))

# s = ""
# while i<n and j<n:
# 	if a[i+1]==b[i+1]:
# 		s = s + a[i+1]
# 		i += 1
# 		j += 1
# 	else:
# 		dp[i+1][j] < dp[i][j+1]:
# 		j += 1
# 	else:
# 		i += 1
# 	print(s)