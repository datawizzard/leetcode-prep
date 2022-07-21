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
def funct(S):
    ans,prev = 0,'$'
    for i in S:
        if prev == i:
            c += 1
        else:
            c = 1
            prev = i
        ans = max(ans,c)
    return ans
for _ in range(int(input())):
    n = int(input())
    s = input()
    q = int(input())
    X = list(map(int,input().split()))
    Y = list(map(str,input().split()))
    res = [0]*(q)
    for i in range(q):
        s = s[:X[i] - 1] + Y[i] + s[X[i]:]
        res[i] = funct(s)
    print(*res)
# def maximum_length (N, S, Q, X, Y):
#     # Write your code here
#     res = []
#     for i in range(Q):
#         S = S[:X[i] - 1] + Y[i] + S[X[i]:]
#         ans,prev,c = 0,'$',0
#         for i in S:
#             if prev == i:
#                 c += 1
#             else:
#                 c = 1
#                 prev = i
#             ans = max(c,ans)
#         res.append(str(ans))
#     return res
#     pass

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     S = input()
#     Q = int(input())
#     X = list(map(int, input().split()))
#     Y = input().split()
#     out_ = maximum_length(N, S, Q, X, Y)
#     print (' '.join(map(str, out_)))