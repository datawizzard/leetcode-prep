import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	ans, mn = 0, 99999999999
	n = int(input())
	a = list(map(int, input().split()))
	for i in a:
		mn = min(i, mn)
		ans+=mn
	print(ans)