import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	N=int(input())
	FUEL=list(map(int,input().split()))
	COST=list(map(int,input().split()))
	sortedindC=[i[0] for i in sorted(enumerate(COST), key=lambda i:i[1])]
	# print(sortedindC)
	# print(FUEL)
	dist=N
	ans=0
	for i in sortedindC:
		car=min(FUEL[i],dist)
		dist-=car
		ans+=car*COST[i]
		if dist==0:
			break
	print(ans)