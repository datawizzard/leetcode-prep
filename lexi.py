import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
s=input()
p=""
ank=s[0]
for i in range(1,len(s)):
	ank=min(ank,s[i])
for i in range(0,len(s)):
	if s[i]==ank:
		p+=s[i]
print(p)