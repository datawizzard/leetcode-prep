import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(k):
        a[i::k] = sorted(a[i::k])
        print(sorted(a[i::k]))
        print(a)
    if a == sorted(a):
        print("yes")
    else:
        print("no")
