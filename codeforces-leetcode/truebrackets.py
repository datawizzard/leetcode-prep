import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	s=input()
	ans,a,b=0,0,0
	#l=stack()
	for i in s:
		if i=="(":
			a+=1
		if i=="[":
			b+=1
			#print(b,ans)
		if i==")" and a>0:
			ans+=1
			a-=1
			#print(a,ans)
		if i=="]" and b>0:
			ans+=1
			b-=1
			#print(b,ans)
	print(ans)
