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
s,s1,s2=0,0,0
for _ in range(II()):
	x,y,z=MI()
	s+=x
	s1+=y
	s2+=z
if s==0 and s1==0 and s2==0:
	print("YES")
else:
	print("NO")