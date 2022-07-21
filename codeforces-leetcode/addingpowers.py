for _ in range(int(input())):
    n,k=map(int,input().split())
    a=[int(i) for i in input().split()]
    b=[0]*100
    for v in a:
        i=0
        while v:
            b[i]+= v%k
            v//=k
            i+=1
    print("YES" if max(b)<=1 else "NO")