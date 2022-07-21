import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
    n = int(input())
    s = input()
    a,b = 0,0
    for i in s:
        if i == 'A':
            a +=1
        else:
            b += 1
    if abs(a-b) == 1:
        ans = 'Y'
    else:
        ans = 'N'          
    print("Case #%s: %s" % (_+1,ans ))