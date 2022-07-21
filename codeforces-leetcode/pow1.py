import sys

sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n=int(input())
arr=list(map(int,input().split()))
from collections import*
a=Counter(arr)
print(a)

