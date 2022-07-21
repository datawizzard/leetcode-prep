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
def letterCasePermutation(self, s: str) -> List[str]:
    # Recursive solutiion
    n = len(s)
    res = []
    def permute(s,curr,idx):
        if len(curr) == len(s):
            res.append(curr)
            return
        if s[idx] >= '0' and s[idx] <= '9':
            return permute(s,curr + s[idx],idx + 1)
        else:
            return (permute(s,curr + s[idx].upper(),idx + 1) or
            permute(s,curr + s[idx].lower(),idx + 1))
    permute(s,"",0)
    return res

# Backtracking solution
    ret = []; chars = list(S)
    def backtrack(i):
        ret.append(''.join(chars))
        for i in range(i, len(chars)):
            if chars[i].isalpha():
                chars[i] = chars[i].swapcase()
                backtrack(i+1)
                chars[i] = chars[i].swapcase() # undo       
    backtrack(0)
    return ret
# One liner
    return map(''.join, product(*[set([i.lower(), i.upper()]) for i in s]))