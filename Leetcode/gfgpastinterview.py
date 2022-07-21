# Return Row No having maximum count of 1
# TC : O(NlogM)
class Solution:
	def rowWithMax1s(self,arr, n, m):
        pos,ans,count = -1,0,0
        for i,row in enumerate(arr):
            # print(row)
            low,high = 0,m-1
            # flag = False
            while low <= high:
                mid = low + (high - low)//2
                # print(mid)
                if (mid == 0 or row[mid - 1] == 0) and row[mid] == 1:
                    count = mid
                    break;
                elif row[mid] == 0:
                    low = mid + 1
                else:
                    high = mid - 1
            if m - count > ans and row[-1] == 1:
                ans = m - count
                pos = i
        return pos

# Optimised Version 
# TC : O(M + N)
def rowWithMax1s( mat):
    # Initialize max values
    R = len(mat)
    C = len(mat[0])
    max_row_index = 0
    index=C-1;
    # Traverse for each row and
    # count number of 1s by finding
    # the index of first 1
    for i in range(0, R):
      flag=False #to check whether a row has more 1's than previous
      while(index >=0 and mat[i][index]==1):
        flag=True #present row has more 1's than previous
        index-=1
        if(flag): #if the present row has more 1's than previous
          max_row_index = i
      if max_row_index==0 and mat[0][C-1]==0:
        return 0;
    return max_row_index


 # Minimum Cut of Ropes
 # TC : O(nlogn)
 # SC : O(N)
 class Solution:
    #Function to return the minimum cost of connecting the ropes.
    import heapq
    def minCost(self,arr,n) :
        heapq.heapify(arr)
        res = 0
        while len(arr) > 1:
            x = heapq.heappop(arr)
            y = heapq.heappop(arr)
            res += x + y
            heapq.heappush(arr,x + y)
        return res


# merge Two Array without extra space
# TC : O(N + M)
# SC : O(N + M)
# Its using extra space
def merge(self,arr1,arr2,n,m):
    #code here
    temp = []
    i,j = 0,0
    while i < n and j < m:
        if arr1[i] > arr2[j]:
            temp.append(arr2[j])
            j += 1
        else:
            temp.append(arr1[i])
            i += 1
    while j < m:
        temp.append(arr2[j])
    while i < n:
        temp.append(arr1[i])
    for i in range(n):
        arr1.append(temp[i])
    for j in range(m):
        arr2.append(temp[n - 1 + j])


# TC : O(NlogN + MlogM + min(N,M))
    # the idea is if arr2 element is less than arr1 element then its must 
    # be present in arr1,so we swap it from right most element in arr1 as it is greatest most
    # element.If arr1 is greater than arr2 we simply move the pointer for arr1.
        i,j,k = 0,0,n-1
        while i <= k and j < m:
            if arr1[i] < arr2[j]:
                i += 1
            else:
                arr1[k],arr2[j] = arr2[j],arr1[k]
                k -= 1
                j += 1
        arr1.sort()
        arr2.sort()


# kadance Alogrithm : Maximum Subarray
# TC : O(n^3)
# SC : O(1)
    # Brute Force : Considering every subarray 
    ans = float('-inf')
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            ans = max(ans,sum(nums[i:j+1]))
    return ans
    # Better 
    # TC : O(N^2)
    # SC : O(1)
    ans = float('-inf')
    for i in range(len(nums)):
        s = 0
        for j in range(i,len(nums)):
            s += nums[j]
            ans = max(ans,s)
    return ans

    # Optimal : Kadance Algorithm
    # TC : O(N)
    # SC : O(1)
    maxi,sums = nums[0],0
    for n in nums:
        sums += n
        maxi = max(sums,maxi)
        sums = max(0,sums)
    return maxi

# Merge Interval
# TC : O(nlogn)
# SC : O(N)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals.sort()
        a,b = intervals[0][0],intervals[0][1]
        temp = []
        for x in intervals:
            if x[0] > b:
                temp.append([a,b])
                a,b = x[0],x[1]
            else:
                b = max(b,x[1])
        temp.append([a,b])
        return temp

# Find the duplicate and missing number 
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dup,mis = 0,1
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                dup = nums[i]
            elif nums[i] > nums[i-1] + 1:
                mis = nums[i-1] + 1
        if nums[n - 1] != n:
            return [dup,n]
        else:
            return [dup,mis]

 # Method II : Using hash
  # TC : O(N)
  # SC : O(N)
 class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup,mis = 0,0   
        c = Counter(nums)
        for i in range(1,n + 1):
            if i in c:
                if c[i] == 2:
                    dup = i
            else:
                mis = i
        return [dup,mis]
 # Method III : Simple Math
