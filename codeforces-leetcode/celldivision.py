import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for u in range(int(input())):
	n = int(input())
	y = []
	while(n > 2):
	    i = n-1
	    while((i-1)**2 >= n):
	        y.append([i, n])
	        i -= 1
	        
	    y.append([n, i])
	    y.append([n, i])
	    n = i
	print(y)    
	print(len(y))
	for i in y:
	    print(*i)



