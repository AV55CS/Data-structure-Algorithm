'''Problem
QUESTION 1: As a senior back end engineer you are tasked with developing a fast in-memory data structure to manage profile information 
(username, name and email) for 100 million users. It should allow the following operations to be performed efficiently:
    1. Insert the profile information for a new user. 
    2. Find the profile information of a user, given their username 
    3. Update the profile information of a user, given their username 
    4. List all the users of the platform, sorted by username 
    You can assume that usernames are unique. 
    
    
The operations insert, find, update involves iterating over a list of users, in the worst case, they may take up to N iterations to return a result,
where N is the total number of users. list_all however, simply returns the existing internal list of users. 
Thus, the time complexities of the various operations are:
    1. Insert: O(N) 
    2. Find: O(N) 
    3. Update: O(N) 
    4. List: O(1) 
   
 Algorithm:
 
 The various functions can be implemented as follows:
    1. Insert: Loop through the list and add the new user at a position that keeps the list sorted. 
    2. Find: Loop through the list and find the user object with the username matching the query. 
    3. Update: Loop through the list, find the user object matching the query and update the details 
    4. List: Return the list of user objects. 
We can use the fact usernames, which are are strings can be compared using the <, > and == operators in Python.
    
'''    
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
class UserDatabase:

    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):

            # Find the first username greater than the new user's username

            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        (target.name, target.email) = (user.name, user.email)

    def list_all(self):
        return self.users
#Insert
database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)
#update
database.update(User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'))
#find
user = database.find('siddhant')
'''output: User(username='siddhant', name='Siddhant U', email='siddhantu@example.com')'''
#Listall
database.list_all()
'''
output:
[User(username='aakash', name='Aakash Rai', email='aakash@example.com'),
User(username='hemanth', name='Hemanth Jain', email='hemanth@example.com'),
User(username='siddhant', name='Siddhant U', email='siddhantu@example.com')]
'''
