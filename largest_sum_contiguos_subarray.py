import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

# Kadance Algorithm
# find largest sum continous subarray
# kadance algorithm doesn't work for all -ve number so i have optimzed it
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
 	currmax=arr[0]
 	maxsofar=arr[0]
 	for i in range(1,n):
 		currmax=max(arr[i],currmax+arr[i])
 		maxsofar=max(maxsofar,currmax)
 		print(currmax,maxsofar)
 	print(maxsofar)

 	# method 2
	maxSub, curSum = arr[0], 0   
	for n in arr:
	    if curSum < 0:
	        curSum = 0
	    curSum += n
	    maxSub = max(maxSub, curSum)
	print(maxSub)

	# Method 3
	maxcurr=0
	maxsofar=arr[0]
	for i in range(len(arr)):
	    maxcurr+=arr[i]
	    if maxsofar<maxcurr:
	        maxsofar=maxcurr
	    if maxcurr<0:
	        maxcurr=0
	print(maxsofar)

