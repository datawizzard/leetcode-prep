import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
#Find the number from list which frequency is odd in 0(n) complexity
from functools import reduce
n=int(input())
arr=list(map(int,input().split()))
print(reduce(lambda a,b:a ^ b,arr))

