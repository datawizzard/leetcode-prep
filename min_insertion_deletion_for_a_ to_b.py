import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
 # question:
 # Find minimum number of insertion and deletion needed to 
 # make change a string from a to b.
def lcs(X,Y,n,m):
	for i in range(n+1):
		for j in range(m+1):
			if i==0 or j==0:
				dp[i][j]=0
	for i in range(1,n+1):
		for j in range(1,m+1):
			# both the element have same character(starting from last)
			# if both the character are same move the string to 1 left and
			# and increase the length by 1 that why we have used 1+
			if X[i-1]==Y[j-1]:
				dp[i][j]=1+dp[i-1][j-1]
			else:
				# if the character are different we have two choice
				# keep the first string as it is and move 1 step left in 2nd 
				# string and 2nd choice is vice versa.It is done recursively
				# you can see i have decrease m-1 i.e len of string 2 in first 
				# case and n-1 in second case and return the max of both.
				dp[i][j]=max(dp[i][j-1],dp[i-1][j])
	# for i in range(n+1):
	# 	for j in range(m+1):
	# 		print(dp[i][j],end=" ")
	#	print()
	len_lcs=dp[i][j]
	# we have remove length of common subsequence from the string
	# and print length of length of resultant string.
	# here we use 2* lcs to remove lcs for both string 1 lcs for 1st
	# string and other lcs for other string.
	return len(X)+len(Y)-2*len_lcs
X=input()
Y=input()
dp=[[0 for j in range(len(Y)+1)] for i in range(len(X)+1)]
print(lcs(X,Y,len(X),len(Y)))

