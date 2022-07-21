import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
    k,d0,d1 = map(int,input().split())
    d2 = (d0+d1)%10
    s = d0 + d1


    if k == 2:
        s = d0+d1
        req_no = s
    elif k == 3:
        req_no = s +( s%10)
        
    else:
        #print(req_no)
        
        t = (k-3)//4
        l = (k-3)%4
        t_sum = ((2*s)%10 )+ ((4*s)%10 )+ ((8*s)%10) + ((6*s)%10)
        #print(t_sum,t)

        req_no = t_sum*t + (s+(s%10))
        #print(req_no)
        if l == 1:
            req_no += (2*s)%10
        elif l == 2:
            req_no += ((2*s)%10 + ((4*s)%10))
        elif l == 3:
            req_no += ((2*s)%10 + ((4*s)%10)+ ((8*s)%10))

        

        
    #print(req_no)
    if req_no%3 == 0:
        print('YES')
    else:
        print('NO')


