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

n,k = MI()
a = LI()
ans,s =[0]*n,0
a.sort()
# print(a)

# BRUTE FORCE


# a.sort(reverse =True)
# print(a)
# r = []
# for i in range(0,n):
# 	s  = 0
# 	day = 1
# 	l = math.ceil(n-i/k)
# 	for j in range(i,n,k):
# 		s += sum(a[j:j+k])*day
# 		day += 1
# 	r.append(s)
# print(*r[::-1])
# print(a)

# VIKASH GOPE LOGIC
p = 0
for i in range(n):
	p += a[i]
	ans[i] += p
	if i >=k:
		ans[i] += ans[i-k]
	print(ans[i],end=" ")


		