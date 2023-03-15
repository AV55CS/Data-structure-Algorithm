'''
we need to store user objects with each key in our BST.let’s define a new class BSTNode to represent the nodes of our tree. 
Apart from having properties key, left and right, we'll also store a value and pointer to the parent node.
 
'''

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None 
        
class User:
    def __init__(self, username, name, email):				Fig:tree
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

#Here keys are  usernames and values are object representation
tree = BSTNode(jadhesh.username, jadhesh)
tree.left = BSTNode(biraj.username, biraj)
tree.right = BSTNode(sonaksh.username, sonaksh)
tree.left.left=BSTNode(aakash.username, aakash)
tree.left.right = BSTNode(hemanth.username, hemanth)
tree.right.left=BSTNode(siddhant.username, siddhant)
tree.right.right=BSTNode(vishal.username, vishal)
'''
This is similar to the way how we  manually created  the binary tree and linked it .
Therefore we need to  define  some helpful function to perform operations :insert, update , find,list_all automated .
'''
