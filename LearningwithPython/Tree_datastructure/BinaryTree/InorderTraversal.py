'''
A traversal refers to the process of visiting each node of a tree exactly once. Visiting a node generally refers to adding the node's key to a list. 
TreeNode:class for creating and initialzing tree nodes
traverse_in_order(node):take root as parameter and return the list of visited keys 
parse_tuple(data):reads tree tuple and returns root node of the created tree
tree=root node of the created tree

Inorder traversal											
    1. Traverse the left subtree recursively inorder. 
    2. Traverse the current node. 
    3. Traverse the right subtree recursively inorder. 
   
'''

class TreeNode:  
  def __init__(self, key):
        self.key = key
        self.left = None#left pointer 
        self.right = None#right pointer

def parse_tuple(data):							
    #print(type(data))
    if isinstance(data, tuple) and len(data) == 3:				
        node = TreeNode(data[1])#root
        node.left = parse_tuple(data[0])#left 
        node.right = parse_tuple(data[2])#right
    elif data is None:
        node = None
    else:
        node = TreeNode(data)#if single node (leaf)		
    return node	
def traverse_in_order(node):
    if node is None: 
        return []
    return(traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right))

tree=parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(traverse_in_order(tree))
#Output:[1, 3, 2, 3, 4, 5, 6, 7, 8]
