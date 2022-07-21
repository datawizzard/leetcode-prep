# Two Sum :
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for i,ele in enumerate(nums):
            if target - ele in idx:
                return [i,idx[target - ele]]
            idx[ele] = i
# Two sum code Link list
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

# Longest Substring without repeating character
# Method I: TC : O(N + N)
#               : SC : O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window Problem n
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
# method II:
# TC: O(N)
# SC : O(N)
def longestUniqueSubsttr(string):
      
    # Creating a map to store the last positions of occurrence
    seen = {}
    maximum_length = 0
  
    # starting the inital point of window to index 0
    start = 0
      
    for end in range(len(string)):
  
        # Checking if we have already seen the element or not
        if string[end] in seen:
 
            # If we have seen the number, move the start pointer
            # to position after the last occurrence
            start = max(start, seen[string[end]] + 1)
        # Updating the last seen value of the character
        seen[string[end]] = end
        maximum_length = max(maximum_length, end-start + 1)
    return maximum_length

# longest Palindromic substring 
# DP Solution
def longestPalindrome(self, s):
    longest_palindrom = ''
    dp = [[0]*len(s) for _ in range(len(s))]
    #filling out the diagonal by 1
    for i in range(len(s)):
        dp[i][i] = True
        longest_palindrom = s[i]
		
    # filling the dp table
    for i in range(len(s)-1,-1,-1):
			# j starts from the i location : to only work on the upper side of the diagonal 
        for j in range(i+1,len(s)):  
            if s[i] == s[j]:  #if the chars matches
                # if len slicied sub_string is just one letter if the characters are equal, we can say they are palindome dp[i][j] =True 
                #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                if j-i ==1 or dp[i+1][j-1] is True:
                    dp[i][j] = True
                    # we also need to keep track of the maximum palindrom sequence 
                    if len(longest_palindrom) < len(s[i:j+1]):
                        longest_palindrom = s[i:j+1]
            
    return longest_palindrom

	# Expanded by picking one and two point
	def longestPalindrome(self, s: str) -> str:
        def helper(s,l,r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        res = ""
        for i in range(len(s)):
            x = helper(s,i,i)
            y = helper(s,i,i+1)
            # print(len(res))
            if len(x) > len(res):
                res = x
            if len(y) > len(res):
                res = y
        return res


# Zig - Zag Conversion
# the idea is whenver we reaches the corner we reverse the direction which will
# automatically append character in right row
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        chararr = [[] for _ in range(numRows)]
        if numRows == 1 or numRows >= len(s):
            return s
        row = 0
        direction = -1
        for c in s:
            chararr[row].append(c)
            if row == 0 or row == numRows - 1:
                direction *= -1
            row += direction
        ans = ""
        for arr in chararr:
            ans += "".join(arr)

# String to atois
def myAtoi(self, s: str) -> int:
    s = s.strip()
    print(s)
    if not s:
        return 0
    res = 0
    negative = False
    if s[0] == '-':
        negative = True
    elif s[0] == '+':
        negative = False
    elif not s[0].isnumeric():
        return 0
    else:
        res = ord(s[0]) - ord('0')
    for i in range(1,len(s)):
        if s[i].isnumeric():
            res = res * 10 + ord(s[i]) - ord('0')
            print(res)
            if not negative and res >= 2**31 - 1:
                return 2**31 - 1
            if negative and res >= 2**31:
                return -2**31
        else:
            break;
    if negative:
        return -res
    else:
        return res

#3Sum
#Time Complexity : O(n^2)
#Space complexity : O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        t = set()
        print(nums)
        for i in range(len(nums)-2):
            left,right = i+1,len(nums) - 1
            #if condition for duplicate element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                summ = nums[left] + nums[right] + nums[i]
                if summ == 0:
                    t.add(tuple([nums[i],nums[left],nums[right]]))
                    left += 1
                    right -= 1
                elif summ > 0:
                    right -= 1
                else:
                    left += 1
        return [[p[0],p[1],p[2]] for p in t]

# Without Using set
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


# Letter combination of phone number
# Time complexity: O(3^N×4^M)
# SC : Same
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitarray = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
        }
        def phonenumber(i,currentstr):
            if len(digits) == len(currentstr):
                res.append(currentstr)
                return
            for c in digitarray[digits[i]]:
                phonenumber(i+1,currentstr + c)
        if digits:
            phonenumber(0,"")
        return res

# Valid Parenthesis
#Time complexity :O(n)
# Space complexity : O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                x = stack.pop()
                if x == '(' and s[i] != ')':
                    return False
                if x == '{' and s[i] != '}':
                    return False
                if x == '[' and s[i] != ']':
                    return False
        if stack:
            return False
        else:
            return True


# Merge Two Sorted Link List
# Time complexity : O(n) 
# Space Complexity : O(1)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        # If either of list left it will be appended at the end of sorted new link list
        curr.next = l1 or l2
        return dummy.next

 # Recursive Approach
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		if l1 is None:
			return l2
		elif l2 is None:
		    return l1
		if l1.val <= l2.val:
		    l1.next = self.mergeTwoLists(l1.next,l2)
		    return l1
		else:
		    l2.next = self.mergeTwoLists(l1,l2.next)
		    return l2

# Generate All possible valid Parenthesis 
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(opeN,closeD,curr,n,res):
            if len(curr) == 2*n:
                res.append(curr)
                return
            if opeN < n:
                helper(opeN + 1,closeD,curr + '(',n,res)
            if closeD < opeN:
                helper(opeN,closeD + 1,curr + ')',n,res)
        res = []
        helper(0,0,"",n,res)

# Using stack
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(openN,closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1,closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN,closedN + 1)
                stack.pop()
        backtrack(0,0)
        return res

# Merge K sorted Link list into one sorted link list
 # Time complexity : O(n*k)
 # Space Complexity : O(n)
class Solution:
    def mergesorted(self,lists : List[ListNode]) -> ListNode:
        dummy = ListNode()
        curr = dummy
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for x in sorted(nodes):
            curr.next = ListNode(x)
            curr = curr.next
        return dummy.next
 # Using heap method
 # Time complexity : O(N*log(k))
 # here comparison cost will be reduced to O(log k) O(logk) for every pop and
 # insertion to priority queue. But finding the node with the smallest value just costs O(1) time.
 # There are N nodes in the final linked list.
 # Space complexity : O(N)
# Using heap method
import heapq
 class Solution:
    def mergesorted(self,lists: List[ListNode]) -> ListNode:
        dummy = ListNode()
        curr = dummy
        q = []
        for idx,l in enumerate(lists):
            if l:
                q.append((l.val,idx))
        heapq.heapify(q)
        while q:
            val,idx = heapq.heappop(q)
            curr.next = lists[idx]
            curr = curr.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(q,(node.val,idx))
        return dummy.next
# Divide and conquer method
# Merge Two Sorted Arrays
def SortedMerge(a, b):
 
    dummy = ListNode()
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    # If either of list left it will be appended at the end of sorted new link list
    curr.next = l1 or l2
    return dummy.next
 
# The main function that takes an array of lists
# arr[0..last] and generates the sorted output
def mergeKLists(arr, last):
 
    # Repeat until only one list is left
    while (last != 0):
        i = 0
        j = last
  
        # (i, j) forms a pair
        while (i < j):
             
            # Merge List i with List j and store
            # merged list in List i
            arr[i] = SortedMerge(arr[i], arr[j])
  
            # Consider next pair
            i += 1
            j -= 1           
            # If all pairs are merged, update last
            if (i >= j):
                last = j
  
    return arr[0]


# Rain water Trapping
# Method 1 : Brute Force

    # Time complexity : O(N^2)
    # Space complexity : O(1)
    class Solution:
        def trap(self, height: List[int]) -> int:
            ans = 0
            n = len(height)
            for i in range(1,n-1):
                a = max(height[i::-1])
                b = max(height[i:])
                ans += min(a,b) - height[i]
            return ans
# Method 2: Using prefix Array Sum
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
                right[i] = max(right[i+1],height[i])
            for i in range(1,n-1):
                ans += min(left[i],right[i]) - height[i]
            return ans
# Method 3 : Two pointer Best Approach
    # Time Complexity : O(N)
    # Space complexity : O(1)
    class Solution:
        def trap(self, height: List[int]) -> int:
            if not height:
                return 0
            else:
                l,r = 0,len(height) - 1
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

# Permutation 

# Method I : Recursion
    # TC : O(N*N!)
    # SC : O(N!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(curr,nums):
            if len(curr) == len(nums):
                ans.append(curr)
                return 
            for i in nums:
                if i not in curr:
                    helper(curr + [i],nums)
            helper([],nums)
            return ans
 # Method II:
  # Time Complexity : O(N*N!)
  # Space Compolexity: O(N!)
  class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        listt = []
        def backtrack():
            if len(listt) == len(nums):
                ans.append(listt.copy())
            for i in nums:
                if i in listt:
                    continue:
                listt.append(i)
                backtrack()
                listt.pop()
        backtrack()
        return ans

    # Method III: 
    # By swapping the the element
    def helper(idx,nums):
        if idx == len(nums):
            ans.append(nums.copy())
            return 
        for i in range(idx,len(nums)):
            nums[i],nums[idx] = nums[idx],nums[i]
            helper(idx + 1,nums)
            nums[i],nums[idx] = nums[idx],nums[i]
    ans = []
    helper(0,nums)
    return ans

