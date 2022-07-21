import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	arr.sort(reverse=True)
	print(arr)
	sum1=0
	w=n//2
	for i in range(k):
		sum1+=arr[w]
		w+=(n//2)+1
	print(sum1)

		

