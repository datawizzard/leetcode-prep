import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')

import bisect
def binarySearch (arr, l, r, m):  
    if r >= l: 
        mid = l + (r - l) // 2
        if arr[mid] == m: 
            return 1 
        elif arr[mid] > m: 
            return binarySearch(arr, l, mid-1, m) 
        else: 
            return binarySearch(arr, mid + 1, r, m) 
    else:  
        return -1
for _ in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()))
	q=int(input())
	for _ in range(q):
		x,y=map(int,input().split())
		k,l=0,0
		l=x+y
		if arr[0]>l:
			print(0)
		elif binarySearch(arr, 0, len(arr)-1, l)==1:
			print(-1)
		else:
			k=bisect.bisect(arr,l,0,len(arr))
			print(k)
