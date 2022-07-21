import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	res = set() 
	pre = {0} 
	for x in arr: 
		pre = {x | y for y in pre} | {x} 
		res |= pre 
	if len(res)==(n*(n+1)//2):
		print("YES")
	else:
		print("NO")
