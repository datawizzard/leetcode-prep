import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

# Normal Version

def is_palindrome(s,i,j):
	t=s[i:j+1]
	return t==t[::-1]
def minpalpartition(s,i,j):	
	if i>=j:
		return 0
	if dp[i][j]!=-1:
		return dp[i][j]
	if is_palindrome(s,i,j):
		return 0
	temp=sys.maxsize
	for k in range(i,j):
		temp= min(temp,1 + minpalpartition(s,i,k) + minpalpartition(s,k+1,j))
	return temp
for _ in range(int(input())):
	n=int(input())
	s=input()
	dp=[[-1 for r in range(n+1)] for m in range(n+1)]
	print(minpalpartition(s,0,n-1))

# Optimized One
def minpalpartition(s,i,j):
    def isPalindrome(start, end):
        while(start < end):
            if( s[start] != s[end] ):
                return False
            start += 1
            end -= 1
        return True
    
    n = len(s)
    dp = [n-1] * n
    dp[0] = 0
    if isPalindrome(0, n-1):
        return 0
    for i in range(1, len(s)):
        if isPalindrome(0, i-1) and isPalindrome(i,n-1):
            return 1
    for i in range( 1, n ):
        for j in range( i+1 ):
            if( isPalindrome(j,i) ):
                dp[i] = min( dp[i], dp[j-1] + 1 ) if(j > 0) else 0
    return dp[-1]
for _ in range(int(input())):
	n=int(input())
	s=input()
	dp=[[-1 for r in range(n+1)] for m in range(n+1)]
	print(minpalpartition(s,0,n-1))