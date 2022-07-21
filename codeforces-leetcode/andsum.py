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
n = II()
a =[1]
prod = 1
for i in range(2,n):
	if math.gcd(n,i) == 1:
		a.append(i)		
for i in a:
	prod = (prod*i)% n
# print(prod%12)

if prod == 1:
	print(len(a))
	print(*a)
else:
	a.remove(prod)
	a.sort()
	print(len(a))
	print(*a)
	