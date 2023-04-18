

class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
 
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
 
    def insert(self, val):
        if val < self.data:
            if self.left:
                self.left.insert(val)
            else:
                self.left = Tree(val)
        elif val > self.data:
            if self.right:
                self.right.insert(val)
            else:
                self.right = Tree(val)

#!t = Tree(Tree("a", "b"), Tree("c", "d"))
