import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
l=input()
r=input()
ans=0
for i in range(int(l)+1,int(r)+1):
	count1=0
	count2=0
	num=i
	while num>0:
		rem=num%10
		if rem%2==0:
			count1+=1
		else:
			count2+=1
		num=num//10
	if count1%2==1 and count2%2==0:
		ans+=1
print(ans%(10**9+7))

