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
	n,k = MI()
	a = LI()
	b = sorted(set(a))
	bset = set(b)
	if k == 0:
		ans = n
		print(ans)
		continue;
	for i in range(max(b) + 2):
		if i not in bset:
			mex = i
			break;
	maxi = max(b)
	if mex == maxi + 1:
		ans = n + k
		print(ans)
	elif maxi > mex:
		# print(maxi,mex)
		z = math.ceil((mex + maxi)/2)
		bset.add(z)
		print(len(bset))





