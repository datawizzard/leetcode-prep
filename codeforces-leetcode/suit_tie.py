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
a = LI()
vis,minswaps= [0 for i in range(n+1)],0
# def minswaps(a,n,count):
# 	if n == 1 or n <0:
# 		return count;
# 	elif a[n-1] == a[n-2]:
# 		return minswaps(a,n-2,count)
# 	else:
# 		return 1 + minswaps(a,n-1,count)
# if __name__ == '__main__':
# 	n = II()
# 	a = LI()
# 	count = 0
# 	print(minswaps(a,2*n,count))

for i in range(2*n):
	ans = 0
	if vis[a[i]] == 0:
		vis[a[i]] = 1
	for j in range(i+1,2*n):
		if vis[a[j]] == 0:
			ans += 1
			print(vis,ans)
		elif a[i] == a[j]:
			print(ans)
			minswaps += ans
print(minswaps)