# Get the sum of all numbers using formula S = N(N+1)/2
# Get the sum of square of all numbers using formula Sum_Sq = N(N+1)(2N+1)/6
# Iterate through a loop from i=1….N
# S -= A[i]
# Sum_Sq -= (A[i]*A[i])
# It will give two equations 
# x-y = S – (1) 
# x^2 – y^2 = Sum_sq 
# x+ y = (Sum_sq/S) – (2) 
  # TC : O(N)
  # SC : O(1)
    sums = (n * (n + 1)) // 2
    sumsq = (n*(n+1)*(2*n+1)) // 6
    for i in arr:
        sums -= i
        sumsq -= i*i
    mis = ((sumsq // sums) + sums) // 2
    rep = mis - sums
    return rep,mis


    # Find the duplicate number
    # Method I :
    # TC :  O(NlogN)
    # SC : O(1)
    class Solution:
        def findDuplicate(self, nums: List[int]) -> int:
            nums.sort()
            for i in range(len(nums) - 1):
                if nums[i] == nums[i+1]:
                    return nums[i]

    # Method II: TC : O(N),SC : O(N)
    c = Counter(nums)
    for i in c:
        if c[i] > 1:
            return i

    # Method III: Floyd Tortoise and Hare (Cycle Detection)
    # TC : O(N)
    # SC : O(1)
    tortoise = hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break;
    # Find entrance of cycle
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    return tortoise

# Set Matrix Zero
 # Brute Force : TC : O(N * M)
 #             : SC : O(N + M)
 class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        # Storing all rows and column having zero before hand
        row = set()
        col = set()
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        # Check if row column is present in required array
        # If its present cange it 0
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0
        print(matrix)

# Optimal Approach : TC : O(N*M)
#                  : SC : O(1)
        # Approach : For first column we handle the case differently
        # because if we found zeros in first column and if we set first dummy row to
        # zero it change the dummy value for other rows also as it is common for
        # both first row and column which is (0,0).
        # Consider case:
        # [[1,1,1,1],
        #  [0,1,0,1],
        #  [1,0,1,1],
        #  [1,1,0,,1]]
        # Here first column 0 makes (0,0) to 0 which ulitmately set all row values to 
        # zeroes which is not true.
        m = len(matrix)
        n = len(matrix[0])
        cols = 1
        for i in range(m):
            if matrix[i][0] == 0:
                cols = 0
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,0,-1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if cols == 0:
                matrix[i][0] = 0
        

# pascal Triangle : Print all levels of pascal triangle
# TC : O(N^2)
# SC : O(N)
# Approach : Its based on pattern
#  for given every row,col the formula to find value at that (row,col) is  (row - 1)C(col - 1)
# according to 1- based indexing
class Solution:
    def generate(self,n: int) -> List[List[int]]:
        res = []
        for x in range(n):
            C = [1] * (x+1)
            for i in range(x):
                C[i+1] = (C[i] * (x-i)) // (i+1)
            res.append(C)
        return res
# To find only nth row of pascal triangle
# Brute Force == DP : TC : O(N^2)
def getRow(self, n: int) -> List[int]:
    triangle = []
    for i in range(n + 1):
        C = [1]*(i + 1)
        C[0] = C[-1] = 1
        for j in range(1,i):
            C[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(C)
    return C

# Optimal : Using math : Don't need to calculate previous rows
# TC : O(N)
# SC : O(N)
    C = [1] * (x+1)
    for i in range(x):
        C[i+1] = (C[i] * (x-i)) // (i+1)
    return C


# Next Permutation 
# Brute Force : Finding all Permutation
 # TC : O(N!)
# SC: O(N!)
    res = []
    def permute(nums, l, r):
        if l==r:
            res.append(nums[:])
        else:
            for i in range(l,r):
                nums[l], nums[i] = nums[i], nums[l]
                permute(nums, l+1, r)
                nums[l], nums[i] = nums[i], nums[l] #backtrack
    permute(nums,0,len(nums))
    print(res)
    for pos,a in enumerate(res):
        if a == nums:
            ans = pos
    if ans == pos:
        nums = res[0]
    else:
        x = res[ans+1]
        nums = x[:]

    # Method II : 
    # TC : O(N)
    # SC : O(1)
    def nextPermutation(self, nums: List[int]) -> None:
        def revers(a,i,j):
            while i < j:
                a[i],a[j] = a[j],a[i]
                i += 1
                j -= 1
        if nums is None or len(nums) == 1:
            return
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:  # Step I : Run loop from backward till
            i -= 1                           # previous element is less than curr element
                                    # which will be breakpoint of our solution
        if i >= 0:      # Step II : If breakpoint is there find the element which is just
            j = len(nums) - 1   # greater than breakpoint element in order to find next greater than 
            while nums[i] >= nums[j]:  # permutation and swap it as STEP III
                j -= 1
            nums[i],nums[j] = nums[j],nums[i] 
        revers(nums,i+1,len(nums)-1) # Last step is to reverse after breakpoint to the end of array
                                    # as we already swap breakpoint to next greater element
                                    # its become greater and since right of breakpoint is 
                                    # decreasing iterating from left we reverse it so that
                                    # its value from left to right decreaases after the breakpoint.


# Count Inversion
# Brute Force :TC : O(N^2)
#              SC : O(1)
def inversionCount(self, arr, n):
    count = 0
    for i in range(n):
        for j in range(n):
            if i < j and a[i] > a[j]:
                count += 1
    return count

# Optimal Approach : TC : O(NlogN) : SC : O(N)
# To be later

# Best time to buy sell Stocks
# Approach : At every price point find difference between current price and minimum price
#            so far till the current price and store difference.The maximum difference will 
#            our ans
#           We initialised maxprofit with 0 since if prices are in decreasing order
#           we don't need to buy or sell something and then ans will be 0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprices,maxprofit = float('inf'),0
        for i in range(len(prices)):
            if prices[i] < minprices:
                minprices = prices[i]
            elif prices[i] - minprices > maxprofit:
                maxprofit = prices[i] - minprices
        return maxprofit

        # same approach with different style
        for pay in prices:
            minprices = min(pay,minprices)
            maxprofit = max(maxprofit,pay - minprices)
        return maxprofit


# Rotate Matrix
# TC : O(N^2)
# SC : O(1)
# Step I : Transpose the matrix
# Step II : Reverse every row 
m = len(matrix)
for i in range(m):
    for j in range(i):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
for i in range(m):
    matrix[i] = matrix[i][::-1]


# Flip Character to make Monotonic Increasing
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        now,ones,zeroes = 0,s.count('1'),s.count('0')
        ans = min(ones,zeroes)
        n = len(s)
        for i,ch in enumerate(s):
            if ch == '1':
                now += 1
            # now stores count of ones till i pos.
# approach : at every pos of i we have to flip all 1 to 0 till i and flip all zero to 1 after i
# So now == no. of 1 till i to flip it 0 + no. of 0 after i to flip it 1
# and store minimum of all the value.
            curr = now + ((n - i - 1) - (ones - now))
            ans = min(ans,curr)
        return ans


# 2D search a matrix

# Method I : Linear Search in Whole matrix
# TC : O(M*N)
# SC : (1)

# Method II : Binary Search
# TC : O(MlogN) : m X n matrix
# SC : O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(a,i,j):
            while i < j:
                mid = i + (j -i)//2
                if a[mid] == target:
                    return True
                elif a[mid] > target:
                    j = mid
                else:
                    i = mid + 1
            return False
        n = len(matrix[0])
        for a in matrix:
            if binary_search(a,0,n):
                return True
        return False

# Method III : Optimise Binary Search
# TC : O(log(M*N))
# SC : O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i,j = 0,m*n
        while i < j:
            mid = i + (j-i)//2
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] > target:
                j = mid
            else:
                i = mid + 1
        return False

# Method IV: Saddle Search
# Iterate fom top most right corner
 class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = 0,len(matrix[0])-1
        m = len(matrix)
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

# Pow (x,n)
# TC : O(N)
# SC: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        mn = n
        if mn < 0:
            mn = -1*mn
        for i in range(1,mn  + 1):
            ans *= x
        if n < 0:
            return 1 / ans
        else:
            return ans
# using python inbuilt fn
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n

# Using fast exponentiation
# TC : O(log(N))
# SC : O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        mn = n
        if n < 0:
            mn = -1 * n
        while mn > 0:
            if mn % 2 == 0:
                x = x * x
                mn = mn // 2
            else:
                ans = ans * x
                mn -= 1
        if n < 0:
            return 1 / ans
        else:
            return ans


# Majority Element
# Method I : Brute Force
# TC : O(N^2)
# SC : O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        maxel = n / 2
        for num in nums:
            count = 0
            for ele in nums:
                if num == ele:
                    count += 1
            if count > maxel:
                return num

# Method II : Hashing
# TC :O(N)
# SC :O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    n = len(nums)
    c = Counter(nums)
    for i in c:
        if c[i] > n / 2:
            return i

# MEthod III : Sorting
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
# Moore Voting Algorithm
# MEthod IV : TC : O(N) : SC : O(1)
# The intution is every time the equal number of majority and equal number of minority element 
# cancel each out i.e when count == 0 element till then will cancel out each other.
# at last major element frequency must be  greater than minor element and  it can't cancel
# out and thus return our ans as candidate element
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = 0
        for num in nums:
            # Count will be zero when majority number will be equal to minority number of prefix.
            if count == 0:
                candidate = num
            # If candidate equals nums we increse the count else decrease.
            count += (1 if num == candidate else -1)
        return candidate


# Majority Element II : 
# Method I : Brute Force
# TC : O(N^2)
# SC : O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        maxel = n / 3
        for num in nums:
            count = 0
            for ele in nums:
                if num == ele:
                    count += 1
            if count > maxel:
                return num

# Method II : Hashing
# TC : O(N)
# SC : O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = []
        c =Counter(nums)
        for x in c:
            if c[x] > n / 3:
                a.append(x)
        return a

# Method III : 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                # If new element is not considered as our candidate
                # then condition will will run.
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3]


# Unique Paths
# TC : O(2^N)
# SC : O(2^N) : Recursion Stack
# We traverse every grid possible and at every cell we have two options
# so final complexity will be 2^N
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i,j):
            # For out of bounds
            if i >= m or j >= n:
                return 0
            # if we reach at the end of grid i.e m-1 and n - 1
            if i == (m - 1) and j == (n - 1):
                return 1
            else:
            # else we have two option 
            # either we can go down or we can go right in the grid.
                return helper(i+1,j) +  helper(i,j+1)
        return helper(0,0)


