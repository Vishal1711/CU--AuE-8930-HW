class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):

        ans = 0
        subSum= sum-root.val

        if(subSum == 0 and root.left == None and root.right == None):
            return True

        if root.left is not None:
            ans = ans or self.__class__.hasPathSum(self,root.left, subSum)
        if root.right is not None:
            ans = ans or self.__class__.hasPathSum(self,root.right, subSum)

        return ans


sum = 22
root=TreeNode(5)
root.left=TreeNode(4)
root.right=TreeNode(8)
root.left.left=TreeNode(12)
root.left.left.right=TreeNode(2)
root.left.left.left=TreeNode(7)
root.right.left=TreeNode(13)
root.right.right=TreeNode(4)
root.right.left.left=TreeNode(1)



sol=Solution()

if sol.hasPathSum(root, sum):
    print (f"There is a root-to-leaf path with sum {sum}")
else:
    print (f"There is no root-to-leaf path with sum {sum}")
