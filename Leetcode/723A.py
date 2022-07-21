import sys
def input(): return sys.stdin.readline().strip("\n")
def II():    return (int(input()))
def LI():    return (list(map(int,input().split())))
for _ in range(II()):
	n = II()
	a = LI()
	a.sort()
	i,j = 0,2*n-1
	while i < j:
		print(a[i],end=" ")
		print(a[j],end=" ")
		i+=1
		j-=1
	print()