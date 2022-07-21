import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
for _ in range(int(input())):
	s=input()
	open_list = ["[","{","("] 
	close_list = ["]","}",")"] 
	stack = [] 
	for i in s: 
	    if i in open_list: 
	        stack.append(i) 
	    elif i in close_list: 
	        pos = close_list.index(i) 
	        if ((len(stack) > 0) and
	            (open_list[pos] == stack[len(stack)-1])): 
	            stack.pop()
	if len(stack)==0:
		print("Balanced")
	else:
		print("Unbalanced")
