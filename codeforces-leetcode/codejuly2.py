import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def sumofdigits(x):
	sum1=0
	while x!=0:
		sum1+=x%10
		x=x//10
	return sum1
for _ in range(int(input())):
	n=int(input())
	count=0
	count1=0
	for _ in range(n):
		p=0
		q=0
		l,m=map(int,input().split())
		p=sumofdigits(l)
		q=sumofdigits(m)
		if p>q:
			count+=1
		elif p<q:
			count1+=1
		else:
			count+=1
			count1+=1
	if count>count1:
		print(0,count)
	elif count<count1:
		print(1,count1)
	else:
		print(2,count)

