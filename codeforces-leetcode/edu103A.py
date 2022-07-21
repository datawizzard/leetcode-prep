# import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
# import sys
# import math
# def input(): return sys.stdin.readline().strip("\n")
# def I():    return (input())
# def II():    return (int(input()))
# def MI():    return (map(int,input().split()))
# def LI():    return (list(map(int,input().split())))
# for _ in range(II()):
# 	n,k = MI()
# 	a = n
# 	i = 1
# 	if n > k:
# 		t = math.ceil(n/k)
# 		print(math.ceil(t*k/n))
# 	else:
# 		t = math.ceil(k/n)
# 		print(t)
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
	a = n
	i = 1
	if k == 1:
		print(1)
	elif n == 1:
		print(k)
	elif n%k == 0:
		print(1)
	else:
		t = math.ceil(a/k)
		# while i*k < a:
		# 	i += 1
		print(math.ceil(t*k/n))
 
