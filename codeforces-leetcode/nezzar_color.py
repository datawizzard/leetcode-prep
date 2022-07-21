import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
def iscontains(a,d):
	while (a > 0):
		if (a % 10 == d):
			return True
		a = a//10
	return False
def solve(c,d):
	i = 0
	while 10 * i < c:
		if (c - (10 * i)) % d  == 0 :
			return "YES"
		i += 1
	return "NO"
for _ in range(II()):
	q,d = MI()
	arr = LI()
	for c in arr:
		if c >= 10 * d or iscontains(c,d) == True or c == d:
			print("YES")
		else:
			print(solve(c,d))
 
# Using DP
# import sys
# import math
# def isSubset(arr,n,sum1):
# 	a = [[False for j in range(sum1+1)] for i in range(n+1)]
# 	for i in range(n + 1):
# 		a[i][0] = True
# 	for j in range(1,sum1 + 1):
# 		a[0][j] = False
# 	for i in range(1,n+1):
# 		for j in range(1,sum1+1):
# 			if arr[i-1] > j:
# 				a[i][j]= a[i-1][j]
# 			elif j>=arr[i-1]:
# 				a[i][j]=(a[i-1][j] or a[i-1][j-arr[i-1]])
# 	return a[i][j]
# def isDigitPresent(x, d): 
# 	    while (x > 0): 	      
# 	        if (x % 10 == d): 
# 	            break	  
# 	        x = x // 10 
# 	    return (x > 0)     
# for _ in range(II()):
# 	q ,d = MI()
# 	arr = LI()
# 	l = []
# 	for i in range(1, 10*d): 
# 		if (i == d or isDigitPresent(i, d) or i%d==0): 
# 			l.append(i)
# 	for c in arr:
# 		if c >= 10 * d:
#  			print("YES")
# 		elif c == d:
#  			print("YES")
# 		elif isDigitPresent(c,d) == True:
#  			print("YES")
# 		else:
# 			if isSubset(l,len(l),c)== True:
# 				print("YES")
# 			else:
# 				print("NO")
