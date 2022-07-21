import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def widegap(n,start,finish):
	l=0
	finlen=l
	gap=[False]*(n+1)
	for i in range(len(start)):
		for j in range(start[i]-1,finish[i]):
			gap[j]=True
	for i in range(n+1):
		if gap[i]==False:
			l+=1
			finlen=max(l,finlen)
		else:
			if gap[i]==True:
				l=0
	return finlen
n=int(input())
start=list(map(int,input().split()))
finish=list(map(int,input().split()))
print(widegap(n,start,finish))
