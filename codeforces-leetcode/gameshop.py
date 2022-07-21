import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n,m=map(int,input().split())
c=list(map(int,input().split()))
a=list(map(int,input().split()))
a.reverse()
ans=0
for i in c:
	if i<=a[-1]:
		ans+=1
		a.pop()
	if ans==m:
		break
print(ans)