# Permutation 2 : Contains duplicate element
  # Time complexity : O(N!/(N-K)!)
  # Space complexity : O(N!)
    from collections import Counter
    def permute(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        ans = []
        listt = []
        def backtrack():
            if len(listt) == len(nums):
                ans.append(listt.copy())
            for i in c:
                if c[i] > 0:
                    listt.append(i)
                    c[i] -= 1
                    backtrack()
                    listt.pop()
                    c[i] += 1
        backtrack()
        return ans


# Rotating the matrix
# Time Complexity : O(M) : 
 # We perform two steps; transposing the matrix, and then reversing each row.
 # Transposing the matrix has a cost of O(M) because we're moving the
 # value of each cell once. Reversing each row also has a cost of O(M), 
 #because again we're moving the value of each cell once.
# Space Complexity : O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(i,n):
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
        for i in range(m):
            matrix[i] = matrix[i][::-1]

# Group of Anagrams
 # Time Complexity : O(NMlogM) : Where M is length of largest word
 # Space complexity : O(N)
     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for num in strs:
            x = "".join(sorted(num))
            d[x].append(num)
        return list(d.values())

# Merge Intervals
# Time Complexity : O(NlogN)
# Space complexity :O(N)

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        print(intervals)
        a = []
        l = intervals[0][0]
        h = intervals[0][1]
        for arr in intervals:
            if arr[0] > h:
                a.append([l,h])
                l,h = arr[0],arr[1]
            else:
                h = max(h,arr[1])
        a.append([l,h])
        return a


#  Spiral Matrix III
 # Time Complexity : O(N*N)
  # Space complexity : O(N*N)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0 for i in range(n)] for j in range(n)]
        count = 1
        top,down,left,right= 0,n-1,0,n-1
        direction = 0
        while top <= down and left <= right:
            if direction == 0:
                for i in range(left,right+1):
                    m[top][i] = count
                    count += 1
                top += 1
            elif direction == 1:
                for i in range(top,down+1):
                    print(i,right-1,count)
                    m[i][right] = count
                    count += 1
                right -= 1
            elif direction == 2:
                for i in range(right,left-1,-1):
                    m[down][i] = count
                    count += 1
                down -= 1
            else:
                for i in range(down,top-1,-1):
                    m[i][left] = count 
                    count += 1
                left += 1
            direction = (direction + 1) % 4
        return m

# Unique Path III
 # Time Complexity : O(N*N)
 # Space Complexity : O(N*N)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)]for i in range(m)]
        for i in range(0,m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break;
        for i in range(0,n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break;
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

# Minimum Path Sum
 # TC : O(N*N)
 # SC : O(N*N)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for j in range(n)]for i in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1,n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]


# Edit Distance
  # Method I : Recursive
 # TC : O(3^n + 3^m)
 # SC : O(1)
 class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        def mindis(word1,word2,m,n):
            if n == 0:
                return m
            if m == 0:
                return n
            if word1[m-1] == word2[n-1]:
                return mindis(word1,word2,m-1,n-1)
            else:
                return 1 + min(mindis(word1,word2,m,n-1),mindis(word1,word2,m-1,n),mindis(word1,word2,m-1,n-1))
        return mindis(word1,word2,m,n)
 # Method II: Bottom Up 
  # TC : O(m*n)
  # SC : O(m*n)
 class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for j in range(n + 1)]for i in range(m + 1)]
        for i in range(m+ 1):
            for j in range(n + 1):
                # If first string is empty, only option is to
            # insert all characters of second string
                if i == 0:
                    dp[i][j] = j
                # If second string is empty, only option is to
            # remove all characters of second string
                elif j == 0:
                    dp[i][j] = i
                # If second string is empty, only option is to
            # remove all characters of second string
                elif word1[i-1] = word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # If last character are different, consider all
            # possibilities and find minimum
                else:
                    dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
        return dp[m][n]

 # Method III :
  # TC : O(m*n)
  # SC : O(2*m)
  def EditDistDP(str1, str2):
     
    len1 = len(str1)
    len2 = len(str2)
 
    # Create a DP array to memoize result
    # of previous computations
    DP = [[0 for i in range(len1 + 1)]
             for j in range(2)];
 
    # Base condition when second String
    # is empty then we remove all characters
    for i in range(0, len1 + 1):
        DP[0][i] = i
 
    # Start filling the DP
    # This loop run for every
    # character in second String
    for i in range(1, len2 + 1):
         
        # This loop compares the char from
        # second String with first String
        # characters
        for j in range(0, len1 + 1):
 
            # If first String is empty then
            # we have to perform add character
            # operation to get second String
            if (j == 0):
                DP[i % 2][j] = i
 
            # If character from both String
            # is same then we do not perform any
            # operation . here i % 2 is for bound
            # the row number.
            elif(str1[j - 1] == str2[i-1]):
                DP[i % 2][j] = DP[(i - 1) % 2][j - 1]
             
            # If character from both String is
            # not same then we take the minimum
            # from three specified operation
            else:
                DP[i % 2][j] = (1 + min(DP[(i - 1) % 2][j],
                                    min(DP[i % 2][j - 1],
                                  DP[(i - 1) % 2][j - 1])))
             
    # After complete fill the DP array
    # if the len2 is even then we end
    # up in the 0th row else we end up
    # in the 1th row so we take len2 % 2
    # to get row
    print(DP[len2 % 2][len1], "")


# Set Matrix Zeroes
 # TC : O(M*N)
 # SC : O(M + N)
 class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        row = []
        col = []
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        # print(row)
        # print(col)
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0
        print(matrix)
 

 # Space optimised : O(1) : Take u forward
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

# Sort Colors:
 # Brute Force : Sort the array : TC : O(nlogN)
 # SC : O(1)
    return nums.sort()
    # TC : O(n + n)
    # SC : O(n)
    # Bucket Sort
    from collections import Counter
        cnt = Counter(nums)
        j = 0
        for i in range(0,3):
            while cnt[i] > 0:
                nums[j] = i
                j += 1
                cnt[i] -= 1
        return nums

    # One pass sol : O(N)
    # SC : O(1)
    # Dutch National Flag Algorithm
    # All the element from [0..to low - 1] will be 0
    # All element between [low... to mid - 1] wiil be 1
    # All the element from [high + 1... end] will be 2
    low,mid,high = 0,0,len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high -= 1
    return nums



# Minimum Window Substring

# Brute Force
 class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        res = ""
        wsize = 99999
        for i in range(len(s)):
            for j in range(i,len(s)):
                window = s[i:j+1]
                if iscontain(window,t):
                    if len(window) < wsize:
                        wsize = len(window)
                        res = window
        return res
    def iscontain(w,t):
        c = Counter(w)
        d = Counter(t)
        flag = 0
        for x in d:
            if x in c and d[x] <= c[x]:
                flag = 1
            else:
                flag = 0
                break;
        if flag == 1:
            return True
        else:
            return False

 # Method II : Sliding Window Technique
  # TC : O(S + T) : O(len(s) + len(t))
  # SC : O(S + T)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r = 0,0
        freqs = defaultdict(int)
        freqt = Counter(t)
        count = 0
        window = ""
        mini = float('inf')
        while r < len(s):
            freqs[s[r]] += 1 # Adding element in window
            if s[r] in freqt and freqs[s[r]] <= freqt[s[r]]:# If window contain char which present in t increase
                count += 1             # the count.Count will store number of char we need such that window contain all element present in t.
            while l <= r and count == len(t):   # Decrease the window size from left till all element of t   
                if r - l + 1 < mini:    # present in curr window and store the minimum window size
                    mini = r - l + 1
                    window = s[l : r + 1]
                freqs[s[l]] -= 1    
                if s[l] in freqt and freqs[s[l]] < freqt[s[l]]: # While removing window size from left if 
                    count -= 1     # all char are not present in window we decrease the count as all element
                l += 1             # are not present.
            r += 1
        return window

# Subset : PowerSet
 # TC : O(N * 2^N)
 # SC : O(N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx,listt):
            if len(listt) >= 0:
                res.append(listt[:])
            for i in range(idx,len(nums)):
                listt.append(nums[i])
                backtrack(i + 1,listt)
                listt.pop()
        backtrack(0,[])
        return res

# Validate if a tree is a binary Search Tree
 # TC : O(N)
 # SC : O(log(N)) : To Store the value in recursion stack
class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        return self.isValidNode(root,float('-inf'), float('inf'))
    def isValidNode(self, root, l, r):
        if not root:
            return True
        return l < root.val < r and self.isValidNode(root.left, l, root.val)
                                 and self.isValidNode(root.right, root.val, r)

 # Method II:
 class Solution:
    def isValid(root):
        result = []
        def inorder(root,result):
            if root:
                inorder(root.left,result)
                result.append(root.val)
                inorder(root.right,result)
        inorder(root,result)
    return sorted(list(set(result))) == result

# Same Tree
 #TC : O(N)
 #SC : O(log(N))
 class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if q is None or p is None:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

# Level Order Traversal(Same as Breadth first search)
# TC : O(N) : For traversing each node
# SC : O(N)
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        q = []
        res = []
        q.append(root)
        while q:
             # nodeCount (queue size) indicates number
        # of nodes at current level.
            count = len(q)
            listt = []
            # Dequeue all nodes of current level and
        # Enqueue all nodes of next level
            while count > 0:
                x = q.pop(0)
                listt.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
                count -= 1
            res.append(listt)
        return res

# Method II :



# Path Sum II 
 # TC : O(N)
 # SC : O(N)
 # Method I : Using Stack
 class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root is None:
            return
        res = []
        stack = [(root,0,[])]
        while stack:
            node,currsum,path = stack.pop()
            if currsum + node.val == targetSum and node.left is None and node.right is None:
                res.append(path + [node.val])
            if node.left:
                stack.append([node.left,currsum + node.val,path + [node.val]])
            if node.right:
                stack.append([node.right,currsum + node.val,path + [node.val]])
        return res

# Method II : Using recursion
 class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:      
        paths = []
        def helper(node, total, path):
            if node:
                if not node.left and not node.right:
                    if total + node.val == sum:
                        paths.append(path+[node.val])
                helper(node.left, total + node.val, path + [node.val])
                helper(node.right, total + node.val, path + [node.val])
        helper(root, 0, [])
        return paths
# Path Sum I:
 # TC : O(N)
 # SC : O(N)
 class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
         def helper(node, total):
            if node:
                if not node.left and not node.right:
                    if total + node.val == targetSum:
                        return True
                return helper(node.left, total + node.val) or helper(node.right, total + node.val)
        return helper(root, 0)
 # Path Sum III:
 # TC : O(N^2)
 # SC : O(N)
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.pathSum_dfs(root,[],sum)
        
    def pathSum_dfs(self,node,path,sum):
        if not node:
            return 0
        
        path.append(node.val)
        count = 0
        cur_sum = 0
        print(path)
        for i in range(len(path)-1,-1,-1):
            cur_sum += path[i]
            if cur_sum == sum:
                count += 1
            
        count += self.pathSum_dfs(node.left,path,sum)
        count += self.pathSum_dfs(node.right,path,sum)
        path.pop()
        return count
# Method II
 # TC : O(N)
 # SC : O(N)
 class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.ans = 0
        
        prefix_sum = collections.defaultdict(int)  # sum -> freq
        prefix_sum[0] = 1
        running_sum = 0
        
        def dfs(node, running_sum):
            if not node:
                return
            
            running_sum += node.val
            required_sum = running_sum - target
            
            if required_sum in prefix_sum:
                self.ans += prefix_sum[required_sum]
                
            # update prefix sum map
            prefix_sum[running_sum] += 1
            
            # follow left path from here
            dfs(node.left, running_sum)
            
            # follow right path from here
            dfs(node.right, running_sum)
            
            # backtrack, done with all the paths containing this node.
            prefix_sum[running_sum] -= 1
            
        dfs(root, 0)
        return self.ans

# Pascal Triangle
 # Method I:
 # TC : O(N)
 # SC : O(N)
 # derived from these two equations
#  C(line, i)   = line! / ( (line-i)! * i! )
# C(line, i-1) = line! / ( (line - i + 1)! * (i-1)! )
# We can derive following expression from above two expressions.
# C(line, i) = C(line, i-1) * (line - i + 1) / i

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        C = [1] * (rowIndex + 1)
        for i in range(rowIndex):
            C[i+1] = (C[i] * (rowIndex-i)) // (i+1)  
        return C
#Method II:
# TC :O(N^2)
# SC :O(N^2)
dp = [[1]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
print(dp)
return dp[-1]


# Best Time to buy sell stocks
# TC : O(N)
# SC : O(1)

minprices,maxprofit = float('inf'),0
for i in range(len(prices)):
    if prices[i] < minprices:
        minprices = prices[i]
    elif prices[i] - minprices > maxprofit:
        maxprofit = prices[i] - minprices
return maxprofit



# Sum Root to Leaf Number
# TC : O(N)
# SC : O(log(N))
class Solution:
    # Method I : Recursive dfs 
    def dfs(self,root,v,sumlist):
        if root is None:
            return
        if root.left is None and root.right is None:
            v = v * 10 + root.val
            sumlist.append(v)
        else:
            self.dfs(root.left,v*10+root.val,sumlist)
            self.dfs(root.right,v*10+root.val,sumlist)
    def sumNumbers(self, root: TreeNode) -> int:
        sumlist = []
        self.dfs(root,0,sumlist)
        return sum(sumlist)
    # Iterative BFS
        total_sum = 0
        q = [(root,0)]
        while q:
            node,prevsum = q.pop()
            currsum = prevsum*10 + node.val
            if node.left is None and node.right is None:
                total_sum += currsum
                continue;
            if node.left:
                q.append((node.left,currsum))
            if node.right:
                q.append((node.right,currsum))
        return total_sum
            

# Clone Linked list with random pointer
# TC : O(N + N): as we have to traverse every node twice
# SC : O(N): Due to creation of hasmap of size N
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        oldcopy = {None:None}
        curr = head
        # Making new node and  mapping old copy with corresponding new copy
        while curr:
            copy = Node(curr.val)
            #mapped current node with its new copy
            oldcopy[curr] = copy
            curr = curr.next
        curr = head
        # Connecting the new nodes
        while curr:
            copy = oldcopy[curr]
            copy.next = oldcopy[curr.next]
            copy.random = oldcopy[curr.random]
            curr = curr.next
        return oldcopy[head]

# Optimised Space complexity:
# TC :O(N)
# SC :O(1)
 # This is done in three steps
 # First step
 curr = head
 front = head
 # Step I : Creating deep copy node and connect with its original node
 while curr:
    front = curr.next
    copy = Node(curr.val) 
    curr.next = copy
    copy.next = front
    curr = front
 # Step II : Point deep copy random pointer with their corresponding given node
 curr = head
 while curr:
    if curr.random:
        curr.next.random = curr.random.next
    curr = curr.next.next
# Step III: Break the link between original node and deep copy node and join the deep copy node
dummy = Node(0)
copy = dummy
curr = head
while curr:
    front = curr.next.next
    copy.next = curr.next
    curr.next = front
    copy = copy.next
    curr = curr.next
return dummy.next


# Word Break :
 # Method I : Recursion
 # Brute Force
 # TC : O(n^n) :  Because there are n^n combinations in The Worst Case.
 # SC : O(n^2) : Because of the Recursive Stack of wordBreakUtil(…) function in The Worst Case.

 class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == "":
            return True
        else:
            l = len(s)
            for i in range(1,l+1):
                if s[:i] in wordDict and self.wordBreak(s[i:],wordDict):
                    return True
        return False 
# Method  II : Memoized
        d = {}
        def helper(s):
            if s == "":
                return True
            if s in d:
                return d[s]
            l = len(s)
            for i in range(1,l+1):
                if s[:i] in wordDict and helper(s[i:]):
                    d[s] = True
                    return True
            d[s] = False
            return False
        x = helper(s)
        return x
    # Method III : Using Dp
    # TC : O(N^3)
    # SC : O(N^2)
    dp=[False]*(len(s)+1)
    dp[0]=True # dp[0] is True because if we do partition at 0 idx string before it is empty
                # and its always True as it is always present in dictionary.
    for i in range(1,len(s)+1): # i corresponds to number of partition in a string
        for j in range(i):  # for every partition we check whether previous is correct and after
                            # partition till j to i if str is also correct then till i, our ans
                            # is True.
            if dp[j] and s[j:i] in wordDict:
                dp[i]=True
                break
    return dp[len(s)]


# Detect Loop in Link List
 # Method I : Hashing Approach
  # SC : O(N)
  # TC : O(N)
  class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        while head:
            if head in s:
                return True
            else:
                s.add(head)
            head = head.next
        return False

 # Method II : Flyod Cycle Finding Algorithm
  # TC : O(N)
  # SC : O(1)
  class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow_ptr = head
        fast_ptr = head
        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
        return False
 # Method III: Mathematical Trick
 # TC : O(N)
 # SC : O(1)
 class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        count = 0
        while head:
            count += 1
            if count > 1000:
                return True
        return False


# Sort Link List
 # Method I : Using heap
 # TC : O(NlogN)
 # SC : O(N)
import heapq
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        heapy = []
        heapq.heapify(heapy)
        while head:
            heapq.heappush(heapy,head.val)
            head = head.next
        dummy = ListNode(0)
        curr = dummy
        while heapy:
            val = heapq.heappop(heapy)
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next


# Method II : Using Merge Sort 
 # TC : O(NlogN)
 # SC : O(1)
class Solution:
    def getMid(self,head):
        slow_ptr = fast_ptr = head
        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr
    def merge(self,l1,l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
    def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        mid = self.getMid(head)
        midnext = mid.next
        mid.next = None
        print(mid)
        left = self.sortList(head)
        right = self.sortList(midnext)
        return self.merge(left,right)


# Intersection of Link List:
 # Method I : Brute Force
 # TC : O(N^2)
 # SC : O(1)
 class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        while headA:
            temp = headB
            while temp:
                if headA == temp:
                    return headA
                temp = temp.next
            headA = headA.next
        return None
# Method II :
 # Optimisation using extra space
 # TC : O(N)
 # SC : O(N)
 class Solution:
    def getIntersectionNode(self,headA : ListNode,headB : ListNode) -> ListNode:
        vis = set()
        while headA:
            vis.add(headA)
            headA = headA.next
        while headB:
            if headB in vis:
                return headB
            headB = headB.next
        return None
# Method III : 
# TC : O(N)
# SC : O(1)
    def getlength(head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l
    l1 = getlength(headA)
    l2 = getlength(headB)
    if l1 < l2:
        headA,headB = headB,headA
        l1,l2 = l2,l1
    diff = l1 - l2
    while diff:
        headA = headA.next
        diff -= 1
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None

# Two Sum II :
 # Method I : Using two pointer
 # TC : O(N)
 # SC : O(1)
 class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0,len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1,j+1]
 # Method II : Using brute force
 # Using two loops
 # TC : O(N^2)
 # SC : O(1)
 for i in range(0,n-1):
    for j in range(i+1,n):
        if a[i] + a[j] == target:
            return [i+1,j+1]


# Rotate Array :
 # MEthod I : Brute force
 # TC : O(N*k)
 # SC : O(1)
 class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        for i in range(k):
            prev = nums[-1]
            for j in range(len(nums)):
                nums[j],prev = prev,nums[j]
 # Method II : Using extra space
  # TC : O(N)
  # SC : O(N)
        n = len(nums)
        a = [0]*len(n)
        for i in range(n):
            a[(i+k)%n] = nums[i]
        nums[:] = a
 # Method III:
        # TC : O(N)
        # SC : O(1)
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k :] + nums[: n - k]

# Method IV:
  # TC : O(N)
  # SC : O(1)
    def reverse(start,end,nums):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1
    k = k % len(nums)
    reverse(0,len(nums),nums)
    reverse(0,k-1,nums)
    reverse(k,len(nums),nums)


# Print right view of tree
# Method I : Using bfs (same as level order traversal just finding last value at every level )
 class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return None
        q = []
        listt = []
        q.append(root)
        while q:
            n = len(q)
            while n > 0:
                n -= 1
                x = q.pop(0)
                if n == 0:
                    listt.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        return listt
        # Method II : Using dfs
         # TC : O(N)
         # SC : O(N)
        hashMap = {}
        stack = [(root,0)]
        while stack:
            node, level = stack.pop()
            # Keep Updating the rightmost node at every level
            hashMap[level] = node.val
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        # At the end our hashMap will only have the
        # rightmost value at every level 
        return list(hashMap.values())


# Number of islands 
 # TC : O(number of row X number of column in grid)
 # Sc : O(1)
 class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(grid,i,j,m,n)
                    count += 1
        return count
    def dfs(self,grid,i,j,m,n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != "1":
            return
        grid[i][j] = "$"
        self.dfs(grid,i-1,j,m,n)
        self.dfs(grid,i,j-1,m,n)
        self.dfs(grid,i+1,j,m,n)
        self.dfs(grid,i,j+1,m,n)


# Happy Number 
 # method I : 
 # SC : O(1)
 # TC : O(1)
 class Solution:
    def happy(self,n):
        s = 0
        while n > 0:
            s += (n % 10)*(n % 10)
            n = n // 10
        return s
    def isHappy(self, n: int) -> bool:
        res = n
        while res != 1 and res != 4:
            res = self.happy(res)
        if res == 1:
            return True
        elif res == 4:
            return False


 # Method II : Using extra space
 class Solution:
    def happy(self,n):
        s = 0
        while n > 0:
            s += (n % 10)*(n % 10)
            n = n // 10
        return s
    s = set()
    def isHappy(self,n :int) -> bool:
        while True:
            n = happy(n):
            if n == 1:
                return True
            elif n in t:
                return False
            s.add(n)

# Count Primes
 # TC : O(N*log(log(N)))
 # SC : O(N)
 # How TC is this?
#    On taking n common from the above equation, the above equation can be rewritten as:
# n*(1/2 + 1/3 + 1/5 + 1/7 ...... p)

# It can be proved as below with the help of Harmonic Progression of the sum of primes:
# (1/2 + 1/3 + 1/5 + 1/7 ...... p) = log(log(n))
# Hence it is n*(log(log(n)))
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        prime = [True for i in range(n)]
        p = 2
        while (p * p <= n):

            # If prime[p] is not
            # changed, then it is a prime
            if (prime[p] == True):

                # Update all multiples of p
                for i in range(p * p, n, p):
                    prime[i] = False
            p += 1
        count = 0
        # Print all prime numbers
        # print(prime)
        for p in range(2, n):
            if prime[p]:
                count += 1
        return count


# Reversing a link list
 # TC : O(N)
 # SC : O(1)
 class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        while current:
            nextnode = current.next
            current.next = prev
            prev = current
            current = nextnode
    head = prev
    return head

# Kth Largest Element
# Method I : Brute Force
# TC : O(nlogn)
# SC : O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums:
            nums.sort(reverse = True)
            return nums[k-1]
        else:
            return None
#  Method II 
# TC : O(N + KlogN)
# SC : O(N)
        import heapq
        if nums:
            heapy = []
            heapq.heapify(heapy)
            for i in nums:
                heapq.heappush(heapy,i)
            j = 0
            while heapy:
                x = heapq.heappop(heapy)
                if j == len(nums) - k:
                    return x
                j +=1
        else:
            return None

# Method III : 
class Solution:
    def findKthLargest(self, nums, k):
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]    
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]


# Palindromic Link List
 # Method I : Using stack
 # TC : O(N + N)
 # SC : O(N)
 class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next
        while head:
            if head.val != stack.pop():
                return False
            head = head.next
        return True
 # Method II : By reversing the first half of the link list(Most efficient)
  # TC : O(N)
  # SC : O(N)
  def isPalindromic(self,head : ListNode) -> bool:
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

# LowestCommon Ancestor of Binary Search Tree
# TC : For Binary Search tree it has two Worst case time complexity i.e minimum and maximum.
# When the BST is balanced then the minimum worst-case time complexity is considered
# and that is O(LogN) i.e height of tree. When BST is skewed then maximum worst-case time 
# complexity is considered O(N) as height will be equal to number of nodes in tree
 # method I : Using property of binary search tree
  # left subtree is less than equal to parent node 
  # right subtree is greater than equal to parent node
  # each subsequent node follows above two property except leaf nodes
  class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        # If both p and q are greater than parent node  it means ancestor always 
        # exist in right subtree
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right,p,q)
        # If both p and q are less than parent node  it means ancestor always 
        # exist in left subtree
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            # we find the ancestor  here 
            return root
    # Method II : Iteratively
    # TC : O(N)
    # SC : O(1)
    class Solution:
        def lowestCommonAncestor(self,root : 'TreeNode', p : 'TreeNode' , q : 'TreeNode') -> 'TreeNode':
            while node:
            # Value of current node or parent node.
                parent_val = node.val

                if p.val > parent_val and q.val > parent_val:    
                    # If both p and q are greater than parent
                    node = node.right
                elif p.val < parent_val and q.val < parent_val:
                    # If both p and q are lesser than parent
                    node = node.left
                else:
                    # We have found the split point, i.e. the LCA node.
                    return node


# Lowest Common Ancestor of binary tree
 # Time Complexity: O(N), where N is the number of nodes 
 # in the BST. In the worst case we might be visiting all the nodes of the BST.

# Space Complexity: O(N). This is because the maximum amount of space
 # utilized by the recursion stack would be N since the height of a skewed 
 # BST could be N.
class Solution:
    def lowestcommonancestor(self,root : 'TreeNode',p : 'TreeNode' , q : 'TreeNode') -> 'TreeNode':
        # Tushar Roy Explanation
        if not root:
            return None
        # If current node is either p or q return that node
        if root.val == p or root.val == q:
            return root
        # or check subusequent left and right node recursively
        # If both of them return True i.e both of them is not null 
        # that means both the substree from the given node contains 
        # p and q so that node is least ancentor node
        left = lowestcommonancestor(root.left,p,q)
        right = lowestcommonancestor(root.right,p,q)
        # If both left and right returns not null that means we found both p and q and will
        # return its root
        if left != None and right != None:
            return root
        # If anyone of them return something and other is null
        # we return whichever of them is true
        else:
            return left or right

        # Method III :
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        leftsubtree = self.lowestCommonAncestor(root.left,p,q)
        rightsubtree = self.lowestCommonAncestor(root.right,p,q)
        if leftsubtree is None:
            return rightsubtree
        if rightsubtree is None:
            return leftsubtree
        if leftsubtree and rightsubtree:
            return root

# Product of array itself
 # Method I : Brute Force
 # TC : O(N^2)
 # SC : O(N)
 class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue;
                prod = prod*nums[j]
            ans.append(prod)
        return ans
            

