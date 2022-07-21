import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
import heapq
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
def isPerfectSquare(x): return (int(math.sqrt(x))**2 == x)
# arr = list(map(int,input().split()))
# a = "".join(map(str,arr))
# a = sorted(a,reverse = True)
# print("".join(a))

n = int(input())
k = int(input())
s = bin(n)
print(s)