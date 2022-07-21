import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n = int(input())
	s=input()
# 	s=sum(arr)
# 	if s<k:
# 		print(0)
# 	elif s//k<=d:
# 		print(s//k)
# 	else:
# 		print(d)
	arr=['a',"b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
	b=arr
	r=""
	count=0
	for i in range(0,n,4):
		arr=b
		for j in s[i:4+i]:
			if j=='0':
				arr=arr[:len(arr)//2]
			else:
				arr=arr[len(arr)//2:]
		r+=str(*arr)
	print(str(r))


