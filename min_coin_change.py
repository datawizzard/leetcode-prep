import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
# import sys
# import math
# import heapq
# def input(): return sys.stdin.readline().strip("\n")
# def I():    return (input())
# def II():    return (int(input()))
# def MI():    return (map(int,input().split()))
# def LI():    return (list(map(int,input().split())))
# def isPerfectSquare(x): return (int(math.sqrt(x))**2 == x)
def coinChange(self, coins: List[int], amount: int) -> int:
    n = len(coins)
    dp = [999999 for i in range(amount + 1)]
    dp[0] = 0
    for i in coins:
        for j in range(1 , amount + 1):
            if j >= i:
                dp[j] = min(dp[j] , 1 + dp[j - i])
    if dp[-1]== 999999:
        return -1
    else:
        return dp[-1]
        