# Method II: Using division operator
 # TC : O(2N)
 # SC : O(1)
        prod = 1
        countzero = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                countzero +=1
            else:
                prod *= nums[i]
        for i in range(n):
            if countzero == 0:
                nums[i] = prod//nums[i]
            elif countzero == 1:
                if nums[i] == 0:
                    nums[i] = prod
                else:
                    nums[i] = 0
            else:
                nums[i] = 0
        return nums

 # Method III: using prefix sum
 # TC : O(N)
 # SC : O(N)
        ret = [1] * len(nums)
        # Store the cumulative product
        cumprod = 1
        
        # Iterate over nums
        for i in range(len(nums)):
            ret[i] = cumprod
            cumprod = nums[i] * cumprod
            
        cumprod = 1
            
        for i in range(len(nums) -1, -1, -1):
            ret[i] *= cumprod
            cumprod = nums[i] * cumprod
            
        return ret


# Sliding window maximum
#  Method I : Brute Force
# TC : O(N^2)
# SC : O(1)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        n = len(nums)
        a = []
        while i <= n - k:
            a.append(max(nums[i:i+k]))
            i += 1
        return a

# Method II : using deque
 # TC : O(N) : Insertion and deletion cost is O(1) in deque hence complexity is O(N)
 # Sc : O(N) : For storing dequeue element
        n = len(nums)
        q = deque()
        res = []
        left = right = 0
        while right < n:
            # For every element, the previous
            # smaller elements are useless
            # so remove them from Qi
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            # Add new element at rear of queue
            q.append(right)
            # Remove the elements which are
            # out of this window
            if left > q[0]:
                # remove from front of deque
                q.popleft()
            # If window size is k the element at the front of the
            # queue is the largest element of
            # previous window, so print it and slide the window
            if right + 1 >= k:
                res.append(nums[q[0]])
                left += 1
            # print(q,left,q[0],nums[q[0]])
            right += 1
        return res



# Search a 2D matrix
 # Method I : 
 # TC : O(nlog(m))
 # SC : O(1)
 class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(row,target):
            low,high = 0,len(matrix[0])-1
            while low <= high:
                mid = (low + high)//2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    high = mid -1
                else:
                    low = mid + 1
            return False
        for row in matrix:
            if binary(row,target):
                return True

    # Method II : Saddlebacksearch
     # TC : O(N)
     # SC : O(1)
    row,col = 0,len(matrix[0]) - 1
    while row < len(matrix) and col >=0:
        if matrix[row][col] == target:
            return True
        if matrix[row][col] > target:
            col -=1
        else:
            row += 1
    return False

# Valid Anagrams
# TC : O(N)
# SC : O(1)
# Method I : using dictionary
if Counter(s) == Counter(t):
    return True
else:
    return False
# Method II : sorting
# TC : O(NlogN)
# SC : O(1)
if sorted(s) == sorted(t):
    return True
else:
    return False

        
# Find median from data stream
# Brute Force : Insertion Sort
 # TC: O(N^2) : N-for inserting num in in array in sorted for every N element
 # SC : O(1)
 def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        if len(self.arr) == 0:
            self.arr.append(num)
            return
        self.arr.append(num)
        j = len(self.arr)-2
        while j >= 0 and num < self.arr[j] :
                self.arr[j + 1] = self.arr[j]
                j -= 1
        self.arr[j + 1] = num
        
    def findMedian(self) -> float:
        if len(self.arr) % 2 == 0:
            return (self.arr[len(self.arr)//2] + self.arr[(len(self.arr)//2 )-1]) / 2
        else:
            return self.arr[len(self.arr)//2]

# Method II :
class MedianFinder:

    def __init__(self):
        # Small is Max Heap
        # Large is Min Heap
        self.small,self.large = [],[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        # make sure every num in small is <= every num in large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        # uneven size
        # If size of max heap is greater than size of min heap more than 1,
        # then pop the max element from max heap and push it into min heap i.e into large array
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        # If size of min heap is greater than size of max heap with more than 1,
        # then pop the min element from min heap and push it into max heap i.e into small array
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-1 * val)
        
            

    def findMedian(self) -> float:
        # If min heap length > max heap length then it means length is odd,hence return 
        # minimum of min heap i.e first element of min heap which is root node of min heap
        if len(self.large) > len(self.small):
            return self.large[0]
        # If max heap length > min heap length then it means length is odd,hence return 
        # maximum of max heap i.e first element of max heap which is root node of max heap
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        # else if both of them are equal i.e length is even,then return average
        # of min heap + max heap(min heap root always contain smallest of second part) & 
        # max heap root always contain maximum of 1st part which is gives correct median
        return (-1 * self.small[0] + self.large[0]) / 2


# Top K frequent elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Method I : Using counter 
        # TC : O(NlogN)
        # SC : O(N)
        c = Counter(nums)
        return sorted(c,key = c.get,reverse = True)[:k]
        # Method II : Using bucket
        # TC : O(N) 
        # SC : O(N)
        bucket = [[] for _ in range(len(nums) + 1)]
        c = Counter(nums).items()
        print(c)
        for num,freq in c:
            bucket[freq].append(num)
        flat_list = []
        for item in bucket:
            for j in item:
                flat_list.append(j)
        # print(flat_list)
        return flat_list[::-1][:k]
        # Method III : Using heap 
        # TC : O(Nlogk) if K < N else O(N) if K = N
        # SC : O(N + k)
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(klogd+ d) time where d  is count of number of distinct element.
        return heapq.nlargest(k, count.keys(), key=count.get) 


# First Unique character in a String
# Method I : Using dictionary
 # TC :O(N)
 # SC :O(N)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i,j in enumerate(s):
            if c[j] == 1:
                return  i
        return -1


# Rotate Function 
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # Method I : Brute Force
        res = []
        n = len(nums)
        k ,s= 0,0
        while k < n:
            s = 0
            for i in range(n):
                s += i * nums[i]
            k += 1
            nums = nums[-1:] + nums[:n - 1]
            # print(nums)
            res.append(s)
        return max(res)

    # Method II : Using Math
#       f(i)          = 0 * A[0] + 1 * A[1] + 2 * A[2] + .... +  (k-1) * A[k-1] + k * A[k]
#   f(i+1)        = 1 * A[0] + 2 * A[1] + 3 * A[2] + ...  +     k  * A[k-1] + 0 * A[k] 
# =>f(i+1) - f(i) =     A[0]   +   A[1]   +   A[2] + ...  +       A[k-1]    - k * A[k] 
#    = (A[0]   +   A[1]   +   A[2] + ...  +       A[k-1] +  A[k]) - (k+1) * A[k]
#    = sum(Array) - A[k] * array.length
# => f(i+1) = f(i) + sum(Array) -  last element * array.length
        r = curr = sum(i * j for i,j in enumerate(A))
        s = sum(A)
        k = len(A)
        while A:
            curr += s - A.pop() * k
            r = max(curr, r)
        return r

# Third Maximum Number
 class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Method I : Using heap
        # TC : O(klogN + N)
        # SC : O(N + N)
        nums = set(nums)
        if len(nums) <= 2:
            return max(nums)
        else:
            heap = []
            for i in nums:
                heapq.heappush(heap,-i)
            # print(heap)
            j = 0
            while heap and j != 3:
                x = heapq.heappop(heap)
                j += 1
            return -1 * x
        # Method II: Sorting 
         #  TC : O(nlogn)
         #  SC : O(n)
        nums = sorted(set(nums))
        if len(nums) <= 2:
             return max(nums)
        else:
            return nums[-3]

        # Method III : Most optimal Using math
        max1,max2,max3 = float('-inf'),float('-inf'),float('-inf')
        for n in nums:
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2 and n < max1:
                max3 = max2
                max2 = n
            elif n > max3 and n < max2:
                max3 = n
        if max3 != float('-inf'):
            return max3
        else:
            return max1


# Battleship in a board
 # Method I : Using the concept of number of connected component which can be solved 
  # using dfs same as the problem count no. of islands
  # TC : O(N*M)
  # SC : worst case O(M×N) in case that the grid map is filled with lands
  # where DFS goes by M×N deep
  class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    count += 1
                    self.dfs(board,i,j,m,n)
        # print(board)
        return count
    def dfs(self,board,i,j,m,n):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'X':
            return
        board[i][j] = '.'
        self.dfs(board,i+1,j,m,n)
        self.dfs(board,i-1,j,m,n)
        self.dfs(board,i,j+1,m,n)
        self.dfs(board,i,j-1,m,n)
    # Method II : Using basic logic
     # TC : O(M * N)
     # SC : O(1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue;
                if i > 0 and board[i-1][j] == 'X':
                    continue;
                if j > 0 and board[i][j-1] == 'X':
                    continue;
                print(i,j)
                count += 1
        return count


    # Shuffling the array : 
    # Method : fisher Yates Algorithm
    # TC : O(N)
    # SC : O(N)
    class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.arr)):
            idx = random.randrange(i,len(self.arr))
            self.arr[i],self.arr[idx] = self.arr[idx],self.arr[i]
        return self.arr


    # Find all anagaram in a string
     # Method I : Brute force
      # TC : O(N*M) where N is length of string s and M is length of string p
      # SC : O(N + M) 
      class Solution:
        def findAnagrams(self, s: str, p: str) -> List[int]:
            m = len(s)
            n = len(p)
            res= []
            c = Counter(p)
            for i in range(m):
                if Counter(s[i:i+n]) == c:
                    res.append(i)
            return res
    # Method II: Sliding Window Problem
     # TC : O(N)
     # SC : O(N)
     # The idea is that  i have handle first p length as a refrence for sliding for sliding window
     # Everytime rather than updating hash for whole window length i have inserted one char in 
     # in hash and remove one char from hash to get new updated hash.
     # If at any time we get hash table same as given pattern we will update the res array
     # with corresponding index i.e i - n + 1
    class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(s)
        n = len(p)
        res= []
        c = Counter(p)
        t = s[:n]
        d = Counter(t)
        if d == c:
            res.append(0)
        for i in range(n,m):
            x = s[i]
            y = s[i - n]
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
            if y in d:
                d[y] -= 1
                if d[y] == 0:
                    d.pop(y)
            if d == c:
                res.append(i - n + 1)
        return res


    # String compression
    # Method I :
     # TC : O(N)
     # SC : O(1)
    class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        idx = 0 
        for i in range(1, len(chars)+1):
            if i < len(chars) and chars[i] == chars[i-1]:
                count += 1
                continue
            chars[idx] = chars[i-1]
            idx += 1
            if count > 1:                    
                s = str(count)                    
                chars[idx:idx+len(s)] = list(s)
                idx += len(s)   
            count = 1                    
            # print(chars) 
        return idx
        
    # Sort character by frequency
     # Method I : Using hashmap
     # TC : O(NlogN)
     # SC : O(1)
     class Solution:
        def frequencySort(self, s: str) -> str:
            c = Counter(s)
            x = sorted(c.items(),key = lambda v : v[1],reverse = True)
            return ''.join((i*j for i, j in x))

    # Method II ; Using max heap
     #  TC : O(NlogN)
        count, res = Counter(s), []
        max_heap = [(-value, key) for key, value in count.items()]
        heapq.heapify(max_heap)
        for _ in range(len(max_heap)):
            value, key = heapq.heappop(max_heap)
            res.append(key*(-value))
        return ''.join(res)

    # Repeated Substring pattern
    #  Method I : Brute Force
    #  TC : O(N^2)
    #  SC : O(N)
    class Solution:
        def repeatedSubstringPattern(self, s: str) -> bool:
            x = len(s)
            for i in range(1,x + 1):
                if len(s) % i != 0:
                    continue;
                if s[:i]*(len(s) // i) == s:
                    return True
            return False
    # Method - II
    # TC : O(N + N)
    # SC : O(N + N)
        x = s[1:] + s[:-1]
        if s in x:
            return True
        else:
            return False

    # Method III :
     # TC : O(N)
     # SC : O(N)
     def repeatedSubstringPattern(s):
        n = len(s)
        dfa = [0] * n
        d = 0
        for i in range(1, n):
            while d and s[i] != s[d]:
                d = dfa[d-1]
            d += s[i] == s[d]
            dfa[i] = d
        pat = dfa[n-1]
        return pat != 0 and (pat % (n-pat) == 0)     

    # Longest Palindromic Subsequence
    # TC : O(N*M)
    # SC : O(N*M)
    class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def helper(s,t,m,n):
            # Memoized 
            if m == 0 or n == 0:
                return 0;
            if dp[m][n] != -1:
                return dp[m][n]
            elif s[m - 1] == t[n - 1]:
                dp[m][n] =  1 + helper(s,t,m - 1,n - 1)
                return dp[m][n]
            else:
                dp[m][n] = max(helper(s,t,m - 1,n),helper(s,t,m,n - 1))
                return dp[m][n]
            # Top down Approach - Dp
            for i in range(m+1):
                for j in range(n+1):
                    if i == 0 or j == 0 :
                        dp[i][j] = 0
                    elif s[i-1] == t[j-1]:
                        dp[i][j] = dp[i-1][j-1]+1
                    else:
                        dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
            return dp[m][n]
        t = s[::-1]
        m = len(s)
        n = len(t)
        dp=[[-1 for j in range(n+1)] for i in range(m+1)]
        return helper(s,t,m,n)

        # Reduced space complexity
        def longestPalindromeSubseq(self, s: str) -> int:
            def helper(s,t,m,n):
                bi = bool     
                for i in range(m):
                    bi = i & 1
                    for j in range(n+1):
                        if (i == 0 or j == 0):
                            dp[bi][j] = 0
                        elif (s[i] == t[j - 1]):
                            dp[bi][j] = dp[1 - bi][j - 1] + 1
                        else:
                            dp[bi][j] = max(dp[1 - bi][j], dp[bi][j - 1])
                return dp[bi][n]
        t = s[::-1]
        m = len(s)
        n = len(t)
        dp = [[-1 for j in range(n+1)] for i in range(2)]
        return helper(s,t,m,n)
    

    # Most frequent subtreesum
    # TC : O(N)
    # SC :O(N)
    class Solution:
        def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
            count = defaultdict(int)
            def getSum(node):
                if not node:
                    return 0
                mySum = getSum(node.right) + getSum(node.left) + node.val
                count[mySum] += 1
                return mySum
            getSum(root)
            res = []
            max_freq = max(count.values())
            for key,val in count.items():
                if val == max_freq:
                    res.append(key)
            return res


    # Super Washing Machine
     # TC : O(N)
     # SC : O(1)
    class Solution:
        def findMinMoves(self, machines: List[int]) -> int:
            s = sum(machines)
            l = len(machines)
            if s % l != 0:
                return -1
            else:
                goal = s // l
                count,x = 0,0
                for load in machines:
                    diff = load - goal
                    count += diff
                    x = max(max(x,abs(count)),diff)
                return x


    # K- different array pairs
     # Method I : Brute force
     # TC : O(N^2 + N)
     # SC : O(N)
     class Solution:
        def findPairs(self, nums: List[int], k: int) -> int:
            l = len(nums)
            c = 0
            d = set()
            for i in range(l - 1):
                for j in range(l):
                    if j > i and abs(nums[i] - nums[j]) == k and (nums[i],nums[j]) not in d:
                        c += 1
                        d.add((nums[i],nums[j]))
                        d.add((nums[j],nums[i]))
            # print(d)
            return c
    # Method II : Using hashmap
    # TC : O(N)
    # SC : O(N)
    class Solution:
        def findPairs(self, nums: List[int], k: int) -> int:
            count = 0
            d = Counter(nums)
            for keys,val in d.items():
                if k == 0:
                    if val > 1:
                        count += 1
                    continue;
                if k + keys in d:
                    count += 1
            return count

    # Complex Number Multiplication
    # Method : Brute Force
    # TC : O(1)
    # SC : O(1)
    class Solution:
        def complexNumberMultiply(self, num1: str, num2: str) -> str:
            reala,imaga = num1.split("+")
            realb,imagb  = num2.split("+")
            imaga = imaga[:-1]
            imagb = imagb[:-1]
            real = int(reala)*int(realb) - int(imaga)* int(imagb)
            imag = int(reala)* int(imagb) + int(realb)* int(imaga)
            return str(real)+"+"+str(imag)+"i"

   # Subarray Equal Sum to K
   # Method I : Brute Force
    # TC : O(N^2)
    # SC : O(1)
    class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        c = 0
        for i in range(n):
            s = 0
            for j in range(i,n):
                s += nums[j]
                if s == k:
                    c += 1
        return c

    # Method II : Using hashmap
    # TC : O(N)
    # SC : O(N)
    class Solution:
        def subarraySum(self, nums: List[int], k: int) -> int:
            prevsum = defaultdict(int)
            res = 0
            currsum = 0
            for i in range(n):
                # If currsum is equal to desired sum,
                # then a new subarray is found. So
                # increase count of result.
                currsum += nums[i]
                if currsum == k:
                    res += 1
                # currsum exceeds given sum by k.
                # Find number of subarrays having 
                # this sum and exclude those subarrays
                # from currsum by increasing count by 
                # same amount.
                if currsum - k in prevsum:
                    res += prevsum[currsum-k]
                # Store the currsum value in map with count
                # of every currsum.
                prevsum[currsum] += 1
            return res
            

# Convert BST to greater Tree
 # Method I : Reverse InOrder Traversal
 # TC : O(N)
 # SC : O(N)
 class Solution(object):
    def __init__(self):
        self.total = 0
    def convertBST(self, root):
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root    

# Method II : Using stack
 class Solution(object):
    def __init__(self):
        self.total = 0
    def convertBST(self,root):
        node = root
        stack = []
        while stack or node is not None:
            while node:
                stack.append(node)
                node = node.right
                # print(stack)
            node = stack.pop()
            # print(node)
            self.total += node.val
            node.val = self.total
            node = node.left
        return root 
        

# Matrix : Brute Force
 # TC : O((M*N)^2)
 # SC : O(M*N)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dp = [[float('inf') if mat[i][j] else 0 for j in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    for k in range(m):
                        for l in range(n):
                            if mat[k][l] == 0:
                                dp[i][j] = min(dp[i][j],abs(i - k) + abs(j - l))
        return dp
# Method II : Using bfs
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    mat[i][j] = self.bfs(mat, i, j)
        return mat
    def bfs(self, mat, x, y):
        queue = deque([(x, y, 0)])
        visited = set()
        while queue:
            x, y, steps = queue.popleft()
            if len(mat) > x > -1 and len(mat[0]) > y > -1 and (x, y) not in visited:
                visited.add((x, y))
                if mat[x][y] == 0:
                    return steps
                queue.append((x + 1, y, steps + 1))
                queue.append((x - 1, y, steps + 1))
                queue.append((x, y + 1, steps + 1))
                queue.append((x, y - 1, steps + 1))
        return mat[x][y]
# BFS II : PRoper bfs
 # TC : O(N*M)
 # SC : O(N)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def bfs(mat,x,y):
            queue = deque([(x,y,0)])
            visited = set()
            while queue:
                # print(queue)     
                a,b,c = queue.popleft()
                direction = [[-1,0],[1,0],[0,-1],[0,1]]
                if mat[a][b] == 0:
                    return c
                for i,j in direction:
                    new_x = i + a
                    new_y = j + b
                    if new_x < 0 or new_y < 0 or new_x >= m or 
                            new_y >= n or (new_x,new_y) in visited:
                        continue;
                    queue.append([new_x,new_y,c + 1])
                    visited.add((new_x,new_y))
        m = len(mat)
        n = len(mat[0])
        dp = [[0 for i in range(n)]for j in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    dp[i][j] = bfs(mat,i,j) 
        return dp

# Optimal Division :
 # Method I : Using math
 # TC : O(N)
 # SC : O(N)
 class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
         if len(nums) == 1:
            return str(nums[0])
         if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
         res = str(nums[0])
         ans = ""
         for i in range(1,len(nums)):
            ans += nums[i]
            if i != len(nums) - 1:
                ans += "/"
        return res + "/(" + ans + ")"


# number of steps to reduce number to zero
 # TC : O(logN)
 # SC : O(1)
 class Solution:
    def numberOfSteps(self, num: int) -> int:
        c = 0
        while num > 0:
            if num % 2 == 0:
                num = num //2
            else:
                num -= 1
            c += 1
        return c


# Search suggestion system
# Method I : Brute Froce 
 # TC : O(N^2)
 # SC : O(N)
        op = []
        products.sort()
        print(products)
        for i, c in enumerate(searchWord):
            temp = []
            for p in products:
                # Index out of bound condition and character equals condition
                if i < len(p) and c == p[i]:
                    temp.append(p)
            op.append(temp[:3])
            products = temp
        return op

# Method II : using binary search
# TC : O(nlog(n)) + O(mlog(n)) : nlogn for sorting and mlogn for binary search of m products.
# SC : O(m)
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        n = len(products)
        idx,out,prefix = 0,[],""
        for c in searchWord:
            prefix += c
            idx = bisect.bisect_left(products,prefix)
            # print(idx)
            temp = []
            for i in range(idx,min(idx+3,len(products))):
                # inseted of this we can use startwithfunction
                # Just checking whether current prefix is equal to products 
                if products[i][:len(prefix)] == prefix:
                    # print(products[i][:len(prefix)])
                    temp.append(products[i])
            # Done to reduce length for product array just for optimization .Can be ignored
            products = products[idx:]
            out.append(temp)
            # print(out)
        return out


# Number of Dice Rolls with Target
# TC : O(d*target)
# SC : O(d)
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def helper(h,d,target):
            if target <= 0 or target > f * d:
                return 0
            if d == 1:
                return 1
            if (d,target) in h:
                return h[(d,target)]
            res = 0
            for i in range(1,f+1):
                res += helper(h,d - 1,target - i)
            h[(d,target)] = res
            return res
        h = {}
        return helper(h,d,target) % (10**9 + 7)



# Sum of Nodes with Even Grandparents
# TC : O(N)
# SC : O(H) : Used by recursion stack where H = height of tree
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.c = 0
        def helper(root):
            if root:
                if root.val % 2 == 0:
                    k = grandchildren(root)
                    self.c += k
                helper(root.left)
                helper(root.right)
        def grandchildren(root):
            temp = 0
            if root.left:
                if root.left.left:
                    temp += root.left.left.val
                if root.left.right:
                    temp += root.left.right.val
            if root.right:
                if root.right.left:
                    temp+=root.right.left.val
                if root.right.right:
                    temp+=root.right.right.val
            return temp
        helper(root)
        return self.c

        # Method II : 
        # If grandparent exist and  its even then add that curr val to sum
        # else we recurse to deep and current become parent and parent become grandparent 
        # after each recursion
        self.s = 0
        def helper(curr,p,gp):
            if curr:
                if gp and gp.val % 2 == 0:
                    self.s += curr.val
                helper(curr.left,curr,p)
                helper(curr.right,curr,p)
            return self.s
        return helper(root,None,None)


        # Method III : 
        # using queue
        import collections
        res = 0
        queue = collections.deque([(root, TreeNode(1))]) # the root does not have parent or grandparent, 
                                                        #you can initialize a TreeNode with any odd value
        
        while queue:
            size = len(queue) # travel level by level
            
            for _ in range(size):
                node, parent = queue.popleft()
                # print(node,parent)
                
                if parent.val % 2 == 0:
                    # check left and right grand child
                    res += node.left.val if node.left else 0
                    res += node.right.val if node.right else 0
                
                # go left and right to next level
                if node.left:
                    queue.append((node.left, node))
                
                if node.right:
                    queue.append((node.right, node))
            
        return res        


# Subarrays with K different Integers
 # Method I : Brute Force
  # TC : O(N^3)
  # SC : O(N)
  class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l = len(nums)
        c = 0
        for i in range(l):
            for j in range(i,l):
                if len(set(nums[i:j+1])) == k:
                    c += 1
        return c
# method II : Sliding window + Hashmap
# TC : O(N)
# SC : O(N)
# Approach: To directly count the subarrays with exactly K different integers is hard
# but to find the count of subarrays with at most K different integers is easy. 
# So the idea is to find the count of subarrays with at most K different integers, 
# let it be C(K), and the count of subarrays with at most (K – 1) different integers, 
# let it be C(K – 1) and finally take their difference, C(K) – C(K – 1) 
# which is the required answer. 
        def atmost(nums,k):
            left,right,d,l = 0,0,defaultdict(int),len(nums)
            count = 0
            while right < l:
                d[nums[right]] += 1
                while len(d) > k:
                    if nums[left] in d:
                        d[nums[left]] -= 1
                    if d[nums[left]] == 0:
                        del d[nums[left]]
                    left += 1
                count += right - left + 1
                right += 1
            return count
        return atmost(nums,k)-atmost(nums,k-1)

# K Closest Point to Origin
# Time: O(NLogN) NlogN(sorting) + N(iterating) so finally NLogN
# Space:O(N)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K == len(points):
            return points
        
        return [j for j in sorted(points, key=lambda x: x[0]*x[0] + x[1]*x[1])[:K]]
# Time: O(NLogK) sorting the heap of size K
# Space: O(N)
class Solution:
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, key=lambda x: x[0] * x[0] + x[1] * x[1])

# Not One liner :  My own implementation
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for p in points:
            dist =math.sqrt(p[0]*p[0] + p[1]*p[1])
            heapq.heappush(heap,[dist,p])
        i = 0
        while i < k:
            x = heapq.heappop(heap)
            res.append(x[1])
            i += 1
        return res
# Method IV :
 # One liner
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:k]

# Prison cells after N days
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        print(n)
        for i in range(1,n + 1):
            d = cells[:]
            for k in range(1,len(cells)-1):
                if (d[k-1] + d[k + 1]) % 2 == 0:
                    cells[k] = 1
                else:
                    cells[k] = 0
                if k == len(cells) - 2:
                    cells[-1] = 0
                if k == 1:
                    cells[0] = 0
            # print(cells)
        return cells

    # Method II : Brute Force
        def find_cycle(N,cells):
            d = {}
            res = [0]*8 
            for i in range(N):
                for j in range(1,7):
                    res[j] = int(cells[j-1] == cells[j+1])
                if len(d) > 0 and d[0] == res:
                    return d[(N - 1)% len(d)]
                else:
                    d[i] = res[:]
                cells  = res[:]
            return cells
        return find_cycle(n,cells)

# Most common Words
 # TC : O(N)
 # SC : O(N)
 class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = "".join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        paragraph = paragraph.split()
        c = Counter(paragraph)
        x = sorted(c.items(),key = lambda y : y[1],reverse = True)
        print(x)
        for a,b in x:
            if a not in banned:
                return a
# Min Cost Climbing
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) - 1
        def helper(n,cost):
            if n < 0:
                return 0
            return cost[n] + min(helper(n - 1,cost),helper(n - 2,cost))
        return min(helper(n,cost),helper(n-1,cost))
