class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.left=left
        self.right=right


# 先序遍历，弹栈+print+压右+压左，循环，头左右
class PreOrder:
    def preSort(self,root:TreeNode):
        ans = [];stack=[]
        if root:stack.append(root)
        while stack:
            root=stack.pop()
            ans.append(root.val)
            if root.right:stack.append(root.right)
            if root.left:stack.append(root.left)
        return ans

# 后序遍历，弹栈+收集栈+压左+压右，循环，收集栈出栈为逆序，头右左-》左右头
# 先序遍历压栈顺序相反，最后弹栈逆序
class AfterOrder:
    def afterSort(self,root:TreeNode):
        ans= [];stack1=[];stack2=[]
        if root:stack1.append(root)
        while stack1:
            root = stack1.pop()
            stack2.append(root)
            if root.left:stack1.append(root.left)
            if root.right:stack1.append(root.right)
        for node in stack2:
            ans.append(node.val)
        return ans


# 中序遍历，先把子树左边界全部压栈，弹出并打印，取出右节点，在全压入左边界，循环
class Inorder:
    def inOrder(self,root:TreeNode):
        ans = [];stack=[]
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ans.append(root.val)
                root=root.right
        return ans


# 验证二叉搜索树，树DP问题，套模板
class isBST:
    def __init__(self,isbst,min_=-1,max_=-1):
        self.isbst = isbst
        self.min_=min_
        self.max_=max_

class isValidBST:
    def isValidBST(self, root:TreeNode):
        ans = self.treeDp(root)
        return ans.isbst

    def treeDp(self,root:TreeNode):
        if not root:return None
        isleft = self.treeDp(root.left)
        isright = self.treeDp(root.right)
        if (isleft and not isleft.isbst)or(isright and not isright.isbst):return isBST(False)
        if (isleft and root.val<=isleft.max_) or (isright and root.val>=isright.min_):return isBST(False)        
        return isBST(True,isleft.min_ if isleft else root.val,isright.max_ if isright else root.val)

# 验证平衡二叉树，树dp问题，套模板
class isBTree:
    def __init__(self,isbalance:bool,depth=0) -> None:
        self.isbalance=isbalance
        self.depth = depth

class IsBalanceTree:
    def isBalance(self,root):
        ans = self.isBalanceTree(root)
        return ans.isbalance

    def isBalanceTree(self,root:TreeNode):
        if not root:return isBTree(True,0)
        leftBT = self.isBalanceTree(root.left)
        rightBT = self.isBalanceTree(root.right)
        if (not (leftBT.isbalance and rightBT.isbalance)) or abs(leftBT.depth-rightBT.depth)>1:
            return isBST(False)
        depth = max(leftBT.depth,rightBT.depth)+1
        return isBST(True,depth)


