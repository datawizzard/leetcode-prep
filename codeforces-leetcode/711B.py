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
for _ in range(II()):
	n,W = MI()
	w = LI()
	count = [0]*20
	for i in w:
		count[int(math.log2(i))] += 1
	# print(count)
	space = W
	height = 1
	for i in range(n):
		largest = - 1
		for size in range(19,-1,-1):
			if count[size] > 0 and 2**size <= space:
				largest = size
				break;
		if largest == -1:
			space = W
			height += 1
			for size in range(19,-1,-1):
				if count[size] > 0 and 2**size <= space:
					largest = size
					break;
		count[largest] -= 1
		space -= 2 ** largest
	print(height)



		


