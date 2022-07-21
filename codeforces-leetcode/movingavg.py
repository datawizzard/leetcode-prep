import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
X,Y= map(int,input().split())
N=int(input())
arr=list(map(float,input().split()))
avg2=[None]*(N-X+1)
avg4=[None]*(N-Y+1)
for i in range(0,N-X+1):
	avg2[i]=sum(arr[i:i+X])/X
print(avg2)
for i in range(0,N-Y+1):
	avg4[i]=sum(arr[i:i+Y])/Y




