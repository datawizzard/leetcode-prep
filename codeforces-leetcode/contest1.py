import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
arr=list(map(int,input().split()))
arr.sort()
print(arr)
