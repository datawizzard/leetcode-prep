import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# Recursive Approach

def knapsack(weight,price,w,n):
	#base case
	if n==0 or w==0:
		return 0;
	#if weight of last item is less than w and if we include it
	# knapsack then price will be max of that remaining n-1 element
	# and current element n
	if weight[n-1]<=w:
		return max(price[n-1]+knapsack(weight,price,w-weight[n-1],n-1),
			knapsack(weight,price,w,n-1))
	# if weight is greater than knapsack capacity we move to next
	# element without adding that element in knapsack.
	elif weight[n-1]>w:
		return knapsack(weight,price,w,n-1)

# # Memoization

# # The purpose of lookup table is to store the previously calculatd value
# # and when there is need for it we can directly accesss the lookup table.
# # This is decrese the time complexity of the table.
def knapsack(weight,price,w,n):
	#base case
	if n==0 or w==0:
		return 0;
	if a[n][w]!=-1:
		return a[n][w];
	#if weight of last item is less than w and if we include it
	# knapsack then price will be max of that remaining n-1 element
	# and current element item n
	# if last item weight is less than knapsack capacity.
	# we have two option either store it in knapsack or ignore it 
	# and move to next item.
	# if we choose that item we move to next item and capacity of knapsack
	# will decrease by w-weight of nth item
	if weight[n-1]<=w:
		a[n][w]=max(price[n-1]+knapsack(weight,price,w-weight[n-1],n-1),
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
				a[i][j]=max(price[i-1]+a[i-1][j-weight[i-1]],a[i-1][j])
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


