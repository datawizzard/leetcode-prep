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
	a = LI()
	switch = 0
	for i in range(n - 1):
		x = 0
		for j in range(i+1):
			x ^= a[j]
		flag = 0
		t = 0
		for j in range(i + 1,n):
			t ^= a[j]
			if t == x:
				flag = 1
				t = 0
		if t == 0 and flag == 1:
			print("YES")
			switch = 1
			break;
	if switch == 0:
		print("NO")

