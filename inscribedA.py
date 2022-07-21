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
n=II()
s=LI()
flag , ans= 0, 0
for i in range(1,n):
	if s[i] == 1:
		if s[i-1]==2:
			ans += 3
		else:
			ans += 4
	elif s[i] == 2:
		if s[i-1] == 1:
			ans += 3
		else:
			flag = 1
			break;
	elif s[i] == 3:
		if s[i-1] == 2:
			flag = 1
			break;
		else:
			ans += 4
for i in range(2,n):
	if s[i-2] == 3 and s[i-1] == 1 and s[i] == 2:
		ans -= 1
if flag:
	print("Infinite")
else:
	print("Finite")
	print(ans)