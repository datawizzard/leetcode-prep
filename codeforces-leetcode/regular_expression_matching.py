import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

# Logic By : Prateek Shukla Youtube

def regular_exp(a,b,n,m):
	dp=[[False for j in range(m+1)] for i in range(n+1)]
	dp[0][0]=True
	for j in range(1,m+1):
		# if we find * in b then character just before the 
		# the * can we deleted or incresed so if the table is true
		# before the two places of '*'  .e j-2 where j is position
		# of * then set the position of '*' true
		if b[j-1]=='*' and dp[0][j-2] ==True:
			dp[0][j]=True
	for i in range(1,n+1):
		for j in range(1,m+1):
			# if two character are same ,check whether the all of 
			# previous of character till that i and j return true  
			# or not if yes set true.Here i-1,j-1 return the 
			# value of previous subproblem also if there is '.' 
			# it means that can also become any character 
			# in order to become equal.
			if a[i-1]==b[j-1] or b[j-1] == '.':
				dp[i][j] = dp[i-1][j-1]
			elif b[j-1]=='*':
				# '*' always comes with pair hence if char before 
				# '*' is equal to char at i then two case arises
				# 1) We want to add that '*' character element
				# 	If we want to add check one row above for that element
				#  i.e dp[i-1][j]
				# 2) We don't want to add that element
				#  If we don't want to add that characcter '*' check two col 
				#  before that '*' col ,ie dp[i][j-2] 
				#  And choose between either of them i.e doing or operation.
				if b[j-2]==a[i-1] or b[j-2]=='.':
					dp[i][j] = dp[i][j-2] or dp[i-1][j]
					# if char before '*' does not equal to char at i
					# then check char 2 place before '*' and store that
					# value
				else:
					dp[i][j] = dp[i][j-2]
	for i in range(n+1):
		for j in range(m+1):
			print(dp[i][j],end=" ")
		print()
	return dp[n][m]
for _ in range(int(input())):
	a=input()
	b=input()
	n=len(a)
	m=len(b)
	print(regular_exp(a,b,n,m))
