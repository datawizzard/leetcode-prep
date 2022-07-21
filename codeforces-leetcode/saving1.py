import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	a,b = map(int,input().split())
	l = input().strip("0").split("1")
	print(l)
	print(len(l))
	if len(l)==1:
		ans = 0
	else:
		ans=a
	for i in l:
		if i != "":
			if len(i)*b <= a:
				ans+=(len(i)*b)
			else:
				ans+=a
	print(ans)