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
for _ in range(II()):
	n = II()
	c = LI()
	a = LI()
	b = LI()
	ans,ans1,ans2,prevans,bestans = 0,0,0,0,0
	for i in range(1,n):
		if (a[i] == b[i]):
			prevans = c[i] + 1;
			bestans = max(prevans, bestans)
			print(bestans,prevans,ans,"gg")
		else:
			print(i)
			ans1 = prevans - (abs(b[i] - a[i])) + c[i] + 1
			ans2 = c[i] + 1 + abs(b[i] - a[i])
			print(ans1,ans2,"mid")
			ans = max(ans1, ans2)
			bestans = max(ans, bestans)
			prevans = ans
			print(bestans,prevans,ans,"low")
	print(bestans)