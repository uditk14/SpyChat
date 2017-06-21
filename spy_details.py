from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy('Udit','Mr',20,5.0)


friend_one = Spy('Ram', 'Mr.',27, 4.9 )
friend_two = Spy('Shyam', 'Ms.', 39, 2.1)
friend_three = Spy('Driving', 'Dr.', 45, 3.7)


friends = [friend_one, friend_two, friend_three]


