import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import math
from itertools import combinations
def decBinary(arr, n): 
    k = int(math.log2(n))  
    while (n > 0): 
        arr[k] = n % 2
        k = k - 1
        n = n//2 
def binaryDec(arr, n): 
    ans = 0
    for i in range(0, n): 
        ans = ans + (arr[i]<<(n-i-1)) 
    return ans  
def concat(m, n):  
    k = int(math.log2(m))+1
    l = int(math.log2(n))+1
    a = [0 for i in range(0, k)] 
    b = [0 for i in range(0, l)]   
    c = [0 for i in range(0, k + l)] 
    decBinary(a, m)
    decBinary(b, n)  
    index = 0
    for i in range(0, k):  
        c[index] = a[i] 
        index = index+1
    for i in range(0, l):  
        c[index] = b[i] 
        index = index + 1
    return (binaryDec(c,k+l))
for _ in range(int(input())):
	n=int(input())
	arr1=list(map(int,input().split()))
	max1=-9999999999
	if n==1:
		print(0)
	else:
		v=[[] for i in range(len(arr1))]
		v=list(combinations(arr1,2))
		for x,y in v:
			max1=max(max1,concat(x,y)-concat(y,x))
		print(max1)
	