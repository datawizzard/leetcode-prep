import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
T = int(input())
for test_no in range(T):
	n, s, k = map(int, input().split())
	a = list(map(int, input().split()))

	for i in range(0, k+1):
		if s-i >= 1 and not s-i in a: 
			print(i); break
		if s+i <= n and not s+i in a:
			print(i); break
	else: assert(False)