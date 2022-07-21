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
	n = II()
	a = list(map(int,input()))
	b = list(map(int,input()))
	one,zero,j =0,0,0
	if a == b:
		print("YES")
	else:
		x = []
		for i in range(n):
			if a[i] == 1:
				one += 1
			else:
				zero += 1
			if zero == one:
				x.append([j,i])
				j = i + 1
		for i in x:
			if a[i[0]] == b[i[0]]:
				continue;
			else:
				for k in range(i[0],i[1]+1):
					if a[k] == 1:
						a[k] = 0
					else:
						a[k] = 1
		if a ==b:
			print("YES")
		else:
			print("NO")
					
