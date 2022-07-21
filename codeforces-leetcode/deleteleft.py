import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
s=input()
t=input()
w=0
while(True):
	i=len(s)-w-1
	j=len(t)-w-1
	if i>=0 and j>=0 and s[i]==t[j]:
		w+=1
	else:
		break;
print(len(s)+len(t)-2*w)