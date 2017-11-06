class Tree(object):
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data
class solution:
    def __init__(self,root):
        self.root=root
        self.cnt=0
    def find(self):
        root=self.root
        def postorder(root):
            if root.left and root.right:
                left=postorder(root.left)
                right=postorder(root.right)
                self.cnt+=abs(left-right)
                return max(left,right)+root.val
            else:
                return root.val

        postorder(root)
        return self.cnt

tree=Tree(1)
tree.left=Tree(2)
tree.right=Tree(11)
tree.left.left=Tree(3)
tree.left.right=Tree(4)
case=solution(tree)
print case.find()