import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
    a,b = map(int,input().split())
    s=input()
    count,ans,ln=9999999999999,0,len(s)
    for i in range(ln):
        if s[i] == "0":
        	count+=1
        else:
        	ans+=min(a,b*count)
        	count=0
        	print(ans,end=" ")
    print(ans)