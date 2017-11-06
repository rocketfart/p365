class Node():
    def __init__(self,data):
        self.val=data
        self.right=None
        self.left=None
        self.parent=None

def find(p,q,root):
    visited=set()
    while p or q:
        if p:
            if p in visited:
                return p
            visited.add(p)
            p=p.parent

        if q:
            if q in visited:
                return q
            visited.add(q)
            q=q.parent

    return None


root = Node(20)

root.left = Node(8)
root.left.parent=root
root.right = Node(22)
root.right.parent=root
root.left.left = Node(4)
root.left.left.parent=root.left
root.left.right = Node(12)
root.left.right.parent=root.left
root.left.right.left = Node(10)
root.left.right.left.parent=root.left.right
root.left.right.right = Node(14)
root.left.right.right.parent=root.left.right
p,q=root.left.right.left,root.left
print find(p,q,root).val