# DP Method
# TC : O(N)
# SC : O(N)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:   
        n = len(cost)
        dp = [0 for i in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        # print(dp)
        return min(dp[n-1],dp[n-2])

# Monotonic Increasing Digits

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = [int(x) for x in str(n)]
        # if lenght of string is 1 return that only e.g 9,8,7,6,5.....,0
        if str(n) == 1:
            return n
        else:
        # Starting from left finding first  cliif i.e when s[i] < s[i-1]
            i = 1
            while i < len(s) and int(s[i]) >= int(s[i-1]):
                i += 1 
            # This i will give point after which cliff is there
            # Now , starting from there reduce s[i-1] till then it become 
            # less than equal to original
            # and also s[i] >= s[i-1] at every step
            # We decrease here by 1 because if we dont and put 9 to the
            # rest of part after cliff the
            # number will become greater than original number.
            while i > 0 and i < len(s) and int(s[i]) < int(s[i-1]):
                s[i-1] = int(s[i - 1]) - 1
                i -= 1
            # Put 9 after the cliff ends
            for k in range(i + 1,len(s)):
                s[k] = 9
            # print(s)
            res = int("".join(map(str, s)))
            return res

# Split link list in parts
#Time Complexity: O(N + k) where NN is the number of nodes in the given list. 
# If k is large, it could still require creating many new empty lists.

# Space Complexity: O(k), the additional space used in writing the answer
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        curr = head
        N = 0
        while curr:
            N += 1
            curr = curr.next
        width = N // k
        rem = N % k
        ans = []
        curr = head
        for i in range(k):
            root = curr
            for j in range(width + (i < rem) - 1):
                if curr:
                    curr = curr.next
            if curr:
                curr.next,curr = None,curr.next
            ans.append(root)
        return ans


# Find Pivot Index
 # TC : O(N + N + N)
 # SC : O(N + N)
 class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0]*(n)
        right = [0]*(n)
        for i in range(1,n):
            left[i] = left[i-1] + nums[i-1]
        for i in range(n-2,-1,-1):
            right[i] = right[i+1] + nums[i+1]
        # print(left,right)
        for i in range(n):
            if left[i] == right[i]:
                return i
        return -1

# Method II : Without Using Extra Space
# TC : O(N)
# SC : O(1)
class Solution:
    def pivotIndex(self,nums:List[int]) ->int:
        n = len(nums)
        s = sum(nums)
        leftsum = 0
        for i,val in enumerate(nums):
            if leftsum == s - leftsum - val:
                return i
            leftsum += val 
        return -1


# Top K Most Frequent Words

# Method I : HashMap
# TC : O(NlogN + N + NlogN) : NlogN for Sorting  + N for creating Dictionary + 
# NlogK for sorting Map but at worst case when all element are different K = N 
# and NlogK will become NlogN
# SC : O(N)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = sorted(words)
        c = Counter(words)
        res = sorted(c.items(),key = lambda x : x[1],reverse = True)[:k]
        # print(res)
        a = []
        for i,j in res:
            a.append(i)
        return a

# Method II : Using Heap
# TC : O(N +  N + KlogN) : N for creating hashmap + N for building heap + KlogN for poping
       # K items from list of N
# SC : O(N)
class Solution:
    def topKFrequent(self,words : List[str],k : int) -> List[str]:
        c = Counter(words)
        max_heap = [(-value, key) for key, value in c.items()]
        heapq.heapify(max_heap)
        res = []
        while k > 0:
            x = heapq.heappop(max_heap)
            # print(x)
            res.append(x[1])
            k -= 1
        return res

# Baseball Game 
 # Method I : Brute Force
  # TC : O(N) : To parse every element in array
  # SC : O(N) : To store in stack
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for i in ops:
            if i == 'C':
                res.pop()
            elif i == 'D':
                x = 2* res[-1]
                res.append(x)
            elif i == '+':
                y = res[-1] + res[-2]
                res.append(y)
            else:
                res.append(int(i))
        return sum(res)

# Account Merge : DFS
 # TC : O(a + a[i]*log(a[i])) : a[i] is length of account[i].log factor is sorting each componet at end
  # class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        em_name = {}
        graph = defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                # print(acc[1])
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_name[email] = name
        # print(graph)
        s = set()
        ans = []
        # stack = []
        for email in graph:
            if email not in s:
                s.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for ni in graph[node]:
                        if ni not in s:
                            s.add(ni)
                            stack.append(ni)
                ans.append([em_name[email]] + sorted(component))
        return ans 

# PArtition Levels
# TC : O(N)
# SC : O(1)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Stores last index for every unique element
        last = {c : i for i,c in enumerate(s)}
        start,end = 0,0
        ans = []
        for i,c in enumerate(s):
            # End will increase if last occurence of current char is greater
            # than last occurences of previous character
            end = max(end,last[c])
            # i reaches to end that means all character in that partition
            # are only present in that partition 
            # So we append length of that partition and move start pointer one
            # step right to that partition so that new partition will start from 
            # here 
            if i == end:
                ans.append(end - start + 1)
                start = i + 1
        return ans


# Unique Email Address
 # TC : O(len(emails) * len(emails[i])) 
 # SC : O(N) - For using set
 class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for mail in emails:
            a,b = mail.split('@')
            a = a.replace(".","")
            idx = a.find('+')
            if idx != - 1:
                a = a[:idx]
            a = a + '@' + b
            s.add(a)
        return len(s)


# Global and Local Inversion
 # TC : O(N)
 # SC : O(1)
#  We can observe that each local inversion is global inversion 
# (or local inversions are subset of global inversions).
#  For both of them to be equal, every global inversion must only be a local inversion.

# A global inversion can be limited to be only a local inversion 
# if for every 0 <= i < N, abs(A[i] - i) <= 1.

# Why?
# Because, if A[i] - i > 1, we can have atleast 2 pairs
#  (i,j) and (i,k) such that A[i] > A[j] and A[i] > A[k] 
# but if every global inversion has to be only local inversion,
#  we should only have gotten a single pair (i,j) (more specifically
#  (i,i+1)) such that A[i] > A[j].
# Eg. [2,0,1], here A[0]-0 = 2 > 1, so we got two pairs of index (0,1) and (0,2) 
# making global inversions != local inversions.

 class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i,val in enumerate(nums):
            if abs(val - i) > 1:
                return False
        return True

# Reorder Data in Log Files
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            a,b = log.split(" ",maxsplit = 1)
            return (0,b,a) if b[0].isalpha() else (1,)
        return sorted(logs,key = get_key)


# Maximum Units on a Truck
# TC : O(NlogN)
# SC : O(1)
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1],reverse =True)
        ans = 0
        for i,j in boxTypes:
            if truckSize >= i:
                truckSize -= i
                ans += i*j
            else:
                ans += truckSize*j
                break;
        return ans

# Using Bucket Sort
# TC : O(N)
# SC : O(max(number of unit per boxes))
class Solution:
    def maximumUnits(self,boxTypes: List[List[int]],truckSize:int) -> int:
        freq, max_units = [0]*1001, 0
        for box in boxTypes:
            freq[box[1]] += box[0]
        # print(freq)
        for units in range(1000,0,-1):
            if truckSize < 0: break
            max_units += min(truckSize, freq[units]) * units
            truckSize -= freq[units]
        return max_units

