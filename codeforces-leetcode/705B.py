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
# Python program to reverse a number 
def rever(n):
	x = str(n)
	y = x[::-1]
	# print(y)
	y = list(y)
	for i in range(2):
		if y[i] == '2':
			y[i] ='5'
		elif y[i] == '5':
			y[i] = '2'
	z = "".join(y)
	z = int(z)
	# print(z)
	return z


def check(c,d):
	r = ""
	r = str(c).zfill(2) + str(d).zfill(2)
	x = str(c).zfill(2)
	y = str(d).zfill(2)
	# print(r,rever(x),rever(y))
	f = ["1","2","5","8","0"]
	if all(i in f for i in r) and rever(x) < m and rever(y) < h:
		return True
	return False
for _ in range(II()):
	h,m = MI()
	s = I()
	hour,minute = s.split(":")
	a = int(hour)
	b = int(minute)
	while check(a,b) is False:
		b += 1
		if b == m:
			a += 1
		b = b % m
		a = a % h
	print(str(a).zfill(2),":",str(b).zfill(2),sep="")
	# print(hour,minute,k)

