'''
Levels: height of the tree + 1

TreeNode:class for creating and initialzing tree nodes
level(node):take root as parameter and return the level of the binary tree.
parse_tuple(data):reads tree tuple and returns root node of the created tree
tree=root node of the created tree

'''
class TreeNode:  
  def __init__(self, key):
        self.key = key
        self.left = None#left pointer 
        self.right = None#right pointer

def parse_tuple(data):							
    if isinstance(data, tuple) and len(data) == 3:				
        node = TreeNode(data[1])#root
        node.left = parse_tuple(data[0])#left 
        node.right = parse_tuple(data[2])#right
    elif data is None:
        node = None
    else:
        node = TreeNode(data)#if single node (leaf)		
    return node	
def level(node):
    if node is None:
        return 0
    elif node.left is None and node.right is None:
        return 1
    return 1+max(level(node.left), level(node.right))
tree=parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(level(tree))
#output:4

