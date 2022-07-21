import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
from collections import*
input()
corona=0
a=Counter(map(int,input().split()))
p=[1<<i for i in range(31)]
for i in a:
	virus=True
	for j in p:
		if a.get(j-i):
			virus=False
			if j-i==i and a[j-i]==1:
				virus=True
			else:
				break;
	if virus:
		corona+=a[i]
print(corona)

