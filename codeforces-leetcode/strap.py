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
# def seive(n):
# 	prime = [True for i in range(n+1)]
# 	prime[0] = False
# 	prime[1] = False
# 	for i in range(2,int(math.sqrt(n))+1):
# 		if prime[i] == True:
# 			for j in range(i*i,n+1,i):
# 				prime[j] =False
# 	return prime
# prime = seive(1000001)
# p = 0
# m={}
# for i in range(1000001):
# 	m[i] = 0
# ans = [0]*(1000001)
# a = []
# for i in range(1000001):
# 	if prime[i]==True:
# 		m[i]+=1
# 		a.append(i)
# 		if len(a)>=2:
# 			if m[i-a[len(a)-2]]>0:
# 				p+=1
# 	ans[i] = p
# # print(m)
# # print(a)
# for _ in range(II()):
# 	n = II()
# 	print(ans[n])
def seive(n):
	prime = [True for i in range(n+1)]
	prime[0] = False
	prime[1] = False
	for i in range(2,int(math.sqrt(n))+1):
		if prime[i] == True:
			for j in range(i*i,n+1,i):
				prime[j] =False
	return prime
prime = seive(1000001)
ans = [0]*(1000001)
p = 0
for i in range(2,1000001):
	if prime[i] == True and prime[i-2] == True:
		p += 1
	ans[i] = p
for _ in range(II()):
	n = II()
	print(ans[n])
