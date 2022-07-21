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
def solution (a, b, n):  
    i = 0
    while i * a <= n: 
        if (n - (i * a)) % b == 0: 
            return "YES"
        i = i + 1
    return "NO"
for _ in range(II()):
	n = II()
	a = 2020
	b = 2021
	print(solution(a,b,n))
	