# Method II : Dynamic programming
# TC : O(N*M)
# SC : O(N*M)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                # If row is 0 we have only one way to reach every cell in 1st row
                if i == 0:
                    dp[i][j] = 1
                # If col is 0 we have only one way to reach every cell in 1st column.
                elif j == 0:
                    dp[i][j] = 1
                # else we either go down or we go right
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

# Method III : Permuatation and Combination
# Formula is (m + n -2)C(m-1) nhi toh  (m + n - 2)C(n-1)
# TC : O(m-1)
# SC : O(1)
 def uniquePaths(self, m: int, n: int) -> int:
    N = m + n - 2
    r = m - 1
    res = 1
    num,deno=1,1
    for i in range(1,r+1):
        num *= (N - r + i)
        deno *= i
    return int(num/deno)

# Two Sum
# Method I: Brute Force
# TC : O(N^2)
# Using two loops

# Method II : Hashing 
# TC : O(N)
# SC : O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i,ele in enumerate(nums):
            if target - ele in idx:
                return [i,idx[target - ele]]
            idx[ele] = i


# 4 Sum  
# Method I : Brute Force
  # TC : O((N^3)*log(N))
  # SC : O(1)
  class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        def binary_search(i,j,arr,k):
            while i <= j:
                mid = i + (j -i)//2
                if arr[mid] == k:
                    return True
                elif arr[mid] > k:
                    j = mid - 1
                else:
                    i = mid + 1
            return False
        sett = set()
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1,n-2):
                for m in range(j + 1,n):
                    s = nums[i] + nums[j] + nums[m]
                    if binary_search(m+1,len(nums)-1,nums,target - s):
                        sett.add((nums[i],nums[j],nums[m],target - s))
        return sett


# Method II : Using Two pointer 
# TC : O(N^3)
# SC : O(1)
    class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-3):
            for j in range(i+1,n-2):
                new_tar = target - nums[i] - nums[j]
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    sums = nums[left] + nums[right]
                    if sums < new_tar:
                        left += 1
                    elif sums > new_tar:
                        right -= 1
                    else:
                        ans = []
                        ans.append(nums[i])
                        ans.append(nums[j])
                        ans.append(nums[left])
                        ans.append(nums[right])
                        res.append(ans)
                        while left < right and nums[left] == ans[2]:
                            left += 1
                        while left < right and nums[right] == ans[3]:
                            right -= 1
                while j+1 < n and nums[j+1] == nums[j]:
                    j += 1
            while (i + 1) < n and nums[i + 1] == nums[i]:
                i += 1
        return res

