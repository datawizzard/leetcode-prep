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
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1,m):
        	# Case 1:
        	# First substring is compared with last part of second substring
        	# i,e s1[:i] to s2[n-i:] and after s1[i:] is compared with first part second
        	# substring i.e s2[:n-i]
            if (self.isScramble(s1[:i],s2[n-i:]) and self.isScramble(s1[i:],s2[:n-i])):
            	return True
            # Case 2:
            # All substring is compared correspondingly i.e s1[:i] and s2[:i] and
            # s1[i:] and s2[i:]
            if (self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:])):
                return True 
        return False
