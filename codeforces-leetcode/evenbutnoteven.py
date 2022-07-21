import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	ig=int(input())
	ans,pg=0,0
	ans=ig
	pg=ig
	c=0
	while(pg>0):
		if (pg%10)%2==1:
			c+=1
		pg=pg//10
	if c%2==0 and ig%2==1:
		print(ig)
	else:
		while(ig>0):
			rem=(ig%10)
			if rem%2==1:
				res = [int(x) for x in str(ig)]
				res.remove(rem)
				break
			ig=int("".join(map(str,res)))
			ig=ig//10
		if ig>0:
			print(ig)
		else:
			print(-1)



