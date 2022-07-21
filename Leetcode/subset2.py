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
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    res = [[]]
    listt = []
    nums.sort()
    def subset(idx):
        if len(listt) >= 1 and listt not in res:
            res.append(listt[:])
        for i in range(idx,len(nums)):
            # if i is not first element and it is an duplicate we don't pick it up
            # so we have continued for it.
            if i > idx and nums[i] == nums[i-1]:
                continue;
            listt.append(nums[i])
            subset(i+1)
            listt.pop()
    subset(0)
    return res