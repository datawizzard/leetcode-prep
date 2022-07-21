import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
d1,v1,d2,v2,p=map(int,input().split())
sum1,ans=0,0
ans=min(d1,d2)-1
l=d1
m=d2
if m<=l:
	while sum1<=p:
		while d2<d1 and sum1<=p:
			sum1+=v2
			ans+=1
			d2+=1
			if sum1>=p:
				break
			#print(sum1,ans)
		if sum1>=p:
			break;
		sum1+=(v1+v2)
		ans+=1
		#print(sum1,ans,"g")
else:
	while sum1<=p:
		while d1<d2 and sum1<=p:
			sum1+=v1
			ans+=1
			d1+=1
			if sum1>=p:
				break;
		if sum1>=p:
			break;
		sum1+=(v1+v2)
		ans+=1
		#print(sum1,ans)
#print(sum1)
print(ans)