# longest Consecutive Sequence
# method I : Brute Force
# TC : O(N^2)
# SC : O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            count = 1
            # Start every element and count no. of consecutive element after it
            # and return max of all count
            while n + 1 in nums:
                n = n + 1
                count += 1
            ans = max(ans,count)
        return ans

# Method II : Sorting
# TC : O(NlogN)
# SC : O(1)
        nums.sort()
        count = 1
        ans = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] = nums[i-1] + 1:
                    count += 1
                else:
                    ans = max(count,ans)
                    count = 1
            # If else condition not reached and count > ans then max value of count will
            # not store in ans that why we have to return max of count and ans.
        return max(ans,count)


# Method III: Hashset
# TC : O(N + N + N)
# SC : O(N)
# The intution behind its is to find head of consecutive number.
# If n - 1 is present in set that means its not head of consecutive number so we iterate 
# forward in loop in search of finding head of consecutive number so inner while loop will not 
# executed.
# If n - 1 is not in s that means its head of consecutive number.
# After finding head we iterate forward by increasing 1 to that head and if find n + 1 in s
# that means we got new consecutive number,so we increase the currstreak of consecutive number by 1
# and after each iteration we store max streakvalue in ans and return it at last.
        s = set(nums)
        for n in nums:
            if n - 1 not in s:
                currstreak = 1
                while n + 1 in s:
                    currstreak += 1
                    n += 1
                ans = max(ans,currstreak)
        return ans


# Largest Substring with Zero Sum
# Method I : Brute Force
# TC : O(N^3)
# SC : O(1)
    maxlen = 0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if sum(arr[i:j+1]) == 0:
                maxlen = max(maxlen,j - i + 1)
    return maxlen

# Method II : Optimised Brute Forced
# TC : O(N^2)
# SC : O(1)
    maxlen = 0
    for i in range(len(arr)):
        s = 0
        for j in range(i,len(arr)):
            s += arr[j]
            if s == 0:
                maxlen = max(maxlen,j - i + 1)
    return maxlen

# Method III : Hashing
 # TC : O(N)
 # SC : O(N)
 # Intution behind we store every prefix sum in hashset  from left to right
 # if prefix sum visited again after some forward iteration that means
 # the gap between substring of those two prefix value has sum 0 because
 # prefix only repeats if in between sum of substring between those two is 0
 # so we store the difference between the index of those two prefix and return max of it in last.
    s = 0
    maxlen = 0
    d = {}
    for i,n in enumerate(arr):
        s += arr[i]
        # At any point if s become 0 then len of largest substring will be from 0 to i.
        # hence len will be i + 1
        if s == 0:
            maxlen = i + 1
        else:
            if s in d:
                # If its already there that means sum between those substring will be 0.
                # So we will subtract its index difference.
                maxlen = max(maxlen,i - d[s])
            else:
                # If prefix sum not in dict add its sum,index pair in dict.
                d[s] = i
    return maxlen


# Count Number of Subarray having given Xor
# TC : O(N)
# SC : O(N)

from collections import defaultdict
def subarrayXor(arr, n, m):
    d=defaultdict(bool)
    d[0]=1
    count=0
    curSum=0
    for i in arr:
        curSum^=i
        if d[curSum^m]:
            count+=d[curSum^m]
        d[curSum]+=1
    return(count)

# Longest SubsString Without Repeating Character
# Method I : Brute Force
# TC : O(N^3)
# SC : O(N)
        n = len(s)
        maxlen = 0
        for i in range(n):
            for j in range(i,n):
                if len(s[i:j+1]) == len(Counter(s[i:j+1])):
                    maxlen = max(maxlen,j - i + 1)
        return maxlen

# Method II :  Optimised 
# TC : O(N + N) : Every character will be visited at max twice in worst case
# SC : O(N)
# intution behind it : Have to create a window of maximum length in which no repeating element 
# should be there.
# Starting l,r two pointer from 0 and r till window does not contain repeating element
# To check for repeating element we add new char in set every time the character not present in
# set.Slide the pointer r to right every time new character found and store length of that window
# in res.
# Now suppose if element is present in set that means current character at s[r] is repeating 
# element in window so we shrink the window from left i.e remove character from left 
# till repeating element present in the window.
# After whole iteration it res will store max len of window having all unique character.
        l = 0
        res = 0
        t = set()
        for r in range(len(s)):
            while s[r] in t:
                t.remove(s[l])
                l += 1
            t.add(s[r])
            res = max(res,r - l + 1)
        return res

# Method III : Using Map
 # TC : O(N)
 # SC : O(N)
 # same concept as set one just difference is that we did not have to delete and iterate 
 # till s[r] in present in set.Rather we store the (char,index) as key value pair where 
 # index is location of char last found.If char repeats we just start new window just after
 # last occurence of that charcter that is max(l,d[s[r]] + 1).here max of l and d[s[r]] because
 # if last occurence of char is outside the window so no need to go back outside window
 # and l will remain same.
 l,r = 0,0
 res = 0
 d = {}
 while r < len(s):
    if s[r] in d:
        l = max(l,d[s[r]] + 1)
    d[s[r]] = r
    res = max(res,r - l + 1)
    r += 1
return res


# Reverse A Link List:
# TC : O(N)
# SC : O(1)
prev  = None
curr = head
while curr:
    nextnode = curr.next
    curr.next = prev
    prev = curr
    curr = nextnode
return prev

# Middle of Link list
# Method I : Brute Force
# Count number of nodes in link list : c
# Next iteration return c//2 + 1 which will return middle of link list
# TC : O(N)
# SC : O(1)
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Merge Two Sorted Link List
# TC : O(L1 + L2)
# SC : O(1)
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l1 = l1.next
            else:
                curr.next = l1
                l2 = l2.next 
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

