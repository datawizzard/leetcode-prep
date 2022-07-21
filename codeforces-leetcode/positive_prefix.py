import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,k=map(int,input().split())
	sum1,count=0,0
	if n%2==0:
		a=[i if i%2==0 else -i for i in range(1,n+1)]
		#print(a,"arr")
	else:
		a=[i if i%2==1 else -i for i in range(1,n+1)]
		#print(a,"hg")
	for i in a:
		sum1+=i
		if sum1>0:
			count+=1
	# print(count)
	if count==k:
		print(*a)
		# sum1=0
		# c=0
		# for i in a:
		# 	sum1+=i
		# 	if sum1>0:
		# 		c+=1
		# print(c,sum1)
	if count>k:
		for i in range(n-1,-1,-1):
			if a[i]>0:
				a[i]=-(i+1)
				count-=1
			if count==k:
				break;
		print(*a)
		# c=0
		# sum1=00
		# for i in a:
		# 	sum1+=i
		# 	if sum1>0:
		# 		c+=1
		# print(c,sum1)
	if count<k:
		for i in range(n-1,-1,-1):
			if a[i]<0:
				a[i]=i+1
				count+=1
			if count==k:
				break;
		print(*a)
		# c=0
		# sum1=0
		# for i in a:
		# 	sum1+=i
		# 	if sum1>0:
		# 		c+=1
		# print(c,sum1)



