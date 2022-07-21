import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	s=input()
	n=len(s)
	count,c=0,0
	vis=[False]*(n)
	for i in range(1,len(s)):
		vis_n=False
		if s[i]==s[i-1] and vis[i-1]==False:
			vis_n=True
			c=1
		if i>=2 and s[i]==s[i-2] and vis[i-2]==False:
			vis_n=True
			c=1
		elif vis_n==False:
			c=0
		vis[i]=vis_n
		# print(vis_n,c)
		count+=c
	print(count)

#Method 2

t=int(input())
for _ in range(t):
    s=list(input())
    c=0
    for i in range(1,len(s)):
        if i>=2 and s[i]==s[i-2] or s[i]==s[i-1]:
            c+=1
            s[i]='A'
    print(c)
		


