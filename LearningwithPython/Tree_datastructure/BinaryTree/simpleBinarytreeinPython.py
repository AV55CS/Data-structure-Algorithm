'''
Implement a binary tree using Python, and show its usage with some examples.
TreeNode:class for creating nodes of tree and intializing it.
'''
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None#left pointer 
        self.right = None#right pointer
 '''Manually creating Nodes and Linking them '''
#creating nodes
node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)
#linking manually the nodes
node0.left = node1
node0.right = node2
# We can create a new variable tree which simply points to the root node, and use it to access all the nodes within the tree.
#tree is our root node
tree = node0
print(tree.key,tree.left.key,tree.right.key)
OUTPUT:(3, 4, 5)
