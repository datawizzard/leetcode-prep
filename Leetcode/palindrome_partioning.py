import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import sys
import math
import heapq
def input(): return sys.stdin.readline().strip("\n")
def I():    return (input())
def II():    return (int(input()))
def MI():    return (map(int,input().split()))
def LI():    return (list(map(int,input().split())))
def isPerfectSquare(x): return (int(math.sqrt(x))**2 == x)

def partition(self, s: str) -> List[List[str]]:
    res = []
    listt = []
    def isPal(s,idx,i):
        x = s[idx:i+1]
        return x == x[::-1]
    def palindrome(idx):
        if idx == len(s):
            res.append(listt[:])
            return
        for i in range(idx,len(s)):
            if isPal(s,idx,i):
                listt.append(s[idx:i+1])
                palindrome(i+1)
                listt.pop()
    palindrome(0)
    return res