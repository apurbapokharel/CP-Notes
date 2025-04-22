from collections import defaultdict, deque

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self, level=0, prefix="Root: "):
        ret = "  " * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__repr__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__repr__(level + 1, "R--- ")
        return ret

class Traversals:
    def dfs(self, root):
        self.res = []
        def dodfs(root):
            if not root:
                return
            self.res.append(str(root.val))
            dodfs(root.left)
            dodfs(root.right)
        dodfs(root)
        print("-".join(self.res))

    def bfs(self, root):
        if not root:
            return ""
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            res.append(str(node.val))
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print("-".join(res))

    def pre_order(self, root):
        self.dfs(root)

    def in_order(self, root):
        self.res = []
        def doit(root):
            if not root:
                return
            doit(root.left)
            self.res.append(str(root.val))
            doit(root.right)
        doit(root)
        print("-".join(self.res))

    def post_order(self, root):
        self.res = []
        def doit(root):
            if not root:
                return
            doit(root.left)
            doit(root.right)
            self.res.append(str(root.val))
        doit(root)
        print("-".join(self.res))
    
    def reverse_pre_order(self, root):
        pass
    
    def reverse_in_order(self, root):
        pass
    
    def reverse_post_order(self, root):
        pass    
    
    def bfs_liked_list(self, root):
        if not root:
            return None

        queue = deque([root])
        prev = None  
    
        while queue:
            current = queue.popleft()
            
            if prev:
                prev.right = current  
            prev = current
            left, right = current.left, current.right
            current.left = None 
    
            if left: 
                queue.append(left)
            if right:  
                queue.append(right)
    
        return root 
            
        
    def pre_order_list(self, root):
        def doit(root):
            if not root:
                return
            left, right = root.left, root.right
            leftChild = doit(left)
            rightChild = doit(right)
            root.left = None
            
            if leftChild:
                root.right = left
                leftChild.right = right
            
            return rightChild if rightChild else leftChild if leftChild else root
        doit(root)
        return root
        
    def in_order_list(self, root):
        def doit(root):
            if not root:
                return (None, None)
            left, right = root.left, root.right
            (llm, lrm) = doit(left)
            (rlm, rrm) = doit(right)
            
            root.left = None
            if left and right:
                lrm.right = root
                root.right = rlm
                return (llm, rrm)
            
            elif left and not right:
                lrm.right = root
                return (llm, root)
            
            elif not left and right:
                root.right = rlm
                return (root, rrm)

            else:
                return (root, root)
            
            # CLEANER CODE
            # if lrm:
            #     lrm.right = root
            # else:
            #     llm = root  
            # if rlm:
            #     root.right = rlm
            # else:
            #     rrm = root  
            # return (llm, rrm)
            
        a, _ = doit(root)
        return a
        
    def post_order_list(self, root):
        def doit(root):
            if not root:
                return (None, None)
            left, right = root.left, root.right
            (llm, lrm) = doit(left)
            (rlm, rrm) = doit(right)
            
            root.left = None
            root.right = None
            if left and right:
                lrm.right = rlm
                rrm.right = root
                return (llm, root)
            
            elif left and not right:
                lrm.right = root
                return (llm, root)
            
            elif not left and right:
                rrm.right = root
                return (rlm, root)

            else:
                return (root, root)
            
        a, _ = doit(root)
        return a
    
tree1 = Tree(1, 
             Tree(2, Tree(4), Tree(5)), 
             Tree(3, Tree(6), Tree(7))
            )
            
tree2 = Tree(10, 
             Tree(5, None, Tree(8, Tree(7))), 
             Tree(15, Tree(12))
            )
            
traveral = Traversals()
# traveral.dfs(tree1) 
traveral.bfs(tree1)
# traveral.pre_order(tree1)
# traveral.in_order(tree2)
# traveral.post_order(tree1)
bfs_list = traveral.bfs_liked_list(tree1)
# print(bfs_list)
# traveral.dfs(bfs_list)
tree1 = Tree(1, 
             Tree(2, Tree(4), Tree(5)), 
             Tree(3, Tree(6), Tree(7))
            )
            
pre_order = traveral.pre_order_list(tree1)
print(pre_order)

tree1 = Tree(1, 
             Tree(2, Tree(4), Tree(5)), 
             Tree(3, Tree(6), Tree(7))
            )
in_order = traveral.in_order_list(tree1)
print(in_order)     

tree1 = Tree(1, 
             Tree(2, Tree(4), Tree(5)), 
             Tree(3, Tree(6), Tree(7))
            )
post_order = traveral.post_order_list(tree1)
print(post_order) 
            

