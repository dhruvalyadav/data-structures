from collections import deque

class Node:
    def __init__(self, value):
        self.info = value
        self.left = None
        self.right = None
class tree:
    def __init__(self,branch,leaf):
        self.branch=branch
        self.leaf=leaf
    
class Btree:
    def __init__(self):
        self.root = None

    def create_tree(self):
        self.root = Node('A')
        self.root.left = Node('B')
        self.root.right = Node('C')
        self.root.left.left = Node('D')

    def display(self):
        def _display(p, level):
            if p:
                _display(p.right, level + 1)
                print("    " * level + str(p.info))
                _display(p.left, level + 1)
        _display(self.root, 0)
        print()

    def preorder(self):
        def _pre(p):
            if p:
                print(p.info, end=" ")
                _pre(p.left)
                _pre(p.right)
        _pre(self.root)
        print()

    def inorder(self):
        def _in(p):
            if p:
                _in(p.left)
                print(p.info, end=" ")
                _in(p.right)
        _in(self.root)
        print()

    def postorder(self):
        def _post(p):
            if p:
                _post(p.left)
                _post(p.right)
                print(p.info, end=" ")
        _post(self.root)
        print()

    def levelorder(self):
        if not self.root:
            print("Empty")
            return
        q = deque([self.root])
        while q:
            p = q.popleft()
            print(p.info, end=" ")
            if p.left: q.append(p.left)
            if p.right: q.append(p.right)
        print()

    def height(self):
        def _height(p):
            if not p: return 0
            return 1 + max(_height(p.left), _height(p.right))
        return _height(self.root)
bt = Btree()
bt.create_tree()
print("Tree:")
bt.display()
print("Preorder:")
bt.preorder()
print("Inorder:")
bt.inorder()
print("Postorder:")
bt.postorder()
print("Level Order:")
bt.levelorder()
print("Height:", bt.height())
