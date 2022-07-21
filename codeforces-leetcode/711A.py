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
def getSum(n):    
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)
for _ in range(II()):
	n = II()
	while math.gcd(n,getSum(n)) <= 1:
		n += 1
	print(n)
