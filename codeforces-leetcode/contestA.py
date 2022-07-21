import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

for _ in range(int(input())):
    a,k=map(int,input().split())
    if a>=k:
        print((a-k)%2)
    else:
        print(k-a)