import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
    n,m,x,y=map(int,input().split())
    ans=0
    if(n*m==1):
        ans=x
    elif(x*2<=y):
        ans=n*m*x   
    elif(y>=x):
        if((n*m)%2==0):
            ans=((n*m)//2)*y
        else:
            ans=((n*m)//2)*y + x
    else:
        ans=((n*m+1)//2)*y
    print(ans)
                    