# Image Smoothing
 # TC : O(N^2)
 # SC : O(N^2)
 class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        newimg = [[0 for j in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                avg = 0
                div = 0
                direction = [(-1,-1),(1,1),(1,0),(0,1),(0,-1),(0,0),(-1,0),(1,-1),(-1,1)]
                for dx,dy in direction:
                    newx,newy = dx + i,dy + j
                    if 0<= newx < m and 0<= newy < n:
                        avg += img[newx][newy]
                        div += 1
                newimg[i][j] = avg // div
        return newimg


# Set MisMatch : Find missing and repeating number
# Method I : using Sort
 # TC : O(NlogN)
 # SC : O(logn) : Sorting takes logn space
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


# Merge Two Binary Trees
 # Method I : Recursive 
  # TC : O(N)
  # SC:  O(logN) : where N is minimum height between two trees : Depth of recursion Tree
  class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root2.val += root1.val
        root2.left = self.mergeTrees(root1.left,root2.left)
        root2.right = self.mergeTrees(root1.right,root2.right)
        return root2

 # Method II : Iterative
  # TC : O(N)
  # SC : O(N)
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        stack = [(root1,root2)]
        while stack:
            x,y = stack.pop()
            # print(x)
            if x is None or y is None:
                continue;
            x.val += y.val
            if x.left:
                stack.append([x.left,y.left])
            else:
                x.left = y.left
            if x.right:
                stack.append([x.right,y.right])
            else:
                x.right = y.right
        return root1
            

# Construct String from binary Tree
# TC : O(N)
# SC : O(N) : in worst case depth of tree will O(n) for skewed tree
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if root is None:
            return ""
        if root.left is None and root.right is None:
            return str(root.val) + ""
        if root.right is None:
            return str(root.val) + "(" + self.tree2str(root.left)+")"
        return str(root.val) + "(" + self.tree2str(root.left) + ")(" + self.tree2str(root.right)+")" 
            

# SubTree of another Tree
# TC : O(N*K)
# SC : O(N)
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool: 
        if root:
            if self.isIdentical(root,subRoot):
                return True
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def isIdentical(self,root,subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        if root.val == subRoot.val:
            return self.isIdentical(root.left,subRoot.left) and self.isIdentical(root.right,subRoot.right)
        return False


    # Method II :  Hashing
     # TC : O(N)
     # SC : O(N)
    class Solution:
        def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool: 
            def hashify(node):
                if not node:
                    return None
                key = (node.val, hashify(node.left), hashify(node.right))

                return memo.setdefault(key, len(memo))
        memo = {}
        hashify(root)

        return (subRoot.val, hashify(subRoot.left), hashify(subRoot.right)) in memo


# Prime Number of Set Bit In Binary Representation
# TC : O((right - left)*log(ele))
# SC : O(1)
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        m = [2,3,5,7,11,13,17,19]
        count = 0
        for ele in range(left,right+1):
            if bin(ele).count("1") in m:
                count += 1
        return count
    # Without using built in function
    class Solution:
        def countPrimeSetBits(self, left: int, right: int) -> int:
            def binary(N):
                binaryans = 0
                count = 0
                while N != 0:
                    rem = N % 2
                    c = pow(10,count)
                    binaryans += rem*c
                    count += 1
                    N = N // 2
                return str(binaryans)
            m = [2,3,5,7,11,13,17,19]
            count = 0
            for ele in range(left,right+1):
                if binary(ele).count("1") in m:
                    count += 1
            return count

# Distant Barcodes
 # TC : O(NlogN)
 # SC : O(N)
 class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)
        pq,ans = [],[]
        # Build max heap to store their frequency and corresponding number
        for n, c in count.items():
            heapq.heappush(pq, (-c, n))
        prev_cnt, prev_num = 0, 0
        # while pq not empty pop an element and add to the result
        # After poping this element become prev_num and its freq become prev_count
        # If prev_count has freq > 0 add that prev_cnt and prev_num in heap again
        # so that we can place num again  in ans array.
        while pq:
            cnt, num = heapq.heappop(pq)
            if prev_cnt:
                heapq.heappush(pq, (prev_cnt, prev_num))
            ans.append(num)
            prev_cnt, prev_num = cnt+1, num
        return ans
    # Method II :
    # TC : O(N)
    # SC : O(N)
        maxfreq = 0
        d = defaultdict(int)
        for x in barcodes:
            d[x] += 1
            if d[x] > d[maxfreq]:
                maxfreq = x
        print(d[maxfreq])
        n = len(barcodes)
        res = [0]*n
        idx = 0
        for v in range(d[maxfreq]):
            res[idx] = maxfreq
            idx += 2
        del d[maxfreq]
        for k,v in d.items():
            for _ in range(v):
                print(idx)
                if idx >= n:
                    idx = 1
                res[idx] = k
                idx += 2
        return res


# Maximum length of Pair Chain : Similar to Merge Interval Question
 # TC : O(NlogN) : for sorting
 # SC : O(N)
 class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs,key = lambda x : x[1])
        # print(pairs)
        count = 1
        l = pairs[0][0]
        h = pairs[0][1]
        for i,j in pairs:
            if i > h:
                count += 1
                l,h = i,j
        return count
            

# 3 Sum Closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        res = nums[0] + nums[1] + nums[-1]
        for i in range(l - 2):
            start,end = i + 1,l - 1
            while start < end:
                currsum = nums[i] + nums[start] + nums[end]
                if currsum > target:
                    end -= 1
                else:
                    start += 1
                if abs(currsum - target) < abs(res - target):
                    res = currsum
        return res

# Maximum Width of Binary Tree
# TC : O(N)
# SC : O(N)
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = []
        maxwidth = 1
        # Here we append root node position as 0 
        queue.append([0,root])
        while queue:
            count = len(queue)
            # Here start will store left most node position of every level
            # and end will store right most node of every level
            # Subtracting both after every level and finding max between all of them will give us our ans.
            start = queue[0][0]
            end = queue[-1][0]
            maxwidth = max(maxwidth,end - start + 1)
            # Exact same code for level order traversal.
            # Here we r just adding on position variable in queue just to keep track of
            # left most and right most node of every partitcular level
            while count > 0:
                count -= 1
                pos,temp = queue.pop(0)
                if temp.left:
                # Left node position will 2* position of its parent node + 1
                    queue.append([2*pos + 1,temp.left])
                if temp.right:
                # Right node position will 2* position of its parent node + 2
                    queue.append([2*pos + 2,temp.right])
        return maxwidth


# Shortest Unsorted Contiguous Array
# MEthod I : Brute Force
  # TC : O(N^2) : Gives TLE
  # SC : O(1)
      for j in range(i+1,len(nums)):
        if nums[i] > nums[j]:
            r = max(r,j)
            l = min(l,i)
        if r - l < 0:
            return 0
        else:
            return r - l + 1
# MEthod II : Two Pointer + Sorting
# TC : O(NlogN)
# SC : O(N)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        t = nums[:]
        t.sort()
        l = len(nums)
        i,j = 0,l - 1
        while i < j:
            if t[i] == nums[i] and t[j] == nums[j]:
                i += 1
                j -= 1
            elif t[i] == nums[i]:
                i += 1
            elif t[j] == nums[j]:
                j -= 1
            else:
                return j - i + 1
        return 0

# Method III : 
 # TC : O(N + N) : Two pass
 # SC : O(N)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        end,start = 0,0
        l = len(nums)
        maxi,mini = float('-inf'),float('inf')
        for i in range(l):
            maxi = max(maxi,nums[i])
            if nums[i] < maxi:
                end = i
        for i in range(l-1,-1,-1):
            mini = min(mini,nums[i])
            if nums[i] > mini:
                start = i
        if end > 0:
            return end - start + 1
        else:
            return 0
# Method IV : Using stack
 # TC : O(N)
 # SC : O(N)
 class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        m,r = float('inf'),float('-inf')
        l = len(nums)
        stack = []
        for i in range(l):
            while stack and nums[stack[-1]] > nums[i]:
                m = min(m,stack[-1])
                m = stack.pop(-1)
            stack.append(i)
        stack = []
        for i in range(l-1,-1,-1):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r,stack[-1])
                r = stack.pop(-1)
        if r - l > 0:
            return r - l + 1
        else:
            return 0

# Knight Dialer
# TC : O(N)
# SC : O(N)
class Solution:
    def paths(self,i,j,n,hm):
        mod = 10**9 + 7
        if i < 0 or j < 0 or i >= 4 or j >= 3 or (i == 3 and j != 1):
            return 0
        if n == 1:
            return 1
        if hm[(i,j,n)] != 0:
            return hm[(i,j,n)] % mod
        hm[(i,j,n)] = self.paths(i - 1, j - 2, n - 1,hm) % mod +
         self.paths(i - 2, j - 1, n - 1,hm) % mod + self.paths(i - 2, j + 1, n - 1,hm) % mod +
          self.paths(i - 1, j + 2, n - 1,hm) % mod + self.paths(i + 1, j + 2, n - 1,hm) % mod +
           self.paths(i + 2, j + 1, n - 1,hm) % mod + self.paths(i + 2, j - 1, n - 1,hm) % mod +
            self.paths(i + 1, j - 2, n - 1,hm) % mod
        return hm[(i,j,n)]
    def knightdialer(self,n:int) -> int:
        s = 0
        hm = defaultdict(int)
        for i in range(4):
            for j in range(3):
                s += paths(i,j,n,hm) % mod
        return s


# Rotten Oranges
# Time complexity: O(rows * cols) -> each cell is visited at least once
# Space complexity: O(rows * cols) -> in the worst case if all the oranges
#  are rotten they will be added to the queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        direction = [[-1,0],[0,-1],[1,0],[0,1]]
        count,freshcount,queue = 0,0,[]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    freshcount += 1
        while freshcount > 0 and queue:
            l = len(queue)
            count += 1
            while l > 0:
                l -= 1
                a,b = queue.pop(0)
                for x,y in direction:
                    new_x = x + a
                    new_y = y + b
                    if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or 
                                    grid[new_x][new_y] == 0 or grid[new_x][new_y] == 2:
                        continue;
                    queue.append([new_x,new_y])
                    grid[new_x][new_y] = 2
                    freshcount -= 1          
        if freshcount == 0:
            return count
        else:
            return -1

# Reoraganize String
# TC : O(N)
# SC : O(N)

class Solution:
    def reorganizeString(self, s: str) -> str:
        maxfreq = 0
        d = defaultdict(int)
        res = [0 for i in range(len(s))]
        for x in s:
            d[x] += 1
            if d[x] > d[maxfreq]:
                maxfreq = x
            if (2 * d[maxfreq]) - 1 > len(s):
                return ""
        idx = 0
        for v in range(d[maxfreq]):
            res[idx] = maxfreq
            idx += 2
        del d[maxfreq]
        for k,v in d.items():
            for _ in range(v):
                if idx >= len(s):
                    idx = 1
                res[idx] = k
                idx += 2
        return "".join(res)

    
# Longest consecutive sequencce
# Brute Force
 # TC : O(n^3)
 # SC : O(1)
 class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            count = 1
            while num + 1 in nums:
                num += 1
                count += 1
            ans = max(ans,count)
        return ans

 # Method II : Sorting
 # TC : O(NlogN)
 # SC : O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        ans = 1
        count = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] - nums[i-1] == 1:
                    count += 1
                else:
                    ans = max(ans,count)
                    count = 1
        return max(ans,count)

# Method III : HashSet + Optimised Brute Force
# TC : Although the time complexity appears to be quadratic due to the 
# while loop nested within the for loop, closer inspection reveals it to be linear.
# Because the while loop is reached only when currentNum marks the beginning of a sequence  
#(i.e. currentNum-1 is not present in nums), the while loop can only run for nn iterations 
# throughout the entire runtime of the algorithm. This means that despite looking like 
# O(n^2) complexity, the nested loops actually run in O(n + n) = O(n)O(n+n)=O(n) time. 
# All other computations occur in constant time, so the overall runtime is linear.
# TC : O(N)
# SC : O(N) : For Hashset
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s =set(nums)
        ans,count = 0,0
        for num in s:
            if num - 1 not in s:
                count = 1
                while num + 1 in s:
                    num += 1
                    count += 1
            ans = max(ans,count)
        return ans


# Add two number II : 
# TC : O(N)
# SC : O(N
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reversell(newl):
            prev = None
            curr = newl
            while curr:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
            newl = prev
            return newl
        # Same code for addtwonumber I 
        def addtwonumber(a,b):
            dummy = ListNode()
            curr = dummy
            carry,val = 0,0
            while a or b or carry:
                v1 = a.val if a else 0
                v2 = b.val if b else 0
                val = v1 + v2 + carry
                carry = val // 10
                val = val % 10
                curr.next = ListNode(val)
                curr = curr.next
                # Edge Case when length are different thats why if else
                a = a.next if a else None
                b = b.next if b else None
            return dummy.next
        return reversell(addtwonumber(reversell(l1),reversell(l2)))


# 4 Sum 
 # TC : O(N^2)
 # SC : O(N + N)
 class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        # Creating frequency map of array sum of both pairs of array
        ab = Counter(l + m for l in nums1 for m in nums2) # For num1 and num2
        cd = Counter(l + m for l in nums3 for m in nums4) # num3 and num4
        for x in ab:
        # Why - x ?
        # Here x is sum of element from first two array
        # In order to make total sum 0, -x key should definately be present in other two pair of array
            if -x in cd:
            # If -x is present we r multiply the frequency because 
            # suppose ab[x] = 2 and cd[-x] = 3 that means we have 6 different pair of tuples i,e different
            # combination will be possible.
                ans += ab[x]*cd[-x]
        return ans

# Contiguous Array
 # TC : O(N^2)
 # SC : O(1)
 class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        maxlen = 0
        for i in range(n):
            one,zero = 0,0
            for j in range(i,n):
                if nums[j] == 0:
                    one += 1
                else:
                    zero += 1
                if zero == one:
                    maxlen = max(maxlen,j-i+1)
        return maxlen

# TC : O(N)
# SC : O(N)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0:-1}
        maxlen,count = 0,0
        for i,val in enumerate(nums):
            if val == 1:
                count += 1
            else:
                count -= 1
            if count in d:
                maxlen = max(maxlen,i - d[count])
            else:
                d[count] = i
        return maxlen

# Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Method I : Brute Force : TC : O(N^2) : SC :O(1)
        n = len(nums)
        maxel = n / 2
        for num in nums:
            count = 0
            for ele in nums:
                if num == ele:
                    count += 1
            if count > maxel:
                return num
        # Method II : Hashing : TC : O(N) : SC : O(N)
        c = Counter(nums)
        for i in c:
            if c[i] > n / 2:
                return i

        # Method III : Boyes Moore Voting Algorithm
        # TC : O(N)
        # SC : O(1)
        count = 0
        candidate = None
        for num in  nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
          
# Find the difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Method I : HashMap : TC : O(N) : SC : O(1)
        c = Counter(s)
        d = Counter(t)
        for x in d:
            if x not in d or c[x] != d[x]:
                return x
        # MEthod II : Bit Malipulation : TC : O(N) : SC : O(1)
        ch = 0
        for num in s:
            ch ^= ord(num)
        for num in t:
            ch ^= ord(num)
        return chr(ch)

# Rank Transform of An  Array
 # TC : O(N)
 # SC : O(N)
 class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = list(sorted(set(arr)))
        d = {}
        for i,val in enumerate(a):
            d[val] = i + 1
        return [d[x] for x in arr]

# Rotate String
# Brute Force
 # TC : O(N^2)
 # SC : O(1)
 class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(n):
            new_s = s[i:] + s[:i]
            if new_s == goal:
                return True
        return False
 # Method II : TC : O(N^2) : SC : O(N)
 class Solution:
    def rotateString(self,s:str,goal:str) -> bool:
        if len(s) == len(goal) and goal in (s + s):
            return True
        return False
# Method III : TC : O(N) SC : O(N)
 # Same as Method II but here We use KMP algorithm for pattern searching
   def kmp(pat, txt):
        # print(pat,txt)
        M = len(pat)
        N = len(txt)
        lps = [0]*M
        j = 0 # index for pat[]
        computeLPSArray(pat, M, lps) 
        i = 0 # index for txt[]
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1 
            if j == M:
                # print ("Found pattern at index " + str(i-j))
                # j = lps[j-1]
                return True 
            # mismatch after j matches
            elif i < N and pat[j] != txt[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return False
    def computeLPSArray(pat, M, lps):
        j = 0 # length of the previous longest prefix suffix 
        lps[0] # lps[0] is always 0
        i = 1
        # the loop calculates lps[i] for i = 1 to M-1
        while i < M:
            if pat[i]== pat[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j-1]  
                    # Also, note that we do not increment i here
                else:
                    lps[i] = 0
                    i += 1
    if len(s) != len(goal):
        return False
    else:
        return kmp(goal,s+s)

# K-Largest Element in A Streak
# Brute Force 
 # TC : Number of add operation*(NlogN)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse = True)
        return self.nums[self.k-1]

# Method II : Heap
# TC : O(N + (N-K)log(N)) : O(N) for heapify and (N -K)logN for finding kth largest number
# SC : O(N)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapify(self.heap)
        # It leaves last k element in tree as first N - k element will be popped out.
        # So first element in heap will be kth largest element
        while len(self.heap) > k:
            heappop(self.heap)
    # For adding every element we require log(N) time for heappush and log(N) for heappushpop
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]

