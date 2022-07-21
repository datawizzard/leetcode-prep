import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,K,x,y=map(int,input().split())
	if K%4==0:
		K=4
	else:
		K=K%4
	a=[]
	if x==y:
		print(n,n)
	elif x>y:
		# print(K)
		a.append([n,n-x+y])
		a.append([n-x+y,n])
		a.append([0,x-y])
		a.append([x-y,0])
		print(a)
		if K==1:
			print(*a[0])
		elif K==2:
			print(*a[1])
		elif K==3:
			print(*a[2])
		elif K==4:
			print(*a[3])
	else:
		a.append([n-y+x,n])
		a.append([n,n-y+x])
		a.append([y-x,0])
		a.append([0,y-x])
		print(a)
		if K==1:
			print(*a[0])
		elif K==2:
			print(*a[1])
		elif K==3:
			print(*a[2])
		elif K==4:
			print(*a[3])