# Delete Nth Node From Last
# Method I : TC : O(N + N)
#          : SC : O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        curr = head
        if count == n:
            return head.next
        for i in range(count - n - 1):
            curr = curr.next
        node = curr.next
        curr.next = curr.next.next
        del(node)
        return head

# Method II : Using two pointer
# TC : O(N)
# SC : O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        count = 0
        while count < n:
            fast = fast.next
        # if n == no. of nodes then,
        if fast == None:
            return head.next 
        while fast.next:
            slow = slow.next 
        node = slow.next 
        slow.next = slow.next.next 
        del(node)
        return head

# Delete node of link link if head is not given.
# TC : O(1)
# SC : O(1)
# Just copy the next node value to the node which has to be deleted and
# delete the next node
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

# Add Two Number as a link list
# TC : O(max(l1,l2))
# SC : O(N)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry,val = 0,0
        while l1 or l2 or carry:
            v1,v2 = 0,0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val 
                l2 = l2.next
            v = v1 + v2 + carry
            value = v % 10
            carry = v // 10
            curr.next = ListNode(value)
            curr = curr.next
        return dummy.next  

# Intersection of Two link List
# Brute Force : O(N*M)
# SC : O(1)
# Comparing whole link list for every node.
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp = headB
        while headA:
            while headB:
                if headA == headB:
                    return headA
                headB = headB.next
            headA = headA.next
            headB = temp
        return None

# Better Approach 
# Method II : Hashing
# TC : O(N + M)
# SC : O(N)
        vis = set()
        while headA:
            vis.add(headA)
            headA = headA.next 
        while headB:
            if headB in vis:
                return headB
            headB = headB.next 
        return None

# Optimal I:
# TC : O(M + N)
# SC : O(1)
# the intution behind is we have to traverse that extra diference between the
# the two link list.When two link list traverse simultaneously the position of two 
# pointer of two link list must be difference between two nodes.
# So when swap pointer that extra difference is compensated and after 1 iteration completed
# the two pointer starts at same distance from intersection.
        curr1 = headA
        curr2 = headB
        while curr1 != curr2:
            if curr1:
                curr1 = curr1.next
            else:
                curr1 = headB
            if curr2:
                curr2 = curr2.next
            else:
                curr2 = headA
        return curr2


# Detect Cycle In a Link List
# Method I : Hashing
# TC : O(N)
# SC : O(N)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        curr = head
        while curr:
            if curr in s:
                return True
            s.add(curr)
            curr = curr.next
        return False

# Method II : Rabit Hare Problem
# the intutition behind is since link list which contain cycle 
# and two pointer running on it must meet to each other since their 
# speed are different.
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        

# Reverse Link List In Size of K
# To be done later 

# Palindromic Link List
# Method I : Brute Force
# TC : O(N + N) : One iterations for 
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        a = []
        while curr:
            a.append(curr.val)
            curr = curr.next
        return a == a[::-1]
# Method II : 
# TC : O(N/2 + N/2 + N/2 + N/2)
# SC : O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        # Reverse second part after middle element
        def reverse(l1):
            curr = l1
            prev = None
            while curr:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
            return prev
        # Finding middle of element
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = reverse(slow)
        # Start pointer from first node of LL from first part
        # and start with first node of second part and start comparing 
        # till second part is not null.
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True

# Link List Cycle II :
# Method I : brute Force
# Hashing : TC : O(N), SC : O(N)
# If node visited again in set tat means cycle is there
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = set()
        if head is None or head.next is None:
            return None
        curr = head
        while curr:
            if curr in s:
                return curr
            s.add(curr)
            curr = curr.next
        return None

# Method II : Two pass Solution using Two Pointer
# TC : O(N)
# SC : O(1)
# Intution : Distance travelled by Slow pointer = L1 + L2
#            Distance travelled by fast pointer = L1 + L2 + nC where C is length of cycle
#            and n is no. of cycle turns.
#            2*(L1 + L2) = L1 + L2 + nC
#            L1 = nC - L2 
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break;
        else:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

# Flattening the link list
def merge(l1,l2):
    dummy = Node(0)
    curr = dummy
    while l1 and l2:
        if l1.data > l2.data:
            curr.bottom = l2
            l2 = l2.bottom
        else:
            curr.bottom = l1
            l1 = l1.bottom
        curr = curr.bottom
    curr.bottom = l1 or l2
    return dummy.bottom

def flatten(root):
    # Base Case
    if root is None or root.next is None:
        return root
    # Recursion goes deep 
    root.next = flatten(root.next)
    # returning from calling stack goiing upward in recursion
    root = merge(root,root.next)
    # After each merge root will be returned
    return root

# Rotate Link List 
# Method I : Brute Force
# TC : O(k*N)
# SC : O(1)
# Intution : Everytime we go to the last node break the node the with
# node  and points it with
# head node.Doing this k times will give our result.
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> 
        curr = head
        if head is None:
            return None
        if head.next is None:
            return head
        i,count = 0,0
        while curr:
            count += 1
            curr = curr.next
        k = k % count
        while i < k:
            curr = head
            prev = None
            while curr and curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
            curr.next = head
            head = curr     
            i += 1
        return head

# Method II: 
# TC : O(N + (N - N % k))
# SC : O(1)
# Step I : First count the number of nodes in link list
#        because if k > len(link list) then 
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) ->
        curr = head
        if head is None:
            return None
        if head.next is None:
            return head
        i,count,j = 0,1,0
        while curr and curr.next:
            count += 1
            curr = curr.next
        k = k % count
        curr.next = head
        while j < count - k:
            curr = curr.next
            j += 1
        head = curr.next
        curr.next = None
        return head

# Clone A Link List with Next and Random Pointer
# Method I : Hashing
# TC : O(N + N)
# SC : O(N)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        hashmap = {None:None}
        curr = head
        # Step I : Mapping old node with deep copy of that node
        while curr:
            copy = Node(curr.val)
            hashmap[curr] = copy 
            curr = curr.next 
        curr = head 
        # Step II : Connecting next and random pointer of deep copy nodes
        while curr:
            copy = hashmap[curr]
            copy.next = hashmap[curr.next]
            copy.random = hashmap[curr.random]
            curr = curr.next
        return hashmap[head]

