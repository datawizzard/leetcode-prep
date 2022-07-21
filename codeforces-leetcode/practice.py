import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for i in range(int(input())):
    n=[a for a in input()]
    if len(n)%2!=0:
        n.remove(n[len(n)//2])
    a=n[0:len(n)//2]
    b=n[len(n)//2:]
    a.sort()
    b.sort()
    if a==b:
        print("YES")
    else:
        print("NO")