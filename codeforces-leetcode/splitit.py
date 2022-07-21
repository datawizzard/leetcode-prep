import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	strin=input()
	if strin[-1] not in strin[:n-1]:
		print("NO")
	else:
		print("YES")