# Method II : Without Using extra space
# TC : O(N)
# SC : O(1)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        iters = front = head
        while iters:
            front = iters.next
            copy = Node(iters.val)
            iters.next = copy
            copy.next = front
            iters = front
        iters = head
        while iters:
            if iters.random:
                iters.next.random = iters.random.next
            iters = iters.next.next
        iters = head
        dummy = Node(0)
        copy= dummy
        while iters:
            front = iters.next.next
            copy.next = iters.next
            iters.next = front
            copy = copy.next
            iters = iters.next
        return dummy.next


# 3Sum
# Method I : Brute Force
# TC : O(N^3)
# SC : O(N)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:  
                        hel = sorted([nums[i],nums[j],nums[k]])
                        s.add(tuple(hel))
        return s

# Method II : HashMap
# TC : O(N^2 + N)
# SC : O(N)
        s = set()
        c = Counter(nums)
        n = len(nums)
        for i in range(n-2):
            c[nums[i]] -= 1
            for j in range(i+1,n-1):
                c[nums[j]] -= 1
                x = -(nums[i] + nums[j])
                if x in c and c[x] > 0:
                    h = sorted([nums[i],nums[j],x])
                    s.add(tuple(h))
                c[nums[j]] += 1
            c[nums[i]] += 1
        return s

# Method III: Two pointer
# TC : O(N * N)
# SC : O(M)
        a = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            low,high = i +1,n - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while low < high:
                if nums[i] + nums[low] + nums[high] == 0:
                    a.append([nums[i],nums[low],nums[high]])
                    # For handling duplicates
                    while low < high and nums[low] == nums[low+1]:
                        low+=1
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif nums[i] + nums[low] + nums[high] > 0:
                    high -= 1
                else:
                    low += 1    
        return a

# Rain Water Trapping
# Brute Force
# TC : O(N^2)
# SC : O(1)
        ans = 0
        n = len(height)
        for i in range(1,n):
            # Find max from current block to first block
            a = max(height[i::-1])
            # Find max from current block to last block
            b = max(height[i:])
            ans += min(a,b) - height[i]
        return ans
# Method II : Using prefix Sum Array
# Method 2:
    # Time COmplexity : O(N)
    # Space complexity : O(N)
    class Solution:
        def trap(self, height: List[int]) -> int:
            ans = 0
            n = len(height)
            left = [0]*n
            right = [0]*n
            left[0] = height[0]
            right[n-1] = height[n-1]
            for i in range(1,n):
                left[i] = max(left[i-1],height[i])
            for i in range(n-2,-1,-1):
                right[i] = max(right[i-1],height[i])
            for i in range(1,n-1):
                ans += min(left[i],right[i]) - height[i]
            return ans
# Method III : Using two Pointer
 # TC : O(N)
 # SC : O(1)
        if not height:
            return 0
        else:
            l ,r = 0,len(height) - 1
            res = 0
            leftmax,rightmax = 0,0
            while l < r:
                if height[l] <= height[r]:
                    leftmax = max(leftmax,height[l])
                    res += leftmax - height[l]
                    l += 1
                else:
                    rightmax = max(rightmax,height[r])
                    res += rightmax - height[r]
                    r -= 1
            return res

# Remove Duplicates from sorted array
# Method I : brute Force
# TC : O(NlogN + N)
# SC : O(N)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = []
        for i in nums:
            if i not in s:
                s.append(i)
        for i in range(len(s)):
            nums[i] = s[i]
        return len(s)

# Method II : Two pointer
# TC : O(N)
# SC : O(1)
# Intution : The idea is to find unique element copy it in front every time
# The first k index will present only unique and after that it may contain duplicates
# We find unique element by j pointer and copy it in i pointer.
        if len(nums) == 1:
            return len(nums)
        else:
            i,j = 0,1
            while j < len(nums):
                if nums[i] == nums[j]:
                    j += 1
                else:
                    i += 1
                    nums[i] = nums[j]
            return i + 1

# MAximum COnsecutive Ones
# TC : O(N)
# SC : O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,maxi = 0,0
        for i in range(len(nums)):
            # When 1,increase count and store it in maxi which store maximum consecutive 1
            if nums[i] == 1:
                count += 1
                maxi = max(maxi,count)
            # When 0 count become  so that we can start again with count = 0
            # when next 1 found
            else:
                count = 0
        return maxi


# N meeting in 1 Room
# TC : O(N + NlogN + N)
# SC : O(N)
# Approach : We can think of greedily that maximum number of meeting is only 
# possible when end time is as much less as possible.
# So we sort the array according to end time.
# And if curr start time of meeting is greater than prev end time of meeting,then
# we can complete that previous meeting, so we increase the ans by 1, and make
# curr meeting to previous meeting.
# We started ans from 1 because at last if two meeting time collide at least 1
# can do meeting from them.
class Solution: 
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        a = []
        for i in range(len(start)):
            a.append(([start[i],end[i]]))
        a.sort(key = lambda x : x[1])
        print(a)
        h1,h2 = a[0][0],a[0][1]
        ans = 1
        for x in a:
            if x[0] > h2:
                ans += 1
                h1,h2 = x[0],x[1]
        return ans


# Minimum Platforms
# TC : NlogN + NlogN
# SC: O(1)
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        i,j = 1,0
        platform,maxi = 1,1
        # If train arrives it takes a new platform.If train leaves it
        # vacant the platform that is platform becomes empty.
        while i < len(arr) and j < len(dep):
            # If arrival time is less than departure time that means train is
            # currently on the platfrom and platfrom is occupied already
            # so new platform is required for arrival so no. of platform increase and
            # we iterate forward
            if arr[i] <= dep[j]: # arrival time is less than departure time
                platform += 1
                i += 1
            # If departure time is less than arrival time that means train left the
            # platform and its available for arrival of new train on that 
            # platform hence no. platform used decreases.
            elif arr[i] > dep[j]: # arrival time greater than departure time
                platform -= 1
                j += 1
            # Store maximum number of platform used after every arrival or departure.
            maxi = max(platform,maxi)
        return maxi

