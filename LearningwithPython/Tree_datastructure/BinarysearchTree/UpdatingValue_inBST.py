'''
        
Updating a value in a BST
function to update the value associated with a given key within a BST
We can use find to locate the node to be updated, and simply update it's value.
    • We will use find function to  get the desired key to be updated.
    • If key is found we set the updated value .
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

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)
        
def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value
        

tree = insert(None, jadhesh.username, jadhesh)
insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)

#Output:('hemanth', User(username='hemanth', name='Hemanth Jain', email='hemanth@example.com'))
update(tree, 'hemanth', User('hemanthk', 'Hemanth Kumar', 'hemanthk@example.com'))
node = find(tree, 'hemanth')#checking the updated node
print(node.value)	
#Output:User(username='hemanthk', name='Hemanth kumar', email='hemanthk@example.com')
