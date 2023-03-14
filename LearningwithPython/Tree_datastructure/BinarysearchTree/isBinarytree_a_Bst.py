'''
Binary Search Tree (BST)
A binary search tree or BST is a binary tree that satisfies the following conditions:
    1. The left subtree of any node only contains nodes with keys less than the node's key 
    2. The right subtree of any node only contains nodes with keys greater than the node's key 
It follows from the above conditions that every subtree of a binary search tree must also be a binary search tree.

is_bst(node):returns (true/flase,minimum key,maximum key).true/false indicates wether a binary tree is BST or not.min key in tree ,maximum key in tree.

remove_none(nums):return list without None.

TreeNode:Creating and Initialzing tree nodes.
parse_tuple(data):returns  root node of a tree .
'''

class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

def remove_none(nums):
    return [x for x in nums if x is not None]
def is_bst(node):
    if node is None:
        return True, None, None
    is_bst_l, min_l, max_l = is_bst(node.left)			
    is_bst_r, min_r, max_r = is_bst(node.right)
    is_bst_node = (is_bst_l and is_bst_r) and (max_l is None or node.key > max_l) and (min_r is None or node.key < min_r)
    min_key = min(remove_none([min_l, node.key, min_r]))			
    max_key = max(remove_none([max_l, node.key, max_r]))			
    #print(node.key, min_key, max_key, is_bst_node)
    return is_bst_node, min_key, max_key
  
tree1 = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
tree2 = TreeNode.parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
print(is_bst(tree1))
print(is_bst(tree2))
@Output:(False, 1, 8)		  #False indicates it is not BST
#Output:(True, 'aakash', 'vishal') #True indicates valid BST
