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
import math
for i in range(II()):
	n,m,x = MI()
	row = (x % n)
	if x % n == 0:
		row = n
	col = int((x / n) + ((x % n) != 0))
	# print(row,col)
	print(m*(row-1)+col)