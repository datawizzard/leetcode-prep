import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	# stack=list()
	# max_area=0
	# index=0
	# while index<n:
	# 	if (len(stack)==0) or (arr[stack[-1]]<=arr[index]):
	# 		stack.append(index)
	# 		index+=1
	# 	else:
	# 		top_stack=stack.pop()
	# 		if stack:
	# 			area=arr[top_stack]*(index-stack[-1]-1)
	# 		else:
	# 			area=arr[top_stack]*index	
	# 	# print(area)
	# 	max_area=max(max_area,area)
	# while len(stack)!=0:
	# 	top_stack=stack.pop()
	# 	if stack:
	# 		area=arr[top_stack]*(index-stack[-1]-1)
	# 	else:
	# 		area=arr[top_stack]*index	
	# 	#print(area)
	# max_area=max(max_area,area)
	# print(max_area)
	stack = list() 
	max_area ,area= 0 ,0
	index = 0
	while index < len(arr): 
		if len(stack)==0 or (arr[stack[-1]] <= arr[index]): 
			stack.append(index) 
			index += 1 
		else: 
			top_of_stack = stack.pop() 
			if len(stack)!=0:
				area = arr[top_of_stack] *(index - stack[-1] - 1)
			else:
				area = arr[top_of_stack] *index 
			max_area = max(max_area, area) 
	while stack:
		top_of_stack = stack.pop()  
		if len(stack)!=0:
			area = arr[top_of_stack] *(index - stack[-1] - 1)
		else:
			area = arr[top_of_stack] *index 
		max_area = max(max_area, area) 
	print(max_area) 


