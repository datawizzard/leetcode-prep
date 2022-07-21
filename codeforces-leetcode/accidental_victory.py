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
# for _ in range(II()):
# 	n = II()
# 	a = LI()
# 	v = []
# 	for i,j in enumerate(a):
# 		v.append((j,i))
# 	v.sort()
# 	# print(v)
# 	pref = [0]*n
# 	pref[0] = v[0][0]
# 	for i in range(1,n):
# 		pref[i] = pref[i-1] + v[i][0]
# 	# print(pref)
# 	ans = []
# 	ans.append(v[n-1][1] + 1)
# 	vis = [0]*n
# 	vis[n-1] = 1
# 	for i in range(n-2,-1,-1):
# 		if (pref[i] >= v[i + 1][0] and vis[i + 1]):
# 			ans.append(v[i][1] + 1);
# 			vis[i] = True;
# 	ans.sort()
# 	print(len(ans))
# 	print(*ans)

# for _ in range(II()):
# 	n = II()
# 	s=0
# 	z=[]
# 	for x,i in sorted((x,i+1)for i,x in enumerate(LI())):
# 		# print(x,i)
# 		if s<x:
# 			z=[]
# 		s+=x
# 		z.append(i)
# 		# print(s,z)
# 	print(len(z))
# 	print(*sorted(z))

def win(pos : int, a : list):
    power = a[pos]
    for i in range(len(a)):
        if i == pos:
            continue
        if power < a[i]:
            return False
        power += a[i]
    return True

t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    a = list(map(int, input().split(' ')))
    b = a.copy()
    a.sort()

    l = -1
    r = n - 1
    while r > l + 1:
        m = (l + r) // 2
        if (win(m, a)):
            r = m
        else:
            l = m

    winIds = []
    for i in range(n):
        if b[i] >= a[r]:
            winIds.append(i + 1)

    print(len(winIds))
    print(*winIds)

