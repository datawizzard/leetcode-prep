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
for _ in range(II()):
	n,k = MI()
	a = LI()
	# x = a[0]
	# y = a[-1]
	# p = min(x,k)
	# # print(p)
	# x -= p
	# y += p
	# a[0] ,a[-1] = x,y
	# for i in a:
	# 	print(i,end =" ")
	# print()
	i,j=0,n-1
	while i < j:
		x = a[i]
		y = a[j]
		p = min(x,k)
		# print(p)
		a[i] -= p
		a[j] += p
		k -= p
		i += 1
	for i in a:
		print(i,end =" ")
	print()