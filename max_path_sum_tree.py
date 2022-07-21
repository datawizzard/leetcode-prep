import sys
sys.stdin=open('input.txt','r')
sys.stdout=open('output.txt','w')
class Solution:
    def dfs(self,node):
        if not node:
            return 0
        left=self.dfs(node.left)
        right=self.dfs(node.right)
        #here we are considering three cases
        #case1: if current node is in the branch with maximum sum
        #(current node is not root node but a member node)

        #case2: if current node is the root of branch with maximum sum

        #case3: if current node is not at all present in the
        # branch with maximum sum(neither as root node not as member node)
        # then compare result in each recursion
                sum1= max(max(right, left) + node.val, node.val) #case1
        sum2= max(sum1,right+left+node.val )             #case2
        self.res= max(sum2,self.res)                     #case3
        return sum1      
    def maxPathSum(self, root: TreeNode) -> int:
        self.res=float('-inf')
        self.dfs(root)
        return self.res