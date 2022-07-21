import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	w,h,n=map(int,input().split())
	c=1
	while w%2==0:
		c=c*2
		w=w//2
	while h%2==0:
		c=c*2
		h=h//2
	if c>=n:
		print("YES")
	else:
		print("NO")

