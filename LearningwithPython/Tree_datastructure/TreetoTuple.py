'''
Define a function tree_to_tuple that converts a binary tree into a tuple representing the same tree. 
Eg. tree_to_tuple converts the tree created above to the tuple ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))). 
TreeNode: Class for intializing tree node with key vlaues.
parse_tuple(data):parse the tree tuple and returns the root node of the tree.
tree_to_tuple(node):takes input as root node of the tree and returns the desired tuple represenatation.
tree:root node returned by the parse_tuple fucntion.
tu:tuple returned by the tree_to_tuple fucntion
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

def tree_to_tuple(node):
   #one of the left or right node is None
    if node is None:
        return None 
    #leaf node
    if node.left is None and node.right is None:
        return node.key

    treeTuple = tree_to_tuple(node.left),node.key,tree_to_tuple(node.right)#recursion 

    return treeTuple

tree=parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
tu= tree_to_tuple(tree)
print(tu)
#output:((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