# Job Sequencing Problem
# TC : O(NlogN + N*M) where M is maximum deadline among all sequencing
# SC : O(M)
# Approach : We have to think greedily and in order to maximize profit the first thing
# comes to my mind is to sort the sequencing according to maximum profit i.e sort in
# decreasing order
# After that we can sequence all job till its maximum deadline
# If some job has deadline 6, we can sequence it on any day that 1,2,3,4,5,6 day.But
# the idea is sequence any job on its last day that is last day of its deadline so that
# we can sequence any job having lesser deadline before it.
# AS we can not sequence two job at one the main idea to increase profit is to
# sequence very job to its last day of deadline.
# Eg if some job has deadline 4,so we can sequence it on 1,2,3,4 but we have to assign
# it on fourth day if that that day no job sequenced earlier.If any job sequence earlier
# we move to third day then second till 1 day.
class Solution:
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key = lambda x : x.profit,reverse = True)
        maxi = 0
        for i in range(n):
            if Jobs[i].deadline > maxi:
                maxi = Jobs[i].deadline
        res = [-1]*(maxi)
        countJobs,maxprofit = 0,0 
        # for i in range(n):
        #     print(Jobs[i].id)
        for i in range(n):
            for m in range(Jobs[i].deadline - 1,-1,-1):
                if res[m] == -1:
                    res[m] = Jobs[i].id
                    countJobs += 1
                    maxprofit += Jobs[i].profit
                    break;
        return [countJobs,maxprofit]


# Fractional Knapsack
# TC : O(NlogN  + N)
# SC : O(N)
# Approach : Sort the knapsack according to Value per weight i.e Value/weight
# If curr weight is less than knapsack capacity we will put that weight into
# knapsack update our new weight and its corresponding profit.
# if any time we exceed our knapsack that means we can't put that weight as whole
# but we can fraction the weight and fill the rest of the remaining knapsack.
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        a = []
        for i in range(n):
            a.append((Items[i].value,Items[i].weight))
        # print(a)
        a.sort(key = lambda x : x[0]/x[1],reverse = True)
        maxprofit,currweight = 0,0
        for i in range(n):
            if currweight + a[i][1] <= W:
                currweight += a[i][1]
                maxprofit += a[i][0]
            else:
                maxprofit += (W - currweight)*(a[i][0]/a[i][1])# W - currweight = capacity left in knapsack
                break;               # a[i][0]/a[i][1] # value per weight
        return maxprofit


# Subset Sum
# TC : O(2^N)
# SC : O(1)
class Solution:
    def subsetSums(self,arr, N):
        # code here
        def funct(idx,summ,arr,N,sumarr):
            if idx == N:
                sumarr.append(summ)
                return
            # Subset including arr[l]
            funct(idx + 1,summ + arr[idx],arr,N,sumarr)
             # Subset excluding arr[l]
            funct(idx,summ,arr,N,sumarr)
        sumarr = []
        self.funct(0,0,arr,N,sumarr)
        return sumarr.sort()

# Subset I : Using Recursion :
# TC : O(2^N)
# SC : O(2^N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def subs(idx,N,res):
            if idx == N:
                result.append(res)
                return
            subs(idx + 1,N,res)
            subs(idx + 1,N,res + [nums[idx]])
        subs(0,len(nums),[])
        return result

# Subset Sum II : Print all unique Subset when nums contains duplicate element
# TC : O(2^N + 2^N*log(2^N) for adding in set)
# SC : O(2^N + 2^N)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        s = []
        def subs(idx,N,res):
            if idx == N:
                result.append(res)
                return
            subs(idx + 1,N,res)
            subs(idx + 1,N,res + [nums[idx]])
        subs(0,len(nums),[])
        for i in result:
            if sorted(i) not in s:
                s.append(sorted(i))
        return s

# Method II :Without using set Using backtracking
# TC : O(n*2^n) : For every len of subset*TC(for recursion)
# SC : O(2^n)*O(k) + O(n) : 2^n subset + auxiliary space for depth of recursion 
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        listt = []
        nums.sort()
        def backtrack(idx):
            if len(listt) >= 1:
                res.append(listt[:])
            for i in range(idx,len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue;
                listt.append(nums[i])
                backtrack(i + 1)
                listt.pop()
        backtrack(0)
        return res


# Permutations
# TC : N*O(N!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        listt = []
        def backtrack():
            if len(listt) == len(nums):
                ans.append(listt.copy())
                return
            for i in nums:
                if i in listt:
                    continue;
                listt.append(i)
                backtrack()
                listt.pop()
        backtrack()
        return ans


# N-Queen Problem : 
# TC : O(N^N) :This means it will look through every position on an NxN board,
#                N times, for N queens.
# Step 1: Create set for all the three types of attacks Two diagonals and One Vertical attacks
# Step2: First diagonal is calculated by i+j and second diagonal j-i. If i+j or j-i is present
# in the set that means that particular diagonal is under attack.
# Step 3: If not under attack place the queen on board and add both the diagonals and vertical
# in the set which are under attack after placing that queen .
# Step 4: Now recurse for next row if at last we find that this solution is not valid we
# backtrack and pop all the value which we have filled earlier as that solution is not 
# valid now and place the queen in next row in next iteration.
# Step 5: After finding solution just add that configuration of board into new list and return it.
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for j in range(n)]for i in range(n)]
        diagonal1 = set()
        diagonal2 = set()
        vertical = set()
        res = []
        def addboard(board):
            l = []
            for row in board:
                t = "".join(row)
                l.append(str(t))
            res.append(l)
        def nqueen(board,row):
            if row == n:
                addboard(board)
                return
            for col in range(n):
                if (row + col) not in diagonal1 and (col - row) not in diagonal2 and col not in vertical:
                    board[row][col] = "Q"        # Placing the knight
                    diagonal1.add(row+col)
                    diagonal2.add(col - row)
                    vertical.add(col)
                    nqueen(board,row + 1)   # After placing recurse all option for next row keeping the 1st knight fixed
                    board[row][col] = "."     # After finding all options backtrack to get into previous state
                    diagonal1.remove(row+col)
                    diagonal2.remove(col - row)
                    vertical.remove(col)
        nqueen(board,0)
        return res


