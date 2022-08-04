from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    sums = []
    def search(root: TreeNode, sum: int):
        if root is None:
            return

        if root.left is None and root.right is None:
            sums.append(sum + root.val)
            return

        search(root.left, sum + root.val)
        search(root.right, sum + root.val)

    search(root, 0)
    return True if targetSum in sums else False

root = TreeNode(1,TreeNode(2), TreeNode(3))
print(hasPathSum(None, 3))