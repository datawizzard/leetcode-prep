import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log, ceil
from collections import defaultdict as dd
from collections import Counter as cc
from bisect import bisect_left as bl
from bisect import bisect_right as br
import functools
INF = float('inf')
MOD = 998244353
mod = 10**9+7
sys.setrecursionlimit(100000000)
def inp(): return sys.stdin.readline()
def out(var):     sys.stdout.write(str(var) + "\n")  
def I():    return (inp())
def II():    return (int(inp()))
def FI():    return (float(inp()))
def SI():    return (list(str(inp())))
def MI():    return (map(int,inp().split()))
def LI():    return (list(MI()))
def SLI():    return (sorted(LI()))
def MF():    return (map(float,inp().split()))
def LF():    return (list(MF()))
def SLF():    return (sorted(LF()))
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # l1 = l1
        # l2 = l2
        currentCarry = 0
        head = cur = ListNode(0)
        while l1 or l2 or currentCarry:
            currentVal = currentCarry
            currentVal += 0 if l1 is None else l1.val
            currentVal += 0 if l2 is None else l2.val
            if currentVal >= 10:
                currentVal -= 10
                currentCarry = 1
            else:
                currentCarry = 0
            # print(currentVal, currentCarry)
            cur.next = ListNode(currentVal)
            cur = cur.next
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                l2 = l2.next
            elif l2 is None:
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next
        return head.next
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		temp1=head
		temp2=head
		length=1
		# while temp2.next:
		# 	temp2=temp2.next
		# 	length+=1

		# if length==n: #crucial step
		# 	return head.next

		# for i in range(length-n-1):
		# 	temp1=temp1.next
		# 	print(temp1.val)

		# temp1.next=temp1.next.next

		# return head
		for i in range(n):
			temp2=temp2.next
		if temp2 is None:
			return head.next
		while temp2.next:
			temp1=temp1.next
			temp2=temp2.next
        
		temp1.next=temp1.next.next
    
		return head
def linked_list_str(l):
    if l is None:
        return ''
    return str(l.val) + '->' + linked_list_str(l.next)

print

# Make first linked list.
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
print(linked_list_str(l1))

# Add linked lists.
s = Solution()
l3 = s.removeNthFromEnd(l1,5)
print(linked_list_str(l3))
