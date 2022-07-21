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
for _ in range(II()):
	n,k = MI()
	s = I()
	# print(s[:-k-1:-1])
	if n == 2 * k or s[:k] != s[:-k-1:-1]:
		print("NO")
	else:
		print("YES")


