import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
i = lambda: map(int, input().split())
for _ in range(int(input())):
    n, w = i()
    a = list(i())
    a = sorted(list(zip(a, range(1, n+1))), reverse=True)
    b = []
    c = 0
    for x in a:
        if  c + x[0] <= w: 
            c += x[0]
            b.append(x[1])
    if c >= (w+1) // 2:
        print(len(b))
        print(*b)
    else:
    	print('-1')