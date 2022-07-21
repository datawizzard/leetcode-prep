import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,k=map(int,input().split())
	s=input()
	ans=0
	i,j,c=0,0,0
	if n==1:
		print(ans)
	else:
		while i<n and j<n:
			if s[i]=='M':
				if s[j]=='I':
					z=max(i,j)
					r=min(i,j)
					for l in range(r,z):
						if s[l]==":":
							c+=1
					P=k+1-abs((j-i))-c
					if P>0:
						ans+=1
						i+=1
						j+=1
						c=0
					elif P<=0:
						if i>j:
							j+=1
						else:
							i+=1
						c=0
				elif s[j]=='X':
					i=j
					i+=1
					j+=1
					c=0
				else:
					j+=1
			elif s[i]=='X':
				j=i
				i+=1
				j+=1
				c=0
			else:
				i+=1
		print(ans)
	
