import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
s=input()
d={}
ans=0
for i in s:
	if i not in d:
		d[i]=1
	else:
		d[i]+=1
for i in d:
	if d[i]==1:
		ans+=1
if ans==0:
	print(0)
else:
	print(ans)

