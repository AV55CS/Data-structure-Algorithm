'''
We first perform an inorder traversal, then create a balanced BST using the function defined .
class BSTNode:Creating and Initializing nodes of bst
class User:initializing and representing objects with 
insert(node, key, value):insert usernames as key and representation of objects as value in our program
list_all(node):returning all the nodes using Inorder Traversal
make_balanced_bst(data, lo=0, hi=None, parent=None): using binary search logic with sorted order of keys 
balance_bst(node):internally call make_balalnce_bst with list_all ,return root node of tree


'''
class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None 
        
class User:
    def __init__(self, username, name, email):			
        self.username = username
        self.name = name
        self.email = email   
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    def __str__(self):
        return self.__repr__()

      
#creating object of user class
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

def insert(node, key, value):
# new node at starting time
    if node is None:
        node = BSTNode(key, value)
#adding node to the left and setting parent node			
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
#adding node to right and setting parent node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node
    
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)
    
    
def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None							
    
    mid = (lo + hi) // 2
    key, value = data[mid]
    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)
    
    return root
def balance_bst(node):
    return make_balanced_bst(list_all(node))
    
#worst case BST    
tree = insert(None, aakash.username, aakash)
insert(tree, biraj.username, biraj)
insert(tree, hemanth.username, hemanth)
insert(tree, jadhesh.username, jadhesh)
insert(tree, siddhant.username, siddhant)
insert(tree, sonaksh.username, sonaksh)
insert(tree, vishal.username, vishal)
tree=balance_bst(tree)
print(tree.left.left.parent.key)


