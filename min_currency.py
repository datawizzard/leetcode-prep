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
d = II()
e = II()
t = n
i=0
while 5 * i * e < n + 1:
	t = min(t,(n - 5 * i * e) % d )
	i += 1
print(t)