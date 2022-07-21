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
from itertools import combinations
def printPowerSet(s,set_size): 
	pow_set_size = (int) (math.pow(2, set_size)); 
	counter = 0; 
	j = 0;
	a=[]
	for counter in range(0, pow_set_size): 
		for j in range(0, set_size):  
			if((counter & (1 << j)) > 0): 
				a.append(s[j])
	
		print()
n = II()
n=str(n)
printPowerSet(n,len(list(n)))

