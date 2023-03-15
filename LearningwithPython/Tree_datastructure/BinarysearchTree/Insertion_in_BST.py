'''
We use the BST-property to perform insertion efficiently: 
    • Starting from the root node, we compare the key to be inserted with the current node's key 
    • If the key is smaller, we recursively insert it in the left subtree (if it exists) or attach it as as the left child if no left subtree exists. 
    • If the key is larger, we recursively insert it in the right subtree (if it exists) or attach it as as the right child if no right subtree exists. 
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
tree = insert(None, jadhesh.username, jadhesh)
insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)

tree2 = insert(None, aakash.username, aakash)
insert(tree2, biraj.username, biraj)
insert(tree2, hemanth.username, hemanth)
insert(tree2, jadhesh.username, jadhesh)
insert(tree2, siddhant.username, siddhant)
insert(tree2, sonaksh.username, sonaksh)
insert(tree2, vishal.username, vishal)

print(tree.left.left.parent.key,tree.left.left.parent.value)
#Output:biraj User(username='biraj', name='Biraj Das', email='biraj@example.com')