# Sudoku Problem
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isValid(row,col,nums,board):
            for i in range(0,9):
                if board[i][col] == nums:
                    return False
                if board[row][i] == nums:
                    return False
            startRow = (row // 3)*3
            startCol = (col // 3)*3
            for i in range(3):
                for j in range(3):
                    if board[i + startRow][j + startCol] == nums:
                        return False
            return True
        m = len(board)
        def sudoku(board):
            for row in range(m):
                for col in range(m):
                    if board[row][col] == '.':
                        for nums in range(1,10):
                            nums = str(nums)
                            if isValid(row,col,nums,board):
                                board[row][col] = nums
                                if sudoku(board) == True:
                                    return True
                                else:
                                    board[row][col] = '.'
                        return False
            return True
        sudoku(board)
                

# Method II : More Optimised
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def vacantpos(board):
            res = []
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        res.append((i, j))
            return res
        def isValid(row,col,nums,board):
            for i in range(0,9):
                if board[i][col] == nums:
                    return False
                if board[row][i] == nums:
                    return False
            startRow = (row // 3)*3
            startCol = (col // 3)*3
            for i in range(3):
                for j in range(3):
                    if board[i + startRow][j + startCol] == nums:
                        return False
            return True
        m = len(board)
        pos = vacantpos(board)
        def sudoku(board,pos):
            if len(pos) == 0:
                return True
            row,col = pos[0]
            for nums in range(1,10):
                nums = str(nums)
                if isValid(row,col,nums,board):
                    board[row][col] = nums
                    if sudoku(board,pos[1:]) == True:
                        return True
                    else:
                        board[row][col] = '.'
            return False
        sudoku(board,pos)



# M-Colour Problem :
    def graphColoring(graph, k, V):
        def isSafe(node,col,graph,color,m):
            for l in range(V):
                if graph[node][l] == 1 and color[l] == col:
                    return False
            return True
        def dfs(node,graph,color,m,V):
            if node == V:
                return True
            for i in range(1,m+1):
                if isSafe(node,i,graph,color,m) == True:
                    color[node] = i
                    if dfs(node + 1,graph,color,m,V) == True:
                        return True
                    color[node] = 0
            return False
        color = [0]*V
        if dfs(0,graph,color,k,V):
            return 1
        else:
            return 0


# Rat Maze Problem
class Solution:
    def findPath(self, m, n):
        direction = [[1,0],[0,-1],[0,1],[-1,0]]
        def isMove(i,j,m,n,vis,ans,move):
            if i == n - 1 and j == n - 1:
                ans.append(move)
                return
            strn = "DLRU"
            for idx in range(4):
                new_x = i + direction[idx][0]
                new_y = j + direction[idx][1]
                if new_x >= 0 and new_y >=0 and new_x <n and new_y < n and vis[new_x][new_y] == 0 and m[new_x][new_y] == 1:
                    vis[i][j] = 1
                    isMove(new_x,new_y,m,n,vis,ans,move + strn[idx])
                    vis[i][j] = 0
                
        ans = []
        vis = [[0 for j in range(n)]for i in range(n)]
        if m[0][0] == 1:
            isMove(0,0,m,n,vis,ans,"")
            return ans
        else:
            return []



def sumpath(root,summ,path):
    if root.left is None and root.right is None:
        if summ + root.data == target:
            ans.append(path + [root.val])
    sumpath(root.left,summ + root.data,path + [root.data])
    sumpath(root.right,summ + root.data,path + [root.data])


# Print K sum Path binary Tree
def printVector(v, i):
    for j in range(i, len(v)):
        print(v[j], end = " ")
    print()
def ksumpath(root,path,k):
    if root is None:
        return
    path.append(root.data)
    f = 0
    for i in range(len(path)-1,-1,-1):
        f += path[i]
        if f == k:
            printVector(path, j)
    ksumpath(root.left,path,k)
    ksumpath(root.right,path,k)
    path.pop(-1)


count,total = 0,0
right = [0]*len(a)
left = [0]*len(a)
for i in range(len(a)):
    if a[i] == 1:
        count = total
    elif a[i] == 0:
        total += 1
    right[i] = count
print(right,total)
count,total = 0,0
for i in range(len(a)-1,-1,-1):
    if a[i] == 1:
        count = total
    elif a[i] == 0:
        total += 1
    left[i] = count
print(left)
for i in range(2):
    L = m[i][0]
    R = m[i][1]
    count = left[L] + right[R] - total
    print(count)

# Max Triplet Product of An Array
# Brute Froce : O(N^3)
# Method II : Sorting
arr.sort()
return max(arr[-1]*arr[-2]*arr[-3],arr[-1]*arr[1]*arr[0])

# Method III : O(N)
max1,max2,max3 = float("-inf"),float("-inf"),float("-inf")
min1,min2 = float("inf"),float("inf")
for num in arr:
    if num >= max1:
        max3 = max2
        max2 = max1
        max1 = num
    elif num <= max1 and num >= max2:
        max3 = max2
        max2 = num
    elif num <= max2 and num >= max3:
        max3 = num
    if num <= min1:
        min2 = min1
        min1 = num
    elif num >= min1 and num <= min2:
        min2 = num
# print(max1,max2,max3,min1,min2)
return max(max1*max2*max3,min1*min2*max1)

