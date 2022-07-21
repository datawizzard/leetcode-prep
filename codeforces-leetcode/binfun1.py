import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
    n = int(input())
    a=list(map(int,input().split()))
    ans = 0
    for i in range(n):
        b1 = bin(a[i]).replace("0b","")
        for j in range(i,n):
            b2 = bin(a[j]).replace("0b","")
            a1 = int(b1+b2,2)
            a2 = int(b2+b1,2)
            ans = max(ans,abs(a2-a1))
    print(ans)