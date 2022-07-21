import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def equalsum(arr,n,sum1):
	a=[[False for j in range(sum1+1)] for i in range(n+1)]	
	for i in range(n+1):
		for j in range(sum1 + 1):
			if i==0 and j==0:
				a[i][j]=True
			elif j==0:
				a[i][j]=True
			elif i==0:
				a[i][j]=False
	for i in range(1,n+1):
		for j in range(1,sum1 + 1):
			if arr[i-1]>j:
				a[i][j]=a[i-1][j]
			else:
				a[i][j]=a[i-1][j] or a[i-1][j-arr[i-1]]
	return a[n][sum1]	
def watchingcpl(arr,k,n):
	count=0
	if sum(arr)<2*k:
		return -1
	if arr[0]>=k:
		count=1
		i,s=1,0
		while i<n and s<k:
			count+=1
			s+=arr[i]
			i+=1
		return count if s>k else -1
	elif arr[0]<k:
		if sum(arr)==2*k:
			if equalsum(arr,n,sum(arr)//2):
				return len(arr)
			else:
				return -1
		if sum(arr)>2*k:
			s,count=0,0
			arr1=[]
			for i in range(n):
				if s<2*k:
					s+=arr[i]
					arr1.append(arr[i])
					p=i
					count+=1
			# print(arr1,s)
			if sum(arr1)==2*k:
				if equalsum(arr1,len(arr1),sum(arr1)//2):
					return len(arr1)
				else:
					arr1.append(arr[p+1])
					if equalsum(arr1,len(arr1),sum(arr1)):
						return len(arr1)
			# print(arr1)
			if equalsum(arr1,len(arr1),k):
				return len(arr1)
			else:
				if equalsum(arr1,len(arr1),k//2):
					return len(arr1)
				b=[]
				for i in arr1:
					b.append(i)
				list1=[arr1[0]]
			# print(list1)
				arr1.remove(arr1[0])
				for i in range(len(arr1)-1,0,-1):
					if sum(list1)<k:
						list1.append(arr1[i])
						arr1.remove(arr1[i])
				list2=arr1
				if sum(list2)>=k:
					return len(list1)+len(list2)
				else:
					for i in range(p+1,n):
						arr1=b
						list1=[]
						list2=[]
						b.append(arr[i])
						if equalsum(b,len(b),k):
							return len(b)
						else:
							list1=[b[0]]
							arr1.remove(b[0])
							for i in range(len(b)-1,0,-1):
								if sum(list1)<k:
									list1.append(b[i])
									arr1.remove(b[i])
							list2=arr1
							if sum(list2)>=k:
								return len(list1)+len(list2)

for _ in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	arr.sort(reverse=True)
	print(watchingcpl(arr,k,n))
	