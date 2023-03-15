'''
List the nodes:

function to retrieve all the key-values pairs stored in a BST in the sorted order of keys.
The nodes can be listed in sorted order by performing an inorder traversal of the BST.

Ouput:
[('aakash', User(username='aakash', name='Aakash Rai', email='aakash@example.com')), 
 ('biraj', User(username='biraj', name='Biraj Das', email='biraj@example.com')), 
 ('hemanth', User(username='hemanth', name='Hemanth Jain', email='hemanth@example.com')),
 ('jadhesh', User(username='jadhesh', name='Jadhesh Verma', email='jadhesh@example.com')), 
 ('siddhant', User(username='siddhant', name='Siddhant Sinha', email='siddhant@example.com')), 
 ('sonaksh', User(username='sonaksh', name='Sonaksh Kumar', email='sonaksh@example.com')), 
 ('vishal', User(username='siddhant', name='Siddhant Sinha', email='siddhant@example.com'))]


Time complexity ="O(N)" and space complexity ="O(N)"
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
tree = insert(None, jadhesh.username, jadhesh)
insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)
print(list_all(tree))
