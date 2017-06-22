# Importing various classes
from datetime import datetime

# Defining a class Spy
class Spy:
    # Constructor for initializing the variables
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

# Defining a class ChatMessage
class ChatMessage:
    # Constructor for initializing variables of this class
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy('Udit','Mr',20,5.0)

# Defining few friends as object of Spy class
friend_one = Spy('Paras', 'Mr.',27, 2.9 )
friend_two = Spy('Mayur', 'Ms.', 29, 4.1)
friend_three = Spy('Vivek', 'Dr.', 45, 5.0)

# Defining list of friends
friends = [friend_one, friend_two, friend_three]


