import sys
# sys.stdin=open('input.txt','r')
# sys.stdout=open('output.txt','w')
# import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
for _ in range(II()):
	s=I()
	s=sorted(s)
	# print(s)
	i,j=0,len(s)-1
	even=[]
	odd=[]
	for i in range(len(s)):
		if ord(s[i])%2==0:
			even.append(s[i])
		else:
			odd.append(s[i])
	flag=0
	# print(odd)
	# print(even)
	l=even + odd
	# print(l)
	for i in range(len(l)-1):
		if abs(ord(l[i]) - ord(l[i+1])) == 1:
			print("No answer")
			flag=1
			break;
	if flag==0:
		print("".join(even+odd))


