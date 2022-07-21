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
import math
def nCr(n,r):
    f = math.factorial
    return f(n) // (f(r) * f(n-r))
for _ in range(II()):
	n,k = MI()
	arr = LI()
	arr.sort(reverse = True)
	m = arr[k-1]
	total,r= 0,0
	for i in arr:
		if i == m:
			total += 1
	for i in arr:
		if i > m:
			r += 1
	print(nCr(total,k-r)%(10**9+7))





