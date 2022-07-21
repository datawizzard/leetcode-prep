
# Product Samples
m = len(matrix)
n = len(matrix[0])
dp = [[0 for j in range(n)] for i in range(m)]
ans = 0
if m == 0 or n == 0:
    return 0
for row in range(m):
    for col in range(n):
        if matrix[row][col] == "1":
            dp[row][col] = 1
            if row > 0 and col > 0:
                dp[row][col] += min(dp[row-1][col],dp[row][col-1],dp[row-1][col-1])
            ans = max(ans,dp[row][col])
return ans

# Lexicographically Largest String
def nextlower(bucket,left):
    for i in range(left-1,-1,-1):
        if bucket[i] > 0:
            bucket[i] -= 1
            return chr(i + ord('a'))
    return ''
def solve(s,k):
    bucket = [0]*26
    ans = ''
    for i in s:
        bucket[ord(i) - ord('a')] += 1
    for i in range(25,-1,-1):
        count = 0
        while (bucket[i] > 0):
            ans += chr(i + ord('a'))
            bucket[i] -= 1
            count += 1
            if (bucket[i] > 0 and count == k):
                sol = nextlower(bucket,i)
                ans += sol
                count = 0
    return ans

# Bit Manipulation
def minimumOneBitOperations(self, n: int) -> int:
    res = 0
    while n:
        res = -res - (n ^ (n - 1))
        n &= n - 1
    return abs(res)

# Sign-In Sign-Out logs
logs = ["30 100 Sign-In","30 105 Sign-Out"]
maxspan = II()
ans = []
d = defaultdict(int)
for s in logs:
    a,b,c = s.split(" ")
    print(a,b,c)
    if a in d:
        if abs(int(b) - int(d[a])) <= maxspan:
            ans.append(a)
    else:
        d[a] = b
    print(d)
print(ans)


# String reduction
ans = 0
from collections import Counter
c = Counter(s)
for i in c:
    if c[i] > 1:
        ans += c[i] - 1
print(ans)


# Even Subarray
ans = 0
n = len(nums)
for i in range(n):
    temp2 = []
    k = 0
    check = set()
    for j in range(i,n):
        if i == 0:
            if nums[j]%2 == 1:
                temp2.append(1)
            else:
                temp2.append(0)
            if temp2[k] <= K and nums[j] not in check:
                ans+=1
                check.add(nums[j])
        else:
            if nums[j]%2 == 1:
                temp2.append(temp1[k]+1)
            else:
                temp2.append(temp1[k])
            if temp2[k] <= K and tuple(nums[k:j+1]) not in check:
                ans+=1
                check.add(tuple(nums[k:j+1]))
        k+=1
    temp1 = list(temp2)

return ans


# Conference Schedule
 def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key=lambda x: x[1])
        visited = set()
        for s, e in events:
            for t in range(s, e+1):
                if t not in visited:
                    visited.add(t)
                    break
        return len(visited)

# Optimised
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        min_heap = []  # min heap of events end time
        events.sort(key = lambda e: e[0])  # sort events by start time

        i = count_events_attended = cur_day = 0
        while i < len(events) or min_heap:
            if not min_heap:
                cur_day = events[i][0]
            
            # add open events for cur_day
            while i < len(events) and events[i][0] <= cur_day:
                heappush(min_heap, events[i][1])
                i += 1

            heappop(min_heap)  # attend the event ends earliest
            count_events_attended += 1

            cur_day += 1
            # remove close events for cur_day
            while min_heap and min_heap[0] < cur_day:
                heappop(min_heap)

        return count_events_attended


# Group of anagram
 def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for num in strs:
            x = "".join(sorted(num))
            d[x].append(num)
        return list(d.values())

# Closest Number
def closestNumbers(arr):
    # Write your code here
    arr.sort()
    ans = []
    m = float('inf')
    for i in range(len(arr)-1):   # Finding min abs diff......
        m = min(arr[i+1]-arr[i],m)  
    
    for i in range(len(arr)-1): 
        if arr[i+1]-arr[i] == m:
            ans.append(arr[i])
            ans.append(arr[i+1])


# Birthday Card Collection
for i in range(len(arr)):
    if i == 0:
        s = 1
    else:
        s = arr[i-1] + 1
    if i != len(arr):
        e = arr[i]
    else:
        e = float('inf')
    if d < s:
        break;
    for k in range(s,e):
        if k <= d:
            result.append(k)
            d -= k
        else:
            break;
print(result)

bal=0
ans=0
for i in range(0,len(p)):
    if(p[i]=='('):
        bal+=1
    else:
        bal+=-1
        
    # It is guaranteed bal >= -1
    if(bal==-1):
        ans+=1
        bal+=1
return bal+ans