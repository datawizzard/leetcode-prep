import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# Difference between bounded and unbounded knapsack
	# In knapsack we can use choose items for only one time either it
	# will selected or not but in unbounded knapsack we can choose 
	# as required i.e more than once also.It can be processed more than once
	# even if we have used it earlier.


# Unbounded knapsack is only rod cutting problem.
# In rod cutting problem we have maximize the price
# by cutting rod optimally .We have N element in array and 
# corresponding to each length of rod the price is given .We
# have to cut the rod according to it and maximize the price
# So we use rod of same length to maximize the price 
# thats why we use unbounded knapsack
def knapsack(weight,price,w,n):
	#base case
	if n==0 or w==0:
		return 0;
	if a[n][w]!=-1:
		return a[n][w];
	# the only difference is we dont have decrease n as we have done in 
	# knapsack as we can process same element again which is not possible 
	# in knapsack.
	if weight[n-1]<=w:
		a[n][w]=max(price[n-1]+knapsack(weight,price,w-weight[n-1],n),
			knapsack(weight,price,w,n-1))
		return a[n][w];
	# if weight is greater than knapsack capacity we move to next
	# element without adding that element in knapsack.
	elif weight[n-1]>w:
		a[n][w]=knapsack(weight,price,w,n-1)
		return a[n][w]
n,w=map(int,input().split())
a=[[-1 for j in range(w+1)]for i in range(n+1)]
# print(a[0])
weight=list(map(int,input().split()))
price=list(map(int,input().split()))
print(knapsack(weight,price,w,n))

# Dynamic Approach
def knapsack(weigh,price,w,n):
	for i in range(n+1):
		for j in range(w+1):
			# if there are 0 item present or it knapsack capacity is 0
			if i==0 or j==0:
				a[i][j]=0
			# if last item weight is less than knapsack capacity.
			# we have two option either store it in knapsack or ignore it 
			# and move to next item.
			elif weight[i-1]<=j:
				a[i][j]=max(price[i-1]+a[i][j-weight[i-1]],a[i-1][j])
			else:
				a[i][j]=a[i-1][j]
	for i in range(n+1):
		for j in range(w+1):
			print(a[i][j],end=" ")
		print()
	return a[i][j]

n,w=map(int,input().split())
a=[[0 for j in range(w+1)]for i in range(n+1)]
# print(a[0])
weight=list(map(int,input().split()))
price=list(map(int,input().split()))
print(knapsack(weight,price,w,n))
