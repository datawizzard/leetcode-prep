import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# for _ in range(int(input())):
# 	s=input()
# 	n=len(s)
# 	if s[0]==')' or s[-1]=='(' or n%2==1:
# 		print("NO")
# 	else:
# 		print("YES")
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	m=int(input())
	arr1=list(map(int,input().split()))
	sum1,sum2,max1,max2=0,0,0,0
	for i in arr:
		sum1+=i
		max1=max(max1,sum1)
	for j in arr1:
		sum2+=j
		max2=max(max2,sum2)
	print(max1+max2)





