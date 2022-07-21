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
	k -= 1
	no_of_col,pos_b = 0,0
	if n % 2 == 1:
		p = n // 2
		print(p)
		no_of_col = k // p
	pos_b = no_of_col + k
	print(pos_b % n + 1)
	

