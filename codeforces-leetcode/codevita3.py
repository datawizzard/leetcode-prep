import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
v=list(map(int,input().split()))
n=len(v)
nse=[]*n
pse=[]*n
pse[0]=-1
stack=[]
stack.append(n-1)
for i in range(n-2,0,-1):
	while(len(stack)!=0 and v[stack[-1]]>v[i]):
		stack.pop()
	if len(stack)==0:
		nse[i]=n
	else:
		nse[i]=stack[-1]
		stack.append(i)
while(len(stack)!=0):
	stack.pop()
stack.append(0)
for i in range(1,n):
	while(len(stack)!=0 and v[stack[-1]]>v[i]):
		stack.pop()
	if len(stack)==0:
		pse[i]=-1
	else:
		pse[i]=stack[-1]
		stack.append(i)
mam=0
for i in range(0,n):
	mam=max(mam,(nse[i]-pse[i]-1)*v[i])
return mam
