'''
data :tuple respresenation of tree

parse_tuple(data):takes tuple represenation as input and returns root node of tree.ie converts tuple to tree

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
tree2 = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
tree3 = parse_tuple(((None,4,None), 3, (None, 5, None)))
#we can verify our tree with various print statements
print(tree2.key)
#output:3
print(tree2.left.left.key, tree2.left.right, tree2.right.left.key, tree2.right.right.key)
#output:(1, None, 3, 7)
