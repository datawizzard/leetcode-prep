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
a = [0,20,36,51,60]
b = [0,0,0,0,60,76,88,99]
for _ in range(II()):
	n = II()
	if n <= 4:
		print(a[n])
	else:
		x = n // 4
		ans = 44 * (x - 1)
		res = n - (x - 1) * 4
		print(ans + b[res])

