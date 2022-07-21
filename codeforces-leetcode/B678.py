import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	if n%2==0:
		for i in range(n):
			for j in range(n):
				if i==j or (i+j)==(n-1):
					print(1,end=" ")
				else:
					print(0,end=" ")
			print()
	else:
		for i in range(n):
			for j in range(n):
				if i==j or (i+j)==(n-1) or (i==n//2 and j==n//2+1) or (i==n//2-1and j==n//2):
					print(1,end=" ")
				else:
					print(0,end=" ")
			print()


