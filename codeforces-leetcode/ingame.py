import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	s=input()
	s=s[::-1]
	c=0
	for i in range(n):
		if s[i]==')':
			c+=1
		else:
			break;
	if c>n-c:
		print("YES")
	else:
		print("NO")
