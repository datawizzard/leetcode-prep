import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	if len(set(arr))==1:
		print("NO")
	else:
		print("YES")
		l=arr[-1]
		m=0
		for i in range(n-2,-1,-1):
			if arr[i]!=l:
				#print(i)
				print(n,i+1)
				m=i+1
		for i in range(n-2,-1,-1):
			if arr[i]==l:
				print(m,i+1)


