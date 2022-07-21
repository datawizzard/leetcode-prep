import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n,p=map(int,input().split())
arr=list(map(int,input().split()))
a=arr[:p]
b=arr[p:]
a.sort()
b.sort(reverse=True)
print(a+b)


