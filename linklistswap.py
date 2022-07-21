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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy=head
        while head:
            if head.next is None:
                return dummy
            curr=head.val
            temp=head.next.val
            head.val=temp
            head.next.val=curr
            head=head.next.next
        return dummy
            
        