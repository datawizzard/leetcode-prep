import sys
from itertools import combinations 
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

for _ in range(int(input())):
	d=int(input())
	print(2*d)
	print(d*"a"+d*"b")