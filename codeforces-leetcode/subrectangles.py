import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n,m,k = map(int,input().split())
a = list(map(len,input().replace(" ","").split("0")))
print(a)
b = list(map(len,input().replace(" ","").split("0")))
p = [(i,k//i) for i in range(1,int(k**0.5)+1) if (k%i==0)]
print(p)
p += [(j,i) for i,j in p if (i!=j)]
print(p)
ans = 0
for i,j in p:
    A = 0
    B = 0
    for l in a:
        if (i<=l):
            A += l-i+1
    for l in b:
        if (j<=l):
            B += l-j+1
    ans += A*B
print(ans)