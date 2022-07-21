import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n=int(input())
str1=input()
c,c1=0,0
for i in range(n):
	if str1[i]=='A' and i!=0 and str1[i-1]=='':
		
	elif str1[i]=='B':
		c1+=1
if c>c1:
	print("A")
elif c<c1:
	print("B")
else:
	print("Coalition government")