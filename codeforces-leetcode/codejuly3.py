import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	k=int(input())
	arr=[]
	arr='O'+(k-1)*'.'+(64-k)*'X'
	j,q=0,8
	for i in range(8):
		while j<q:
			print(arr[j],end="")
			j+=1
		q+=8
		print()

