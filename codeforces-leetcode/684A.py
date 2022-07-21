import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
    n,c,b,a=map(int,input().split())
    s=input()
    x=s.count("0")
    y=s.count("1")
    l=x*min(a+b,c)+y*min(a+c,b)
    print(l)

			