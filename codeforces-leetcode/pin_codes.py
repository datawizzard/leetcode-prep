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
for _ in range(II()):
	n = II()
	arr = []
	s =set()
	for i in range(n):
		a = I()
		arr.append(a)
		s.add(a)
	if len(s) == n:
		print(0)
		for i in s:
			print(i)
	else:
		res=0
		for i in range(n):
			if arr[i] in arr[i+1:]:
				res+=1
				j=9
				while arr[i] in arr[:i] + arr[i+1:]:
					arr[i]=arr[i][:3] + str(j)
					j -= 1
		print(res)
		for i in range(n):
			print(arr[i])  