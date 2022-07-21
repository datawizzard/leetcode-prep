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
# def printn(n):
# 	if n == 1:
# 		print(1)
# 		return
# 	print(n)
# 	printn(n-1)
# 	print(n)
# n = II()
# printn(n)
# def recur(n):
# 	if n == 1:
# 		return 2
# 	if n == 2:
# 		return 3
# 	else:
# 		return recur(n-1) + recur(n -2)
# n = II()
# print(recur(n))
# def noways(n):
# 	if n == 0:
# 		return 0
# 	if n == 1:
# 		return 1
# 	else:
# 		return noways(n-1) + (n-1)*noways(n-2)
# n = II()
# print(noways(n))
# def cuberoot(a,b):
# 	if b == 0:
# 		return 1
# 	else:
# 		return a * cuberoot(a,b-1)
# a,b = MI()
# print(cuberoot(a,b))

# Recursive pattern print using for loop and recursion
# def pattern(n,i):
# 	if n == 0:
# 		return
# 	for i in range(n):
# 		print("*",end=" ")
# 	print()
# 	return pattern(n-1)
# n = II()
# pattern(n)

# Recursive patter print without using for loop

# def pattern(n,i):
# 	if n == 0:
# 		return
# 	if i < n:
# 		print("*",end=" ")
# 		pattern(n,i+1)
# 	else:
# 		print() 
# 		pattern(n-1,0)
# n = II()
# pattern(n,0)

def recur()
