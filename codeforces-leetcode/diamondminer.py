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
	n = II()
	diamond = []
	miners = []
	for _ in range(2*n):
		x,y = MI()
		x =abs(x)
		y =abs(y)	
		if x == 0:
			diamond.append((x,y))
		elif y == 0:
			miners.append((x,y))
	diamond.sort()
	miners.sort()
	ans = 0
	# print(diamond)
	# print(miners)
	for i in range(n):
		ans += pow(pow((diamond[i][1] - miners[i][1]),2) + pow((diamond[i][0] - miners[i][0]),2),0.5)
	print(ans)