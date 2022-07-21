import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for i in range(int(input())):
    r,g,b,w = map(int, input().split())
    s = r%2+g%2+b%2+w%2
    print('No' if s == 2 or s>2 and r*g*b == 0 else 'Yes')