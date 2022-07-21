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
	s = I()
	x =II()
	flag=0
	a=['1']*(len(s))
	for i in range(0,len(s)):
		if s[i]=='0':
			if i>=x:
				a[i-x] = '0'
			if i+x<len(s):
				a[i+x] = '0'
	# print(a)
	# if a can be changed to s it means a is ans else -1
	r=a[:]
	for i in range(len(s)):
		if i>=x and a[i-x]=='1' or i+x<len(s) and a[i+x]=='1':
			r[i]='1'
		else:
			r[i]='0'
	r="".join(r)
	if r==s:
		print("".join(a))
	else:
		print(-1)
