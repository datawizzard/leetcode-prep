import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	N,M=map(int,input().split())
	arr=list(map(int,input().split()))
	res = [(input().split())
		for i in range(M)]
	print(res)
	arrpos = [*enumerate(arr)] 
	print(arrpos)
	for i in range(len(arrpos)-1):
		for j in range(i,len(arrpos)):
			if (i[0]+1,j[0]+1) in res and i[1]>j[1]:
				temp=i[1]
				i[1]=j[1]
				j[1]=temp

  
  

	brr=[0]*N
	N = len(brr) 
	
	arrpos.sort(key = lambda it:it[1]) 
	res=[0]


