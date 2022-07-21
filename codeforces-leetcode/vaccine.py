import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
d1,v1,d2,v2,p=map(int,input().split())
min1=min(d1,d2)
max1=max(d1,d2)
ans=min1-1
sum1=0
l=min1
m=max1
while sum1<=p:
	while l<m and sum1<=p:
		if min1==d1:
			sum1+=v1
			l+=1
			ans+=1
		elif min1==d2:
			sum1+=v2
			l+=1
			ans+=1
print(ans)
