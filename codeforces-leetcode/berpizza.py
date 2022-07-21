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
k=1
d={}
for _ in range(II()):
	arr = LI()
	if arr[0] == 1:
		d[k] = arr[1]
		k += 1
		print(d)
	elif arr[0] == 2:
		l = min(d)
		print(l,end=" ")
		d.pop(l)
	elif arr[0] == 3:
		l = (max(d, key=d.get))
		print(l,end=" ")
		d.pop(l)
