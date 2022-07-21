class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m > 0:
            def maxareaunderhistogram(n,arr):
                stack = list() 
                max_area ,area= 0 ,0
                index = 0
                while index < len(arr): 
                    if len(stack)==0 or (arr[stack[-1]] <= arr[index]): 
                        stack.append(index) 
                        index += 1 
                    else: 
                        top_of_stack = stack.pop() 
                        if len(stack)!=0:
                            area = arr[top_of_stack] *(index - stack[-1] - 1)
                        else:
                            area = arr[top_of_stack] *index 
                        max_area = max(max_area, area) 
                while stack: 
                    top_of_stack = stack.pop()  
                    if len(stack)!=0:
                        area = arr[top_of_stack] *(index - stack[-1] - 1)
                    else:
                        area = arr[top_of_stack] *index 
                    max_area = max(max_area, area) 
                return max_area
            n = len(matrix[0])
            arr = [0]*n
            ans = 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == '0':
                        arr[j] = 0
                    else:
                        arr[j] += int(matrix[i][j])
                ans = max(ans,maxareaunderhistogram(n,arr))
            print(arr)
            return ans
        else:
            return 0
