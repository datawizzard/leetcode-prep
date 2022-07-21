import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n1,n2=map(int,input().split())	
res=""
count=0
for p in range(n1,n2+1):
	for i in range(0,24):
		for j in range(0,60):
				for k in range(0,60):
					res=str(p)+str(i).zfill(2)+str(j).zfill(2)+str(k).zfill(2)
					ans = ''.join(reversed(res))
					if ans==res:
						count+=1
						print(ans)
print(count)

