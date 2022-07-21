import sys
import os
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
s=input()
n=input()
x=s.lower()
y=n.lower()
l=0
c=0
while l<len(s):
	if x[l:l+len(n)]==y:
		c+=1
	l+=1
print(c)