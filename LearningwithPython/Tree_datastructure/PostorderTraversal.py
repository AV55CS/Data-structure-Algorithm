'''
TreeNode:class for creating and initialzing tree nodes

traverse_post_order(node):take root as parameter and return the list of visited keys 

parse_tuple(data):reads tree tuple and returns root node of the created tree

tree=root node of the created tree.

Postorder traversal
    1. Traverse the left subtree recursively preorder. 
    2. Traverse the right subtree recursively preorder. 
    3. Traverse the current node. 
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
def traverse_post_order(node):
    if node is None: 
        return []
    return(traverse_post_order(node.left) + traverse_post_order(node.right)+ [node.key] )
tree=parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(traverse_post_order(tree))
#Output:[1, 3, 4, 3, 6, 8, 7, 5, 2]
