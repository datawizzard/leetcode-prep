import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
    st=input()
    q=int(input())
    qi=list(map(int,input().split()))
    n=len(st)
    print(n)
    tracker=0
    # lastClose=-1
    ans=[-1]*n
    stack=[]
    for i in range(n-1,-1,-1):
        if st[i]==')':
            stack.append(i+1)
            print(stack)
            if i!=n-1:
                ans[i]=ans[i+1]
                print(ans)
            # lastClose=i+1
            tracker-=1
        elif tracker<0 and st[i]=='(':
            ans[i]=stack.pop()
            tracker+=1
    # print(ans)
    for i in range(q):
        print(ans[qi[i]-1])