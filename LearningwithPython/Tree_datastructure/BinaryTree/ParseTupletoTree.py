'''
data :tuple respresenation of tree

parse_tuple(data):takes tuple represenation as input and returns root node of tree.ie converts tuple to tree
The parse_tuple creates a new root node when a tuple of size 3 as an the input. Interestingly, to create the left and right subtrees for the node, 
the parse_tuple function invokes itself. This technique is called recursion. The chain of recursive calls ends when parse_tuple encounters a number or None
as input. 

isinstance() returns:
True :if the object is an instance or subclass of a class or any element of the tuple
False: otherwise
'''

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
tree1 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
tree2 = parse_tuple(((None,4,None), 3, (None, 5, None)))
#we can verify our tree with various print statements
print(tree2.key)
#output:3
print(tree1.left.left.key, tree1.left.right, tree1.right.left.key, tree1.right.right.key)
#output:(1, None, 3, 7)
