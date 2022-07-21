import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
def SieveOfEratosthenes(n):
		a=[]            
		prime = [True for i in range(n+1)] 
		p = 2
		while (p * p <= n): 
		    if (prime[p] == True): 
		        for i in range(p * p, n+1, p): 
		            prime[i] = False
		    p += 1
		for i in range(1,n+1):
			if prime[i]:
				a.append(i)
		return prime,a
p , a= SieveOfEratosthenes(int(100000))
# print(p)
# print(a)
for _ in range(int(input())):
    d = int(input())
    x1 = 1
    for i in range(1,len(a)):
        if a[i] > d:
            x2 = a[i]
            break
    # print(x2)
    for i in range(1,len(a)):
        if a[i]-x2 >= d:
            x3 = a[i]
            break
    print(x2*x3)


        
        
        
        
        
        
    
    
   
