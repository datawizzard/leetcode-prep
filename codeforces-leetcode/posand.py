import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def isPowerOfTwo(l):
	while (l != 1):
			if (l % 2 != 0):
				return False
			l = l // 2		
	return True
for _ in range(int(input())):
	n=int(input())
	arr1=[2,3,1]
	for i in range(4,n+1):
		arr1.append(i)
	print(arr1)
	if n==1:
		print(1)
	elif isPowerOfTwo(n)==True:
		print(-1)
	elif n>=3:
		flag=0
		for i in range(3,n-1):
			if isPowerOfTwo(arr1[i])==True and i-flag>1:
				arr1[i],arr1[i+1]=arr1[i+1],arr1[i]
				flag=i
		print(*arr1)



