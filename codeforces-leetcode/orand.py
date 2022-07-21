import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# Logic behind code:
 # We use two datastructure here one for storing unique element i.e set
 # and other of storing every new element so that we can do OR , AND opeartion
 # to every new element store in the array with the whole array.
 # Every poping element is new element and we are doing OR , AND with
 # each of them with each element of array.
 # After list is empty it means all possible element are found
 # and the size of the set gives the required ans
# for _ in range(int(input())):
# 	n,m=map(int,input().split())
# 	a=list(map(int,input().split()))
# 	b=list(map(int,input().split()))
# 	s=set()
# 	queue=[]
# 	queue.append(0)
# 	while len(queue)!=0:
# 		x=queue[-1]
# 		l=queue.pop()
# 		# print(l)
# 		for i in range(n):
# 			y=a[i]
# 			if x|y not in s:
# 				s.add(x|y)
# 				queue.append(x|y)
# 				# print(s,"array1")
# 				# print(queue,"array1.1")
# 		for i in range(m):
# 			z=b[i]
# 			if x&z not in s:
# 				s.add(x&z)
# 				queue.append(x&z)
# 				# print(s)
# 				# print(queue)
# 	# print(s)
# 	print(len(s))

from queue import LifoQueue
def orand(a,b,n,m):
	stack = LifoQueue()
	stack.put(0)
	s=set()
	while stack.empty()==False:
		x=stack.get()
		for i in range(n):
			if a[i]|x not in s:
				s.add(a[i]|x)
				stack.put(a[i]|x)
		for i in range(m):
			if x&b[i] not in s:
				s.add(x&b[i])
				stack.put(x&b[i])
	print(s)
	return len(s)
for _ in range(int(input())):
	n,m=map(int,input().split())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	print(orand(a,b,n,m))