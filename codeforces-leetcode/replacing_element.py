import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n,x=map(int,input().split())
	arr=list(map(int,input().split()))
	arr.sort()
	if all(i<=x for i in arr):
		print("YES")
		continue;
	elif arr[0]+arr[1]<=x:
		print("YES")
	else:
		print("NO")
		