# peak Index in mountain array
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # method I : linear run : tc : O(N)
        n = len(arr)
        for i in range(1,n-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                return i
        # method II : Tc : O(logN), SC :O(1)
        n = len(arr)
        lo,hi = 0,n-1
        while lo < hi:
            mid = (lo + hi)//2
            if arr[mid] < arr[mid+1]:
                lo = mid + 1
            else:
                hi = mid
        return lo

# Pairs of Songs with Total Duration
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Method I : Brute Force
        # TC : O(N^2)
        # SC : O(1)
        n = len(time)
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        return count
        # Method II : HashMap
        # TC : O(N)
        # SC : O(1)
        remainders = defaultdict(int)
        counts = 0
        for i, t in enumerate(time):
            if t % 60 == 0: # check if a % 60 and b % 60 == 0
                counts += remainders[t % 60]
            else:
                # Check if a % 60 + b % 60 = 60
                # if 60 - a % 60 in remainders that means there in pairs
                counts += remainders[60 - t % 60] 
            remainders[t % 60] += 1
        return counts

# Number of ways to Split a Binary String 
# TC : O(N + N)
# SC : O(1)
class Solution:
    def noways(self,s:str) -> int:
        l = len(s)
        ones = 0
        for c in s:
            if c == '1':
                ones += 1
        if ones == 0:
            return ((l-1)*(l-2)//2) % mod
        if ones % 3 != 0:
            return 0
        ones,ways,ways2= 0,0,0
        onethird = ones // 3
        for c in s:
            if c == '1':
                ones += 1
            if ones == onethird:
                ways += 1
            if ones == 2 * onethird:
                ways2 += 1
        return (ways * ways2) % mod
     

# Make max area of islands   
# TC : O(N*N)
# SC : O(N*N)
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,i,j,gridId):
            # normal dfs operation
            if i < 0 or j < 0 or i>=len(grid) or j>=len(grid) or grid[i][j] != 1:
                return 0
            # Setting up grid to its corresponding id of island
            grid[i][j] = gridId
            return dfs(grid, i+1, j,gridId) + dfs(grid, i-1, j,gridId) + dfs(grid, i, j+1,gridId) + dfs(grid, i, j-1,gridId) + 1
        m = len(grid)
        d = defaultdict(int)
        gridId = 2
        for i in range(m):
            for j in range(m):
                if grid[i][j] == 1:
                    area = dfs(grid,i,j,gridId) # Store a key value pair of <id,area of island>
                    d[gridId] = area   #  in dictionary
                    gridId += 1   # Increase the id for new island
        # print(d)
        res = d[2] # If there are no zeores then we return res = area of one single island or (N*N)
        for i in range(m):
            for j in range(m):
                # If zero is there check its adjacent four neighbour and store the ids of                 if grid[i][j] == 0:
                   # all four neighbours islands if its exists
                    s = set()
                    direction = [[-1,0],[1,0],[0,1],[0,-1]]
                    for nx,ny in direction:
                        new_x = i + nx
                        new_y = j + ny
                        if new_x < 0 or new_y < 0 or new_x >= m or new_y >= m:
                            continue;
                        s.add(grid[new_x][new_y])
                    # We have changed 0 to 1, so total will start from 1
                    total = 1
                    # Now add the area of all four islands of that particular 0.
                    for x in s:
                        total += d[x]
                    res = max(res,total)
        return res


# Number of Province 
# Method I
# TC : O(N*M)
# SC : O(N)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(graph,visited,i):
            visited[i] = 1
            for l in graph[i]:
                if visited[l] == 0:
                    visited[l] = 1
                    dfs(graph,visited,l)
        graph = OrderedDict()
        n = len(isConnected)
        path = [[] for j in range(n)]
        visited = [0]*(n+1)
        # Creating adjacency list using graph
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    if i not in graph:
                        graph[i] = [j]
                    else:
                        graph[i].append(j)
        count = 0
        for i in range(n):
            if visited[i] == 0:
                count += 1
                # Start traversing one row and traverse deep to find its all connected component
                dfs(graph,visited,i)
        return count 

# Method II : 
# without creating adjaceny matrix
class Solution:
    def findCircleNum(self,iscon : List[List[int]]) -> int:
        n = len(iscon)
        visited = [0]*(n + 1)
        def dfs(v,visited):
            visited[v] = 1
            for i in range(n):
                if visited[i] == 0 and iscon[v][i] == 1:
                    visited[i] = 1
                    dfs(i,visited)
        count = 0
        for i in range(n):
            if visited[i] == 0:
                count += 1
                dfs(i,visited)
        return count

# Iterative Using Stack
from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        def dfs(node):
            queue = deque()
            queue.append(node)
            visited[node] = True
            while queue:
                node1 = queue.pop()
                for node2 in range(n):
                    if isConnected[node1][node2] == 1 and not visited[node2]:
                        queue.append(node2)
                        visited[node2] = True
                
        visited = [False]*n
        count = 0
        for node in range(n):
            if not visited[node]:
                dfs(node)
                count += 1   
        return count

# First Bad version
# Binary Search Implementation
        # left,right = 1,n
        # while left < right:
        #     mid = left + (right - left)//2
        #     if isBadVersion(mid):
        #         right = mid
        #     else:
        #         left = mid + 1
        # return right
# Sqrt :
    # Finding sqrt using binary search
    # if x == 0:
    #         return 0
    #     if x == 1:
    #         return 1
    #     left,right = 0,x
    #     while left < right:
    #         mid = left + (right - left)//2
    #         if mid * mid > x:
    #             right = mid
    #         else:
    #             left = mid + 1
    #     return right - 1

# Find K closest element
class Solution(object):
    def findClosestElements(self, arr, k, x):
        # Method I : Heap
        # TC : NlogK + klogN + KlogK
        heap,res = [],[]
        for i in arr:
            heap.append((abs(x-i),i))
        heapq.heapify(heap)
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return sorted(res)

        # Method II : Two pointer
        left,right = 0,len(arr) - 1
        while right - left >= k:
            if abs(x - arr[left]) <= abs(x - arr[right]):
                right -= 1
            else:
                left += 1
        return arr[left:right + 1]

        # Method III : Binary Search
        # TC : O(logN + k)
        # SC : O(1)
        left,right = 0,len(arr) - 1
        while left < right:                        # Method to find index where x is
            mid = left + (right - left) // 2       #  should be placed so that array will
            if arr[mid] >= x:                      # remain sorted
                right = mid
            else:
                left = mid + 1
        # print(left)
        insert_pos = left - 1
        left = insert_pos
        right = insert_pos + 1              # After finding index expand from both sides and
        i = 0                               # check for less difference and move left and
        while i < k and left >= 0 and right < len(arr):  # right pointer accordingly.
            if abs(x - arr[left]) <= abs(x - arr[right]):
                left -= 1
            else:
                right += 1
            i += 1
        while i < k:
            if left < 0:
                right += 1
                i += 1
            elif right >= len(arr):
                left -= 1
                i += 1
        return arr[left+1:right]


        # Method III.0 :Binary Search consise
        left,right = 0,len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
            
# As far from land as possible : Same code as For Rotten Tree with some slight difference
# BFS Solution
# TC : O()
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = []
        n = len(grid)
        zero = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j))
                else:
                    zero += 1
        if zero == 0 or len(queue) == 0:
            return -1
        count = 0
        while queue:
            l = len(queue)
            count += 1
            while l > 0:
                l -= 1
                x,y = queue.pop(0)
                direction = [[-1,0],[1,0],[0,1],[0,-1]]
                for dx,dy in direction:
                    new_x,new_y = x + dx,y + dy
                    if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n or grid[new_x][new_y] != 0:
                        continue;
                    queue.append((new_x,new_y))
                    grid[new_x][new_y] = "#"
        return count - 1



# Task Schedular :
   # TC : O(N)
   # SC : O(1)
# Suppose {A:6,B:4,C:2} n = 2 then we can fill the slot  in the matrix for clear visualization
    # At every row there will be three element since n = 2
    # So [
    #       [ A  , B , C ],
    #       [ A  , B , C ],
    #       [ A , B , idle],
    #       [ A , B , idle ],
    #       [ A, idle , idle ],
    #       [ A , empty ,empty ]
    #    Here we can see that for first 5 row number of element is 
    #     (maxfreq - 1) * ( number of element in column i.e (n + 1)
    
    #    For last row there might be all all three n + 1 element or less than that ,which depends upon 
    #    frequency  of  elements in array.So we handle that case diffrently.
    
    #    For calculating number of element in last row,we can check how many character have
    
    #    max frequency which is thevalue of  last_row
    # So final answer will be 
    #    ans = (number of row - 1) * ( column) + number of element in last row
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        freq = list(freq.values())
        last_row = freq.count(max_freq)
        ans = (max_freq - 1) * (n + 1) + last_row
        return max(len(tasks),ans)
            
# Robot Bounded In a Circle
 # TC : O(N)
 # SC : O(1)
#  https://leetcode.com/problems/robot-bounded-in-circle/discuss/290856/JavaC%2B%2BPython-
#   Let-Chopper-Help-Explain
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dx,dy = 0,1
        x,y = 0,0
        for i in instructions:
            if i == 'G':
                x,y = x + dx,y + dy
            elif i == 'L':
                dx,dy = -1 * dy,dx
            else:
                dx,dy = dy, -1 * dx
        if (x,y) == (0,0) or (dx,dy) != (0,1):
            return True
        return False

# Capacity to Ship Packages Within D days
# Method I : Binary Search
# TC : O(N*log(sum(N) - max(N)))
# Quite Challenging Problem
# Intitution Behind Binary Search ?
# We know that our boundary lies within max(weights) to sum(weights) because
# we might have D >= len(weights) that means we can ship one weight in each
# particular days so least weight capacity will be max(weights)
# Also if d == 1,then we have ship all weights in 1 day,in that case least weight 
# capacity will be sum of all weights.
# So after this we know that our ans lies between ans -> (max(weights) to (sum(weights)))
# So boundary space of binary search is left = max(weigts) ,right = sum(weigts)
# After that we check for mid which is actually capacity of ship.
# If capacity is greater obivously it will take less days to ship all weights.
# So if days  < D that means we have days left in our account then we can optimise our 
# solution by decreasing the capacity.
# How can we decrease our capacity ?
# By decreasing our ans space.So rigt will move to mid.
# If capacity become too less than it will take more number of days than required
# In that case we have to increase our capacity that is we have increase mid 
# So we increase our left to mid.
# Gradually our boundary decrease and it satisfy our d and give our result.


# I tried my best to make you understand.Hope it helps.
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def feasible(capacity) -> bool:
            days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:  # too heavy, wait for the next day
                    total = weight
                    days += 1
                    if days > D:  # cannot ship within D days
                        return False
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                # print(mid)
                right = mid
            else:
                left = mid + 1
                # print(left)
        return left

# Optimal Strategy For Game 
# using DP
piles = list(map(int,input().split()))
dp = [[0 for i in range(len(piles))] for j in range(len(piles))]
n = len(piles)
for g in range(n):
    j = g
    for i in range(n):
        if g == 0:
            dp[i][j] = piles[i]
        elif g == 1:
            dp[i][j] = max(piles[i],piles[j])
        else:
            val1 = piles[i] + min(dp[i+2][j],dp[i + 1][j-1])
            val2 = piles[j] + min(dp[i + 1][j - 1],dp[i][j - 2])
            dp[i][j] = max(val1,val2)
        j += 1
return dp[0][n-1]

# Course Scheduling II :
# Method I : Using Kahns Algorithm
# TC : O(N^2)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def kahnalgo(graph,indegree,numCourses,ans):
            queue = []
            # Step II :
             # Push all indegree nodes which has no prequisite that means 
                # there value will be 0
            for i in range(numCourses):
                if indegree[i] == 0:
                    queue.append(i)
            count = 0
            # Step III : 
             # Preprocess the queue using bfs
                # At each level we remove the node from queue one by one
                # If we remove the node obviously indegree values will decrease
                # of those which are connected from that node
                # If indegree become zero that means now they have no prequesite
                # and we can append that in our queue.
            while queue:
                curr = queue.pop(0)
                for a in graph[curr]:
                    indegree[a] -= 1
                    if indegree[a] == 0:
                        queue.append(a)
                # Since we are appending only indegree value 0 as a node in queue
                # that means it has no prequesite so we can append it in ans 
                # array.
                ans.append(curr)
                count += 1
            # also here count is there to keep track if there might be deadlock 
            # or cycle is present there in graph.
            if count != numCourses:
                return False
            return True
        # Step I : Create adjacney graph or list  and create indegree array
        # which will store no. of incoming edges of every nodes
        graph = defaultdict(list)
        indegree = [0]*(numCourses)
        for desc,src in prerequisites:
            graph[src].append(desc)
            indegree[desc] += 1
        ans = []
        if kahnalgo(graph,indegree,numCourses,ans):
            return ans
        return []

# Knight Probablity In a Chess Board
# Method I : Recursive
# TC : O(8^N)
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def recurse(n,k,r,c):
            direction = [[1,2],[1,-2],[-1,2],[-1,-2],[-2,-1],[-2,1],[2,1],[2,-1]]
            if r < 0 or c < 0 or r > n - 1 or c > n - 1:
                return 0
            if k == 0:
                return 1
            ans = 0
            for dx,dy in direction:
                ans += 0.125*recurse(n,k-1,r + dx,c + dy)
            return ans
        return recurse(n,k,row,column)
# Method II : Memoized + Recursion
# 
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        d = {}
        def recurse(n,k,r,c):
            direction = [[1,2],[1,-2],[-1,2],[-1,-2],[-2,-1],[-2,1],[2,1],[2,-1]]
            if r < 0 or c < 0 or r > n - 1 or c > n - 1:
                return 0
            if k == 0:
                return 1
            if (r,c,k) in d:
                return d[(r,c,k)]
            ans = 0
            for dx,dy in direction:
                ans += 0.125*recurse(n,k-1,r + dx,c + dy)
            d[(r,c,k)] = ans
            return ans
        return recurse(n,k,row,column)


# Best Time to Buy Sell Stock III:
# Explanation
# It's not difficult to get the DP recursive formula:

# dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j-1]), j=[0..i-1]
# For k transactions, on i-th day,
# if we don't trade then the profit is same as previous day dp[k, i-1];
# and if we bought the share on j-th day where j=[0..i-1], then sell the 
# share on i-th day then the profit is prices[i] - prices[j] + dp[k-1, j-1] .
# Actually j can be i as well. When j is i, the one more extra item 
# prices[i] - prices[j] + dp[k-1, j] = dp[k-1, i] looks like we just lose one
# chance of transaction.

# TC : O(kN)
    def int MaxProfitDpCompact1(int[] prices):
        if len(prices) == 0:
            return 0;
        dp = new int[3, len(prices)];
        for k in range(1,3):
            mini = prices[0];
            for i in range(1,len(prices)):
                mini = min(mini, prices[i] - dp[k-1, i-1]);
                dp[k, i] = max(dp[k, i-1], prices[i] - mini);
            return dp[2, prices.Length - 1];
    # Method II:
    # O(N)
     def int MaxProfitDpCompact1(int[] prices):
            int buy1 = int.MaxValue, buy2 = int.MaxValue;
            int sell1 = 0, sell2 = 0;

            for i in range(len(prices)):
                buy1 = min(buy1, prices[i]);
                sell1 = max(sell1, prices[i] - buy1);
                buy2 = min(buy2, prices[i] - sell1);
                sell2 = max(sell2, prices[i] - buy2);
            return sell2;


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.dic = dict() # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1


# LRU Cache
    def put(self, key: int, value: int) -> None:
        if key in self.dic:             # similar to get()        
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value         # replace the value len(dic)
        else: 
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key,value)
            self.dic[key] = node
            self.insertIntoHead(node)
            
    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insertIntoHead(self, node):
        headNext = self.head.next 
        self.head.next = node 
        node.prev = self.head 
        node.next = headNext 
        headNext.prev = node
    
    def removeFromTail(self):
        if len(self.dic) == 0: return
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)


# Inorder Traversal

# Recursive
class Solution:
    def helper(self,root,res):
        if root:
            self.helper(root.left,res)
            res.append(root.val)
            self.helper(root.right,res)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root,res)
        return res

# Iterative
curr = root
stack = []
done = 0
while curr and stack:
    while curr:
        stack.append(curr)
        curr = curr.left
    curr = stack.pop()
    res.append(curr.val)
    curr = curr.right 
return res 

#PostOrder Traversal : TC : O(N)
#                    : SC : O(N)
class Solution:
    def helper(self,root,res):
        if root:
            self.helper(root.left,res)
            self.helper(root.right,res)
            res.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root,res)
        return res

# PreOrder Traversal : TC : O(N) , SC : O(N)

class Solution:
    def helper(self,root,res):
        if root:
            res.append(root.val)
            self.helper(root.left,res)
            self.helper(root.right,res)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            res = []
            self.helper(root,res)
            return res

# Left View OF Binary Tree
def LeftView(root):
    ans = []
    if root is None:
        return ans
    queue = []
    queue.append(root)
    while len(queue)>0:
        size = len(queue)
        for i in range(1,size+1):
            temp = queue.pop(0)
            if i == 1:
                ans.append(temp.data)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            size-=1
    return ans


# Find bottom left tree value
if root is None:
    return
queue = [root]
while queue:
    r = queue.pop(0)
    if r.right:
        queue.append(r.right)
    if r.left:
        queue.append(r.left)
return r.val


# Bottom VIew Of Binary Tree
# Method I :
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return 
        d = {}
        stack = [(root,0)]
        while stack:
            node, level = stack.pop(0)
            # Keep Updating the rightmost node at every level
            d[level] = node.data
            if node.left:
                stack.append((node.left, level - 1))
            if node.right:
                stack.append((node.right, level + 1))
        # Level +1 and -1 is to just to make sure that left and right  node at every level
        # will store in different hashmap value.
        a = []
        for i in sorted(d.keys()):
            a.append(d[i])
        return a 

# Method II : To find distance of every node from root and store  its distance and
#         value in hashmap.For every key in hashmap we have a one value which is bottom view 
def bottomView(self, root):
        # code here
        def __init__(self):
            self.hd = 0
        if root is None:
            return
        hd = 0
        d = dict()
        root.hd = 0
        queue = [root]
        while queue:
            x = queue.pop(0)
            hd = x.hd
            d[hd] = x.data
            if x.left:
                queue.append(x.left)
                x.left.hd = hd - 1
            if x.right:
                queue.append(x.right)
                x.right.hd = hd + 1
        a = []
        for i in sorted(d.keys()):
            a.append(d[i])
        return a  


# Print Top View
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return 
        d = {}
        stack = [(root,0)]
        while stack:
            node, level = stack.pop(0)
            # Keep Updating the rightmost node at every level
            if level not in d:  # Just one line chance from bottom view
                d[level] = node.data
            if node.left:
                stack.append((node.left, level - 1))
            if node.right:
                stack.append((node.right, level + 1))
        # Level +1 and -1 is to just to make sure that left and right  node at every level
        # will store in different hashmap value.
        a = []
        for i in sorted(d.keys()):
            a.append(d[i])
        return a 

# Spiral Level Order Traversal
def findSpiral(root):
    # Code here
    if root:
        queue = [root]
        flag = 1
        res = []
        while queue:
            l = len(queue)
            listt = []
            flag =  -1*flag
            for i in range(l):
                x = queue.pop(0)
                listt.append(x.data)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            if flag > 0:
                res.extend(listt)
            else:
                res.extend(listt[::-1])
        return res
    else:
        return []


# height of Binary Tree
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if root is None:
            return 0
        lefttr = self.height(root.left)
        righttr = self.height(root.right)
        return max(lefttr,righttr) + 1


# Diameter of Tree
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        
        def depth(p):
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left+right) # For every node we check max of left depth + right depth and store in as
            return 1 + max(left, right) # Return maximum depth of every node i.e max height of that node
            
        depth(root)
        return self.ans

# Is Tree Balanced
# An empty tree is height-balanced. A non-empty binary tree T is balanced if: 
# 1) Left subtree of T is balanced 
# 2) Right subtree of T is balanced 
# 3) The difference between heights of left subtree and right subtree is not more than 1. 
#    The above height-balancing scheme is used in AVL trees. The diagram below shows two
#    trees, one of them is height-balanced and other is not. The second tree is not 
#    height-balanced because height of left subtree is 2 more than height of right subtree.
def height(root):
     
    # base condition when binary tree is empty
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1
 
# function to check if tree is height-balanced or not
def isBalanced(root):
     
    # Base condition
    if root is None:
        return True
 
    # for left and right subtree height
    lh = height(root.left)
    rh = height(root.right)
 
    # allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh - rh) <= 1) and isBalanced(
    root.left) is True and isBalanced( root.right) is True:
        return True
 
    # if we reach here means tree is not
    # height-balanced tree
    return False

# More optimised One : 
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.bal=True
        def dfs(node):
            if node is None:
                return 0;
            # first we go depth of tree that is dfs 
            left,right=dfs(node.left),dfs(node.right)
            if abs(left-right)>1:
                self.bal=False
            # This last return gives ans to its calling function 
            # when recursion is going up and subsequently
            # one by all information will return to root node.
            return max(left,right)+1
        dfs(root)
        return self.bal


