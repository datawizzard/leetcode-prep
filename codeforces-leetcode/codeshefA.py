import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	s=input()
	count=0
	for i in s:
		if i=='1':
			count+=1
	if ((120-n+count)/120)*100>=75:
		# print((120-n+count)/120)
		print("YES")
	else:
		print("NO")