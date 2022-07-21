# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
n = II()
add_str = '5'
if n == 0:
	print(50)
elif n > 0:
	res = 0
	s = str(n)
	for i in range(len(s)):
		ans = s[:i] + add_str + s[i:]
		ans = int(ans)
		res = max(ans,res)
	print(res)
elif n < 0:
	res = -99999
	n = abs(n)
	s = str(n)
	for i in range(len(s)):
		ans = s[:i] + add_str + s[i:]
		ans = int(ans)*(-1)
		res = max(ans,res)
	print(res)

