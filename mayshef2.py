import sys
from collections import Counter
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	N,Q=map(int,input().split())
	s=input()
	dict=Counter(s)
	for _ in range(Q):
		ans=0
		c=int(input())
		print(dict)
		for i in dict.values():
			if i>c:
				ans+=i-c
		print(ans)