# Max Path Sum TC : O(N)
def findMaxUtil(root):
     
    # Base Case
    if root is None:
        return 0
 
    # l and r store maximum path sum going through left
    # and right child of root respectively
    l = findMaxUtil(root.left)
    r = findMaxUtil(root.right)
     
    # Max path for parent call of root. This path
    # must include at most one child of root
    max_single = max(max(l, r) + root.data, root.data)
     
    # Max top represents the sum when the node under
    # consideration is the root of the maxSum path and
    # no ancestor of root are there in max sum path
    max_top = max(max_single, l+r+ root.data)
 
    # Static variable to store the changes
    # Store the maximum result
    findMaxUtil.res = max(findMaxUtil.res, max_top)
 
    return max_single

def findMaxSum(root):
    findMaxUtil.res = float("-inf")
    findMaxUtil(root)
    return findMaxUtil.res

# Symetric Mirror Images
def isMirror(root1, root2):
    # If both trees are empty, then they are mirror images
    if root1 is None and root2 is None:
        return True
 
    """ For two trees to be mirror images,
        the following three conditions must be true
        1 - Their root node's key must be same
        2 - left subtree of left tree and right subtree
          of the right tree have to be mirror images
        3 - right subtree of left tree and left subtree
           of right tree have to be mirror images
    """
    if (root1 is not None and root2 is not None):
        if root1.key == root2.key:
            return (isMirror(root1.left, root2.right)and
                    isMirror(root1.right, root2.left))
 
    # If none of the above conditions is true then root1
    # and root2 are not mirror images
    return False
 
 
def isSymmetric(root):
 
    # Check if tree is mirror of itself
    return isMirror(root, root)


    # Populate Next Right Pointer Tree
    class Solution:
    # @param root, a tree node
    # @return nothing

    # Just like Level Order Traversal
    def connect(self, root):
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            
            s = len(queue)
            
            while s:
                node = queue.popleft()
                if s != 1:
                    node.next = queue[0]
                else:
                    node.next = None
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
                s -= 1
            
        
        return root

# Search given key in BST
def search(root,key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
    # Key is smaller than root's key
    return search(root.left,key)

# Insert Node In A Binary Tree
def insert(root, Key):
    # code here
    if root is None:
        return Node(Key)
    else:
        if root.data == Key:
            return root
        # Key larger than root's key
        elif root.data < Key:
            if root.right:
                insert(root.right,Key)
            else:
                root.right = Node(Key)
        # Key is smaller than root's key
        elif root.data > Key:
            if root.left:
                insert(root.left,Key)
            else:
                root.left = Node(Key)
    return root


# Design Stack and find Getmin in O(1) and O(1)
class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            self.stack.append((val,min(val,self.stack[-1][1])))
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return -1                     
    def getMin(self) -> int:
        return self.stack[-1][1]


# Place k elements such that minimum distance is maximized
# Approach using BInary Search
def binary_serch(arr,k,n):
    arr.sort()
    left,right = 1,arr[n-1]
    while left < right:
        mid = left + (right - left)//2
        if feasible(mid,arr,k,n):
            ans = max(ans,mid)
            left = mid + 1
        else:
            right = mid
def feasible(mid,arr,k,n):
    pos,element = arr[0],1
    for i in range(1,n):
        if arr[i] - pos >= k:
            element += 1
            pos = arr[i]
            if element == k:
                return True 
    return False


# Boggle Words
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def bogglewords(board,m,n,words,res,visited,path):
            for i in range(m):
                for j in range(n):
                    dfs(i,j,m,n,board,words,visited,path)
            return res
        def dfs(i,j,m,n,board,words,visited,path):
            direction = [[-1,0],[0,-1],[1,0],[0,1]]
            visited[i][j] = True 
            path += board[i][j]
            if path in words:
                res.add(path)
            for x,y in direction:
                new_x = x + i 
                new_y = y + j
                if new_x < 0 or new_y < 0 or new_x >= m or new_y >= n or visited[new_x][new_y] == True:
                    continue;
                dfs(new_x,new_y,m,n,board,words,visited,path)
            visited[i][j] = False
        m = len(board)
        n = len(board[0])
        visited = [[False for j in range(n)]for i in range(m)]
        res = set()
        return bogglewords(board,m,n,words,res,visited,"")


# Search in Sorted Rotated Array
class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        # Complete this function
        low,high = 0,h
        while low < high:
            mid = low + (high - low)//2
            if A[mid] == key:
                return mid
            # Check whether left half is sorted or not
            if A[low] < A[mid]: # Yess sorted
                if A[low] <= key < A[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                if A[mid] <= key < A[high]:
                    low = mid + 1
                else:
                    high = mid
        return -1

# Vertical Order Traversal
def verticalOrder(self, root): 
    #Your code here
    from collections import defaultdict
    d = defaultdict(list)
    queue = [(root,0)]
    while queue:
        node,level = queue.pop(0)
        d[level].append(node.data)
        if node.left:
            queue.append((node.left,level - 1))
        if node.right:
            queue.append((node.right,level + 1))
    a = []
    for v in sorted(d.keys()):
        a.extend(d[v])
    return a


# Swap Kth node from beginning and end
 def countNodes(self):
        count = 0
        node = self.head
        while node.next is not None:
            count += 1
            node = node.next
        return count
     
    """
    Function for swapping kth nodes from
    both ends of linked list
    """
    def swapKth(self, k):
 
        # Count nodes in linked list
        n = self.countNodes()
 
        # check if k is valid
        if n<k:
            return
 
        """
        If x (kth node from start) and
        y(kth node from end) are same
        """
        if (2 * k - 1) == n:
            return
 
        """
        Find the kth node from beginning of linked list.
        We also find previous of kth node because we need
        to update next pointer of the previous.
        """
        x = self.head
        x_prev = Node(None)
        for i in range(k - 1):
            x_prev = x
            x = x.next
 
        """
        Similarly, find the kth node from end and its
        previous. kth node from end is (n-k + 1)th node
        from beginning
        """
        y = self.head
        y_prev = Node(None)
        for i in range(n - k):
            y_prev = y
            y = y.next
 
        """
        If x_prev exists, then new next of it will be y.
        Consider the case when y->next is x, in this case,
        x_prev and y are same. So the statement
        "x_prev->next = y" creates a self loop. This self
        loop will be broken when we change y->next.
        """
        if x_prev is not None:
            x_prev.next = y
 
        # Same thing applies to y_prev
        if y_prev is not None:
            y_prev.next = x
         
        """
        Swap next pointers of x and y. These statements
        also break self loop if x->next is y or y->next
        is x
        """
        temp = x.next
        x.next = y.next
        y.next = temp
 
        # Change head pointers when k is 1 or n
        if k == 1:
            self.head = y
         
        if k == n:
            self.head = x

# Check whether two nodes are cousin of each other or not
class Node:
     
    # Constructor to create a new Binary Tree
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def isSibling(root, a , b):
 
    # Base Case
    if root is None:
        return 0
 
    return ((root.left == a and root.right ==b) or
            (root.left == b and root.right == a)or
            isSibling(root.left, a, b) or
            isSibling(root.right, a, b))
 
# Recursive function to find level of Node 'ptr' in
# a binary tree
def level(root, ptr, lev):
     
    # Base Case
    if root is None :
        return 0
    if root == ptr:
        return lev
 
    # Return level if Node is present in left subtree
    l = level(root.left, ptr, lev+1)
    if l != 0:
        return l
 
    # Else search in right subtree
    return level(root.right, ptr, lev+1)
 
 
# Returns 1 if a and b are cousins, otherwise 0
def isCousin(root,a, b):
     
    # 1. The two nodes should be on the same level in
    # the binary tree
    # The two nodes should not be siblings(means that
    # they should not have the smae parent node
 
    if ((level(root,a,1) == level(root, b, 1)) and
            not (isSibling(root, a, b))):
        return 1
    else:
        return 0

# Sum of all left leaf nodes
def leftLeavesSum(root_node):
    s = 0
    # Complete this function
    def inorder(root_node,left):
        nonlocal s
        if root_node is None:
            return
        inorder(root_node.left,True)
        if root_node.left is None and root_node.right is None and left:
            s += root_node.data
        inorder(root_node.right,False)
        return s
    inorder(root_node,False)
    return s

# Jump Game II: 
class Solution:
    def minJumps(self, arr, n):
        #code here
        res = 0
        l = r = 0
        while r < len(arr) - 1:
            farthest = 0
            for i in range(l,r + 1):
                farthest = max(farthest,i + arr[i])
            l = r + 1
            r = farthest
            res += 1
            if r < l:
                return -1
        return res


# Using DP:
        dp = [float('inf') for i in range(len(arr)+1)]
        dp[0] = 0;
        for i in range(len(arr)):
            start = i;
            end = min(i + arr[i], len(arr) - 1);
            for j in range(start,end+1):
                dp[j] = min(dp[j], dp[start] + 1);
        if dp[len(arr) - 1] == len(arr):
            return -1
        else:
            return dp[len(arr) - 1];


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


# Construct Binary Tree Using Inorder and PreOrder
# Method I : O(N^2)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None 
        # The first element of preorder is root node 
        root = TreeNode(preorder[0])
        # Search this root node in inorder and from that position the tree will split to left and right
        mid = inorder.index(root.val)
        # We exclude mid in inoder as it is root node and already added in our new tree from preorder.
        buildTree(preorder[1:mid+1],inorder[:mid])
        buildTree(preorder[mid+1:],inoder[mid+1:])
        return root  

# Method II : Optimised : O(N)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre = 0
        def helper(left,right):
            nonlocal pre 
            if left > right:
                return 
            root = TreeNode(preorder[pre])
            pre += 1
            buildTree(left,d[root]-1)
            buildTree(d[root] + 1,right)
            return root
        d = { i : val for i,val in enumerate(inorder)}
        return helper(0,len(inorder)-1)



# Mirror Of a Tree
# TC : O(N)
# SC : O(N)
class Solution:
    def mirror(self,root):
        # Code here
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.mirror(root.left)
        self.mirror(root.right)


# Shortest unique Prefix for every Word
class Solution:
    def findPrefixes(self,arr, N):
        from collections import defaultdict
        prefixes=defaultdict(int)
        for word in arr:
            pref = ""
            for i in range(len(word)):
                pref += word[i]
                prefixes[pref]+=1
        # print(prefixes)
        
        out=[]
        for word in arr:
            result=word
            pref = ""
            for i in range(len(word)):
                pref += word[i]
                if prefixes[pref]==1:
                    result=pref
                    break
            out.append(result)
        return out


# Demolishing Robot
n = int(input())
mat = [[int(x) for x in input().split()] for _ in range(n)]
queue = [(0,0,0)]
flag = 0
visited = set()
visited.add((0,0))
while queue:
    a,b,count = queue.pop(0)
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    if mat[a][b] == 9:
        flag = 1
        print(count)
    for i,j in direction:
        new_x = i + a
        new_y = j + b
        if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m or (new_x,new_y) in visited or mat[new_x][new_y] == 0:
            continue;
        queue.append([new_x,new_y,count + 1])
        visited.add((new_x,new_y))
if flag == 0:
    print(-1)


# Find String In Grid
# Time complexity: O(R*C*8*len(str)). 
class Solution:
    def search2D(self, grid,row,col, word):
        dire = [[-1, 0], [1, 0], [1, 1],
                    [1, -1], [-1, -1], [-1, 1],
                    [0, 1], [0, -1]]
        # If first character of word doesn't match
        # with the given starting point in grid.
        if grid[row][col] != word[0]:
            return False
             
        # Search word in all 8 directions
        # starting from (row, col)
        for x, y in dire:
             
            # Initialize starting point
            # for current direction
            rd, cd = row + x, col + y
            flag = True
             
            # First character is already checked,
            # match remaining characters
            for k in range(1, len(word)):
                 
                # If out of bound or not matched, break
                if (0 <= rd <self.R and
                    0 <= cd < self.C and
                    word[k] == grid[rd][cd]):
                     
                    # Moving in particular direction
                    rd += x
                    cd += y
                else:
                    flag = False
                    break
             
            # If all character matched, then
            # value of flag must be false       
            if flag:
                return True
        return False
         
    # Searches given word in a given matrix
    # in all 8 directions   
    def searchWord(self, grid, word):
         
        # Rows and columns in given grid
        self.R = len(grid)
        self.C = len(grid[0])
         
        # Consider every point as starting point
        # and search given word
        res = []
        for row in range(self.R):
            for col in range(self.C):
                if grid[row][col] == word[0] and self.search2D(grid, row, col, word):
                    res.append((row,col))
        return res

# Number of Pair divisible by 4
class Solution:
    def count4Divisibiles(self, arr , n ): 
        from collections import defaultdict
        remainders = defaultdict(int)
        counts = 0
        for t in arr:
            if t % 4 == 0: # check if a % 60 and b % 60 == 0
                counts += remainders[t % 4]
            else:
                # Check if a % 60 + b % 60 = 60
                # if 60 - a % 60 in remainders that means there in pairs
                counts += remainders[4 - t % 4] 
            remainders[t % 4] += 1
        return counts


def letterCombinations(self,s):
    table = ["0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    listt = []
    def helper(s,table,curr,i):
        if len(curr) == len(s):
            listt.append(curr)
        for letter in table[s[i]]:
            helper(s,table,curr + letter,i + 1)
    return helper(s,table,"",0)

# Minimum time to take from Source to Destination
# Using bfs
n = int(input())
mat = [[int(x) for x in input().split()] for _ in range(n)]
def minpath(n,mat):
    p,q = 0,0
    for i in range(n):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                p,q = i,j
                break;
    queue = [(p,q,0)]
    flag = 0
    visited = set()
    visited.add((p,q))
    while queue:
        a,b,count = queue.pop(0)
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
        if mat[a][b] == 2:
            return count
        for i,j in direction:
            new_x = i + a
            new_y = j + b
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= len(mat[0]) or (new_x,new_y) in visited or mat[new_x][new_y] == 0:
                continue;
            queue.append([new_x,new_y,count + 1])
            visited.add((new_x,new_y))
print(minpath(n,mat))

# K-Largest Element In a Stream
class Solution:
    def kthLargest(self, k, arr, n):
        import heapq
        heap = []
        for i,num in enumerate(arr):
            if len(heap) < k:
                heapq.heappush(heap,num)
            elif num > heap[0]:
                heapq.heappushpop(heap,num)
            if len(heap) < k:
                arr[i] = -1
            else:
                arr[i] = heap[0]
        return arr



# Minimum Number of Taps to Open For Garden
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        arr = [0] * (n+1) 
        for i, r in enumerate(ranges):
            left, right = max(0, i - r), min(n, i + r)
            arr[left] = max(arr[left], right - left)
        # same code for jump game II after this
        res = 0
        l = r = 0
        while r < len(arr) - 1:
            farthest = 0
            for i in range(l,r + 1):
                farthest = max(farthest,i + arr[i])
            l = r + 1
            r = farthest
            res += 1
            if r < l:
                return -1
        return res
            
# Maximum Path Sum in matrix
n = int(input())
mat = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[float('-inf') for j in range(len(mat[0]))]for i in range(n)]
dp[0][0] = mat[0][0]
for i in range(1,n):
    dp[i][0] = dp[i-1][0] + mat[i][0]
for j in range(1,len(mat[0])):
    dp[0][j] = dp[0][j-1] + mat[0][j]
for i in range(1,n):
    for j in range(1,len(mat[0])):
        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + mat[i][j]
print(dp)
print(dp[-1][-1])


# Maximum Level Sum of Binary Tree
# TC : O(N)
# SC : O(H)
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is  None:
            return 0
        d = defaultdict(int)
        def helper(root,level,d):
            if root:
                d[level] += root.val
                helper(root.left,level + 1,d)
                helper(root.right,level + 1,d)
        helper(root,1,d)
        return max(d, key=d.get)

# Spilt the array into two subset such that their sum of difference be minimum
a  = LI()
n = I()
# MEthod I : TC : O(N) ; SC : O(N)
prefix,suffix = [0]*n,[0]*n
prefix[0] = a[0]
suffix[n-1] = a[n-1]
diff = float('inf')
for i in range(1,n):
    prefix[i] = prefix[i-1] + a[i]
    suffix[n-i-1] = suffix[n-i] + a[n-i -1]
for i in range(n):
    diff = min(diff,abs(prefix[i] - suffix[i+1]))
return diff

# Method II : TC : O(N), SC : O(1)
summ = sum(a)
diff = float('inf')
for num in arr:
    prefix_sum += num 
    diff = min(diff,abs(summ - prefix_sum - prefix_sum))
return diff


# Minimum Subset Sum Difference
# Partition Array to into two half such that their sum difference is mininmum
# TC : O(2^N)
def findMinRec(arr, n, sumCalculated,
               sumTotal):
  
    # If we have reached last element.
    # Sum of one subset is sumCalculated,
    # sum of other subset is sumTotal-
    # sumCalculated.  Return absolute
    # difference of two sums.
    if (n == 0):
        return abs((sumTotal - sumCalculated) - sumCalculated)
  
    # For every item arr[i], we have two choices
    # (1) We do not include it first set
    # (2) We include it in first set
    # We return minimum of two choices
    return min(findMinRec(arr, n - 1,sumCalculated+arr[n - 1],sumTotal),findMinRec(arr, n - 1,
                          sumCalculated, sumTotal))
  
# Returns minimum possible
# difference between sums
# of two subsets
def findMin(arr,  n):
    sumTotal = 0
    for i in range(n):
        sumTotal += arr[i]
    return findMinRec(arr, n,0, sumTotal)


# USing DP
def findMin(a, n):

    su = 0

    # Calculate sum of all elements
    su = sum(a)

    # Create an 2d list to store
    # results of subproblems
    dp = [[0 for i in range(su + 1)]
        for j in range(n + 1)]

    # Initialize first column as true.
    # 0 sum is possible
    # with all elements.
    for i in range(n + 1):
        dp[i][0] = True

    # Initialize top row, except dp[0][0],
    # as false. With 0 elements, no other
    # sum except 0 is possible
    for j in range(1, su + 1):
        dp[0][j] = False

    # Fill the partition table in
    # bottom up manner
    for i in range(1,n+1):
            for j in range(1,su + 1):
                if a[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-a[i-1]]
    # Initialize difference
    # of two sums.
    diff = sys.maxsize

    # Find the largest j such that dp[n][j]
    # is true where j loops from sum/2 t0 0
    for j in range(su // 2, -1, -1):
        if dp[n][j] == True:
            diff = su - (2 * j)
            break

    return diff


# Count Number of Palindromic Substring
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        n = len(s)
        count = 0
        for i in range(n - 1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if j -i == 1 or dp[i+1][j-1] == True:
                        dp[i][j] = True
                        count += 1
        return count + n

# Longest Palindromic Substring
 # Using Dp : TC : O(N^2) : SC : O(N^2)
 def longestPalindrome(self, s):
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        #filling out the diagonal by 1 because diagonal represent s[i:i] which is one element
        # and is palindrome with itself.
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]
            
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
                # j starts from the i location : to only work on the upper side of the diagonal 
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:  #if the chars mathces
                    # if len slicied sub_string is just two letter and if the characters are equal, we can say they are palindomr dp[i][j] =True 
                    #if the slicied sub_string is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]
        return longest_palindrom


# STandard DP Problem

# Longest Common Subsequence
# Method I : recursive : TC : O(2^N)
def lcs(self,x,y,s1,s2):
    if x == 0 or y == 0:
        return 0
    elif s1[x-1] == s2[y-1]:
        return 1 + self.lcs(x-1,y-1,s1,s2)
    else:
        return max(self.lcs(x-1,y,s1,s2),self.lcs(x,y-1,s1,s2))

# Method II : DP 
def lcs(m,n,X , Y):
    L = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    return L[m][n]


# Longesst Increasing Subsequence
# TC : O(N^2)
def longestSubsequence(self,a,n):
    lis = [1]*n
    for i in range(1,n):
        for j in range(i):
            if a[i] > a[j] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1
    return max(lis)


# Edit Distance
# MEthod I :recursion
# TC : O(3^N)
class Solution:
    def editDistance(self, s, t):
        m = len(s)
        n = len(t)
        def helper(s,t,m,n):
            if m == 0:
                return n
            elif n == 0:
                return m
            elif s[m-1] == t[n-1]:
                return helper(s,t,m-1,n-1)
            else:
                return 1 + min(helper(s,t,m-1,n-1),helper(s,t,m-1,n),helper(s,t,m,n-1))
        return helper(s,t,m,n)

# MEthod II : DP
    def editDistance(self, s, t):
        m = len(s)
        n = len(t)
        def helper(s,t,m,n):
            dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
 
    # Fill d[][] in bottom up manner
            for i in range(m + 1):
                for j in range(n + 1):
         
                    # If first string is empty, only option is to
                    # insert all characters of second string
                    if i == 0:
                        dp[i][j] = j    # Min. operations = j
         
                    # If second string is empty, only option is to
                    # remove all characters of second string
                    elif j == 0:
                        dp[i][j] = i    # Min. operations = i
         
                    # If last characters are same, ignore last char
                    # and recur for remaining string
                    elif s[i-1] == t[j-1]:
                        dp[i][j] = dp[i-1][j-1]
         
                    # If last character are different, consider all
                    # possibilities and find minimum
                    else:
                        dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                           dp[i-1][j],        # Remove
                                           dp[i-1][j-1])    # Replace
            return dp[m][n]
        return helper(s,t,m,n)

# Minimum Partition

# Method I: Recursive : TC : O(2^N)
def findMinRec(arr, i, sumCalculated,sumTotal):
    # If we have reached last element.
    # Sum of one subset is sumCalculated,
    # sum of other subset is sumTotal-
    # sumCalculated.  Return absolute
    # difference of two sums.
    if (i == 0):
        return abs((sumTotal - sumCalculated) -
                   sumCalculated)
    return min(findMinRec(arr, i - 1,
                          sumCalculated+arr[i - 1],
                          sumTotal),
               findMinRec(arr, i - 1,
                          sumCalculated, sumTotal))
def findMin(arr,  n):
    sumTotal = sum(arr)
    return findMinRec(arr, n, 0, sumTotal)


# Count No. of Hops
# Recursive Solution
def printCountDP(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return self.countWays(n-1) + self.countWays(n-2) + self.countWays(n-3)

# DP SOlution
def printCountDP(dist):
    count = [0] * (dist + 1)
     
    # Initialize base values. There is
    # one way to cover 0 and 1 distances
    # and two ways to cover 2 distance
    count[0] = 1
    if dist >= 1 :
        count[1] = 1
    if dist >= 2 :
        count[2] = 2
     
    # Fill the count array in bottom
    # up manner
    for i in range(3, dist + 1):
        count[i] = (count[i-1] +
                   count[i-2] + count[i-3])     
    return count[dist];


# Maximum Path Sum In a Matrix
class Solution:
    def maximumPath(self, n, mat):
        # code here
        maxsum = 0
        dp = [[0 for j in range(n+2)]for i in range(n+2)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1]) + mat[i-1][j-1]
                maxsum = max(maxsum,dp[i][j])
        return maxsum

# Coin Change : Maximum Number of Ways
class Solution:
    def count(self, S, m, n): 
        if n == 0:
            return 1
        if n < 0:
            return 0
        if m <= 0 and n >= 1:
            return 0
        else:
            return self.count(S,m-1,n) + self.count(S,m,n - S[m-1])

# DP Solution
        n=len(arr)
        dp=[[0 for j in range(s+1)] for i in range(n+1)]
        for i in range(n+1):
            for j in range(s+1):
                if i==0 and j==0:
                    dp[i][j]=1
                elif i==0:
                    dp[i][j]=0
                elif j==0:
                    dp[i][j]=1
        for i in range(1,n+1):
            for j in range(1,s+1):
                # If coin value is less than sum,we have to option
                # either to choose it or left it as it recurse for next part
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j]+dp[i][j-arr[i-1]]
                # If coin value is greater than we can't able to take in our ans.
                else:
                    dp[i][j]=dp[i-1][j]
        # print(dp)
        return dp[n][s]


# Knapsack 0-1
# Recursive
def knapSack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),knapSack(W, wt, val, n-1))

