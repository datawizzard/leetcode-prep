import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
import bisect
def cnt_(x, idx):
    cnt = 0
    for i in range(idx, len(pop)):
        if x >= pop[i]:
            cnt, x = cnt+1, pop[i]*2
        else:
            while x < pop[i]:
                cnt, x = cnt+1, x*2
            cnt += 1
            x = pop[i]*2
    return cnt+idx

t = int(input())
while t:
    n, x = [int(i) for i in input().split()]
    pop = [int(i) for i in input().split()]
    pop.sort()
    idx = bisect.bisect_right(pop, x, lo=0, hi=len(pop))
    print(min(cnt_(x, idx), cnt_(x, max(0, idx-1))))
    t = t - 1