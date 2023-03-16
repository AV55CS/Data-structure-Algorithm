'''
Recursive strategy:
    1. Ensure that the left subtree is balanced. 
    2. Ensure that the right subtree is balanced. 
    3. Ensure that the difference between heights of left subtree and right subtree is not more than 1.
    
TreeNode:class for creating and initialzing tree nodes
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
    
def is_balanced(node):								
    if node is None:
        return True, 0
    if node.left is None and node.right is None:
        return True, 0
        
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1		 
    height = 1 + max(height_l, height_r)
    return balanced, height
tree1 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
tree2 = parse_tuple(((None,4,None), 3, (None, 5, None)))
print(is_balanced(tree1),is_balanced(tree2))

