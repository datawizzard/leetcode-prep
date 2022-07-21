import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# Brute Force: time complexity n^2 ,space complexity O(1)
 # Logic: Maximum unit of water which will be hold by any particular
 #  		building will be min(max of building height of all height to the left
 #  		and maximum of all building  height to the right of any particular 
 #  		building height)-height of that building
for _ in range(int(input())):
	n=int(input())
	height=list(map(int,input().split()))
	s=0
	n=len(height)
	for i in range(1,n-1):
	    s+=min(max(height[:i+1]),max(height[i:]))-height[i]
	print(s)






 # 2nd approach : time complexity n, space complexity O(n)
for _ in range(int(input())):
	n=int(input())
	height=list(map(int,input().split()))
	prefix=[-1]*n
	prefix[0]=height[0]
	# Prefix sum store the maximum element till visited in an array
	for i in range(1,n):
		prefix[i]=max(height[i],prefix[i-1])
	# print(prefix)
	suffix=[-1]*n
	suffix[n-1]=height[-1]
	for i in range(n-2,-1,-1):
		suffix[i]=max(suffix[i+1],height[i])
	# print(suffix)
	s=0
	for i in range(n):
		s+=min(prefix[i],suffix[i])-height[i]
	print(s)






# Stack Approach
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	stack=list()
	ans=0
	for i in range(n):
		while(len(stack)!=0 and arr[stack[-1]]<arr[i]):
			pop_height=arr[stack[-1]]
			#print(pop_height,stack)
			stack.pop()
			#print(pop_height,stack)
			if len(stack)==0:
				break;
			distance=i-stack[-1]-1
			#print(distance)
			min_height=min(arr[stack[-1]],arr[i])-pop_height
			#print(min_height)
			ans+=distance*min_height
			#print(ans)
		stack.append(i)
		#print(stack)
		#print("Next Iter")
	print(ans)


# Two pointer
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	i,j,lmax,rmax,ans=1,n-2,arr[0],arr[-1],0
	while(i<=j):
		if arr[i]>lmax:
			lmax=arr[i]
		if  arr[j]> rmax:
			rmax=arr[j]
		if lmax<=rmax:
			ans += lmax-arr[i]
			print(lmax,rmax,ans)
			i+=1
		else:
			ans += rmax-arr[j]
			j-=1
	print(ans)
