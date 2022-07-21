import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
n=int(input())
b,h=map(int,input().split())
arr=list(map(int,input().split()))
mod=pow(10,9)+7
sum1=0
for i in range(n):
	sum1=sum1+arr[i]
r,ans=0,0
stack=[]
for i in range(n):
	while len(stack)!=0 and arr[i]<=arr[stack[-1]]:
		top=stack[-1]
		stack.pop()
		if len(stack)==0:
			r=arr[top]*i
		else:
			r=arr[top]*(i-stack[-1]-1)
		ans=max(ans%mod,r)
	stack.append(i)
while(len(stack)!=0):
	top=stack[-1]
	stack.pop()
	if len(stack)==0:
		r=arr[top]*n
	else:
		r=arr[top]*(n-stack[-1]-1)
	ans=max(ans%mod,r)
print(((sum1%mod-ans%mod)%mod*b%mod*h%mod)%mod)
