import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):

    k = int(input())
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    n = int(input())
    t = [[0]*(k) for i in range(k)]
    c.reverse()
    t[k-1] = c
    pr = int(1e9)

    for i  in range(k-1):
        t[i][i+1] = 1

    #print(t)

    def mat_pro(a1,a2):
        b = [[0]*(k)for i in range(k)]
        for i in range(k):
            for j in range(k):
                for p in range(k):
                    b[i][j] += (a1[i][p]*a2[p][j])

                    b[i][j] %= pr



        return b

    def powerMod(x,y):
        res = [[0]*k for i in range(k)]
        for i in range(k):
            res[i][i] = 1
        print(res)
        
        while y > 0:
            if y&1:
                res = mat_pro(res,x)
                print(res)
            y = y>>1
            x = mat_pro(x,x)
            #print(x)
        return res


    r = powerMod(t,n-1)
    print(r)
    ans = 0
    for i in range(k):
        ans += (r[0][i]*b[i])
    print(ans%pr)
