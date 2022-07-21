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
from bisect import bisect
# a = []
# for i in range(1,10000):
# 	a.append(pow(i,3))
# # print(a)
# for _ in range(II()):
# 	n = II()
# 	flag = 0
# 	for i in a:
# 		l = bisect(a,n-i)
# 		if l != len(a)+1 and a[l-1] == n - i:
# 			flag = 1
# 			break;
# 	if flag == 1:
# 		print("YES")
# 	else:
# 		print("NO")

a = []
for i in range(1,10000):
	a.append(pow(i,3))
# print(a)
for _ in range(II()):
	n = II()
	flag = 0
	i = 1
	while i*i*i <= n:
		l = bisect(a,n-i*i*i)
		if l != len(a)+1 and a[l-1] == n - i*i*i:
			flag = 1
			break;
		i += 1
	if flag == 1:
		print("YES")
	else:
		print("NO")

	