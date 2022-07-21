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
	s = input()
	print(s[:-1])
	if all(i == 'a' for i in s):
		print("NO")
	else:
		print("YES")
		if s == s[::-1]:
			s = "a" + s
		else:
			s = s[:len(s)//2] + "a" + s[len(s)//2:]
		print(s)