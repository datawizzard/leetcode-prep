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




# n = int(input())
# a = list(map(int,input().split()))
# i,j = 0,n-1
# while i <= j:
# 	print(a[j],end=" ")
# 	if i != j:
# 		print(a[i],end=" ")
# 	j -= 1
# 	i += 1




n = int(input())
s = 0
for i in range(n):
	if i % 2 == 0:
		s += 6
	else:
		s += 2
print(s)