# USing DP
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]+ K[i-1][w-wt[i-1]],K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]


# Rod Cutting Problem
# Recursive Solution
def rodcutting (arr,n):
    if n <= 0:
        return 0
    maxi = float('-inf')
    for i in range(n):
        maxi = max(maxi,arr[i] + rodcutting(arr,n-i-1))
    return maxi 

# DP Solution : Memoization 
# Similar to Unbonded Knapsack
def rodcutting(price,n):
    def maximizeTheCuts(self,n,x,y,z):
        length = [x,y,z]
        l = len(length)
        dp = [[float('-inf') for j in range(n+1)] for i in range(l+1)]
        def helper(length,i,j):
            if i == 0:
                return float('-inf')
            if j == 0:
                return 0
            if dp[i][j] != float('-inf'):
                return dp[i][j]
            if length[i-1] > j:
                dp[i][j] = helper(length,i-1,j)
                return dp[i][j]
            else:
                # Two option either we cut rod or not.
                dp[i][j] = max(helper(length,i-1,j),1 + helper(length,i,j-length[i-1]))
                return dp[i][j]
        return helper(length,l,n)

# DP 
def cutRod(price, n):
    val = [0 for x in range(n+1)]
    val[0] = 0
    for i in range(1, n+1):
        max_val = INT_MIN
        for j in range(i):
             max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val
    return val[n]


# Similarity  with knapsack solution
int un_kp(int price[], int length[],
                    int Max_len, int n)
 
    # // The maximum price will be zero,
    # // when either the length of the rod
    # // is zero or price is zero.
    if (n == 0 || Max_len == 0):
        return 0;
    # // If the length of the rod is less
    # // than the maximum length, Max_lene will
    # // consider it.Now depending
    # // upon the profit,
    # // either Max_lene  we will take
    # // it or discard it.
    if (length[n - 1] <= Max_len)
    {
        t[n][Max_len]
            = max(price[n - 1]
                      + un_kp(price, length,
                           Max_len - length[n - 1], n),
                  un_kp(price, length, Max_len, n - 1));
    }
 
    # // If the length of the rod is
    # // greater than the permitted size,
    # // Max_len we will  not consider it.
    else
    {
        t[n][Max_len]
            = un_kp(price, length,
                              Max_len, n - 1);
    }
 
    # // Max_lene Max_lenill return the maximum
    # // value obtained, Max_lenhich is present
    # // at the nth roMax_len and Max_lenth column.
    return t[n][Max_len];

# MAximum Product Cutting
def maxProd(n):
     
    # Base cases
    if (n == 0 or n == 1):
        return 0
  
    # Make a cut at different places
    # and take the maximum of all
    max_val = 0
    for i in range(1, n - 1):
        max_val = max(max_val, max(i * (n - i), maxProd(n - i) * i))
  
    #Return the maximum of all values
    return max_val;

ll solve(ll n)
{
    //declare dp state of length n+1.
    ll dp[n + 1];

    //initialize base cases.
    dp[0] = dp[1] = 0;

    //iterate through different
    //size of rope length.
    for (ll i = 1; i <= n; i++) {

        ll res = INT_MIN;
        //iterate through cuts
        for(ll j = 1; j < i; j++)
            res = max(max(j * (i - j), j * dp[i - j]), res);
        //store res in dp[i] state.
        dp[i] = res;
    }
    //return maximum dp[n] value.
    return dp[n];

# Egg Dropping Problem
def eggproblem(n,k):
    #If there are no floors, then no trials
    # needed. OR if there is one floor, one
    # trial needed.
    if k == 0 or k == 1:
        return k
    # We need k trials for one egg
    # and k floors
    if n == 1:
        return k
    # Consider all droppings from 1st
    # floor to kth floor and return
    # the minimum of these values plus 1.
    mini = float('inf')
    for x in range(1,k+1):
        mini = min(mini,1 + max(eggproblem(n-1,x-1),eggproblem(n,k-x)))
    return mini


    # DP Solution
    # Additionally we think of like how many floors we can check with m move and K eggs.
    # Start with m == 1 we have 1 move and K eggs then maximum number of floor we can check
    # is 1 because after dropping 1 egg,1 move decreases and our number of move become 0 
    # So we can't check any other floor.
    # So we increase m to 2.Now egg(2,K)
    # If we have 2 move k egg we can get two result either egg break or not.
    # If egg break maximum number of floor we can check is  (m - 1,k - 1)
    # else (m - 1,k)
#He has turned the problem around from
# "How many moves do you need to check N floors if you have K eggs"
# to:
# "How many floors can you check given M moves available and K eggs".

# If you can solve this second problem than you can just increase the moves M one by one until you are able to check a number of floors larger or equal to the number N which the problem requires.
# He then defined
# dp[M][K] as the maximum number of floors that you can check within M moves given K eggs

# A move essentially is dropping an egg and it either breaks or doesn't break.
# Case A: The egg breaks and now you have spent 1 move (M=M-1) and also lost 1 egg (K=K-1). You can still check dp[M-1][K-1] floors, with your remaining eggs and moves.
# Case B: The egg remains and you only loose one move (M=M-1). You can still check dp[M-1][K] floors.
# Additionally you just checked a floor by dropping the egg from it.
# Therefore dp[M][K] = dp[M - 1][k - 1] + dp[M - 1][K] + 1
# As you can see we can easily calculate how many floors we can check in M moves if we know how many floors we can check in M-1 moves.

# However we not only have to know how many floors we can can check with one move less, but also how many we can check with one move and one egg less. Therefore we have to calculate how many moves we can check for all number off eggs from 1 to K.

# An example:
# N = 6 and K = 2
# Turn the problem around: How many floors can you check with 2 eggs and M moves:

# Solve for M=1, K=1,2
# you can only check 1 floor (since afterwards you have no more moves left)

# Solve for M=2, K=1
# Case A: Your egg breaks, you have no more eggs left and can check nothing. dp[M=1,K=0]=0
# Case B: your egg survives and you can use it to test an additional floor above the floor you just tested. dp[M=1,K=1]=1
# dp[2][1]=dp[1][0]+dp[1][1]+1=0+1+1=2

# Solve for M=2, K=2
# Case A: Your egg breaks: you have 1 move left and 1 egg. Since you know that the floor F where the eggs break is below the floor you just tested you can now check dp[M=1,K=1] floors below you, with only 1 move left you check 1 additional floor below. dp[M=1,K=1]=1
# Case B: Your eggs survives and you start to search above the current floor. dp[1][2] is still only 1 move and we can check 1 floor. dp[1][2]
# dp[2][2]=1+1+1=3

# Solve for M=3, K=1
# Case A: Your egg breaks and you are out of eggs, no chance to check anything anymore
# Case B: Your egg survives and you can use it for 2 more moves dp[2][1], which as we established above is enough to check 2 floors.
# dp[3][1]=0+2+1=3

# Solve for M=3, K=2
# Case A: Your egg breaks and you check dp[2][1]=2 additional floors
# Case B: Your egg survives and you check dp[2][2]=3 additional floors
# dp[3][2]=2+3+1=6

# As you can see 3 moves and 2 eggs allows you to check 6 floors. Which answers the original question how many moves you need to check 6 floors given 2 eggs,
# The answer is 3
      def superEggDrop(self, K, N):
        dp = [[0] * (K + 1) for i in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][K] >= N: return m


# Using Standard DP
def eggproblem(self,egg,floor):
    dp = [[0 for f in range(floor + 1)]for e in range(egg + 1)]
    for f in range(floors + 1):
        dp[1][f] = 1 
    for e in range(eggs + 1):
        for f in range(floors + 1):
            dp[e][f] = float('inf')
            for k in range(1,f + 1):
                c = 1 + max(dp[e-1][f-1],dp[e][f-k])
                dp[e][f] = min(dp[e][f],c)
    return dp[e][f]
 

# Cycle detection of graph using bfs : TC : O(N + E) ; SC : O(N)
def iscycle(v,adj,s):
    queue = [(s,-1)]
    v[s] = True
    while queue:
        node,parent = queue.pop(0)
        for itr in adj[node]:
            if v[itr] == False:
                queue.append((itr,node))
                v[itr] = True
            elif itr != parent:
                return True
    return False
adj = defaultdict(list)
for i in range(N):
    a,b = src,dest
    adj[a].append(b)
    adj[b].append(a)
v = [False]*(n + 1)
for i in range(1,N):
    if not v[i]:
        if iscycle(v,adj,i):
            return True
return False


# Bipartite Graph : If we can can color whole graph using only two color without having 
# adjacent colour as same.It is called bipartite graph.
def iscycle(color,adj,s):
    queue = [s]
    color[s] = True
    while queue:
        node = queue.pop(0)
        for itr in adj[node]:
            if color[itr] == False:
                queue.append(itr)
                color[itr] == True
            elif color[itr] == color[node]:
                return False 
    return True 
adj = defaultdict(list)
for i in range(N):
    a,b = src,dest
    adj[a].append(b)
    adj[b].append(a)
color = [False]*(n + 1)
for i in range(1,N):
    if not color[i]:
        if not isbiapartite(color,adj,i):
            return False
return True

# Topological Sorting 
# Using dfs
def findtopological(s,stack,vis,adj):
    vis[s] = True 
    for itr in adj[s]:
        if vis[itr] == False:
            findtopological(itr,stack,vis,adj)
    stack.append(s)
adj = defaultdict(list)
for i in range(N):
    a,b = src,dest
    adj[a].append(b)
vis = [False]*(N + 1)
stack = []
for i in range(1,N):
    if not vis[i]:
        findtopological(i,stack,vis,adj)
topo = []
while stack:
    topo.append(stack.pop(-1))
return topo 


# Remove K digits
# if number is in increasing order we have to remove last k element in order to get minimum element.
# so starting from left to right if top of stack is greater than current number that means
# it is peak element and we have to remove it in order to get minimum number.
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        # print(stack)
        # Case when number is in increasing order and no element is removed from stack.
        # then if k is greater than 0, remove last k element of stack.
        while k > 0:
            stack.pop()
            print(stack)
            k -= 1
        i = 0
        # If starting element is 0 we have to trim it.
        while i < len(stack) and stack[i] == '0':
            i += 1
        if len(stack[i:]):
            return "".join(stack[i:])
        else:
            return '0'

# Pacific Atlantic Water Flow 
# TC : O(N*M)
# SC : O(M*N)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        direc = [[-1,0],[0,-1],[1,0],[0,1]]
        m = len(heights)
        n = len(heights[0])
        vis_a = set()
        vis_b = set()
        def dfs(i,j,vis):
            if (i,j) in vis:
                return
            vis.add((i,j))
            for x,y in direc:
                new_x = x + i
                new_y = y + j
                if 0 <= new_x < m and 0 <= new_y < n:
                    if heights[i][j] <= heights[new_x][new_y]:
                        dfs(new_x,new_y,vis)
        for row in range(m):
            dfs(row,0,vis_a)
            dfs(row,n-1,vis_b)
        for col in range(n):
            dfs(0,col,vis_a)
            dfs(m-1,col,vis_b)
        return list(vis_a & vis_b)


# DFS TEMplate fro Solving Matrix PRoblem
# This is a DFS Template to solve matrix questions:

def dfs(matrix):
    # 1. Check for an empty graph.
    if not matrix:
        return []

    # 2. Initialize
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):
        # a. Check if visited
        if (i, j) in visited:
            return
        # b. Else add to visted
        visited.add((i, j))

        # c. Traverse neighbors.
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                # d. Add in your question-specific checks.
                traverse(next_i, next_j)

    # 3. For each point, traverse it.
    for i in range(rows):
        for j in range(cols):
            traverse(i, j)


# Using BFS : 
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        queue1,queue2 = [],[]
        vis_a,vis_b = set(),set()
        for i in range(m):
            queue1.append((i,0))
            queue2.append((i,n-1))
            vis_a.add((i,0))
            vis_b.add((i,n-1))
        for j in range(n):
            queue1.append((0,j))
            queue2.append((m-1,j))
            vis_a.add((0,j))
            vis_b.add((m-1,j))
        def bfs(queue,visited):
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            while queue:
                x, y = queue.pop(0)
                visited.add((x, y))
                for d in directions:
                    dx, dy = d[0] + x, d[1] + y
                    # check bounds
                    if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in visited and heights[dx][dy] >= heights[x][y]:
                        queue.append((dx, dy))
                        visited.add((dx, dy))
            return visited
        pacific_visited = bfs(queue1,vis_a)
        atlantic_visited = bfs(queue2,vis_b)
        return list(pacific_visited & atlantic_visited)


