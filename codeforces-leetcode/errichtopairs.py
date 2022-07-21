import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	is_b=[False]*(2*n+1)
	ans=n+1
	for k in range(n):
		is_b[arr[k]]=True
	is_b=is_b[1:]
	print(is_b)
	for i in range(2):
		bal=0
		lower=0
		for j in range(0,2*n):
			if is_b[j]:
				bal+=1
			else:
				bal-=1
			lower=max(lower,bal)
			print(lower,bal)
		ans-=lower
		is_b=is_b[::-1]
	print(ans)