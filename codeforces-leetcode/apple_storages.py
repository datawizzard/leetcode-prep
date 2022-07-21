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
# n = II()
# a = LI()
# k = [0]*(10**5+5)
# cnt = [0]*(10**5+5)
# for i in a:
# 	k[i] += 1
# 	cnt[k[i]] += 1
# for i in range(II()):
# 	s,v = I().split()
# 	v = int(v)
# 	if s == '+':
# 		k[v] += 1
# 		cnt[k[v]] += 1
# 	else:
# 		cnt[k[v]] -= 1
# 		k[v] -= 1
# 	if cnt[8] > 0 or cnt[4] >= 2 or (cnt[6] > 0 and cnt[2] >= 2 ) or (cnt[4] > 0 and cnt[2] >= 3):
# 		print("YES")
# 	else:
# 		print("NO")
from collections import Counter
import heapq
n = II()
a = LI()
cnt = Counter(a)
for i in range(II()):
	s,v = I().split()
	v = int(v)
	if s == '+':
		if v in cnt:
			cnt[v] += 1
		else:
			cnt[v] = 1
	else:
		cnt[v] -= 1
	# print(cnt)
	# z = sorted(cnt.values(),reverse = True)[:3]
	z = (heapq.nlargest(3,cnt.values()))
	# print(z)
	if len(z)<3:
		z.append(0)
	# print(z)
	if z[0] >= 8 or (z[0] >= 4 and z[1] >= 4) or (z[0] >=6 and z[1] >= 2) or (z[0] >= 4 and z[1] >=2 and z[2] >= 2):
		print("YES")
	else:
		print("NO")