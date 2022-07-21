import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
def equalsum(arr,n,total):
	dp=[[0 for j in range(total+1)] for i in range(n+1)]	
	for i in range(n+1):
		for j in range(total + 1):
			if i==0 and j==0:
				dp[i][j]=1
			elif j==0:
				dp[i][j]=1
			elif i==0:
				dp[i][j]=0
	for i in range(1,n+1):
		for j in range(1,total + 1):
			if arr[i-1]>j:
				dp[i][j]=dp[i-1][j]
			else:
				dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
	return dp[n][total]	
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
		if s>k:
			return count
		else:
			return -1
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
			if sum(arr1)==2*k:
				if equalsum(arr1,len(arr1),sum(arr1)//2):
					return len(arr1)
				else:
					arr1.append(arr[p+1])
					if equalsum(arr1,len(arr1),sum(arr1)):
						return len(arr1)
			if equalsum(arr1,len(arr1),k):
				return len(arr1)
			else:
				if equalsum(arr1,len(arr1),k//2):
					return len(arr1)
				temp=[]
				for i in arr1:
					temp.append(i)
				newlistA=[arr1[0]]
				arr1.remove(arr1[0])
				for i in range(len(arr1)-1,0,-1):
					if sum(newlistA)<k:
						newlistA.append(arr1[i])
						arr1.remove(arr1[i])
				newlistB=arr1
				if sum(newlistB)>=k:
					return len(newlistA)+len(newlistB)
				else:
					for i in range(p+1,n):
						arr1=temp
						newlistA=[]
						newlistB=[]
						temp.append(arr[i])
						if equalsum(temp,len(temp),k):
							return len(temp)
						else:
							newlistA=[temp[0]]
							arr1.remove(temp[0])
							for i in range(len(temp)-1,0,-1):
								if sum(newlistA)<k:
									newlistA.append(temp[i])
									arr1.remove(temp[i])
							newlistB=arr1
							if sum(newlistB)>=k:
								return len(newlistA)+len(newlistB)

for _ in range(int(input())):
	n,k=map(int,input().split())
	arr=list(map(int,input().split()))
	arr.sort(reverse=True)
	print(watchingcpl(arr,k,n))
	