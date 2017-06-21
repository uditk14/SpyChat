# Importing details from various classes
from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime

# Initializing a list containing status messages
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']

print "Hello! Let\'s get started !!"

# Asking for aproval to continue as default existing user
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "

# Getting user input to continue as existing or not
existing = raw_input(question)

# Defining a function to add/update status message
def add_status():

    updated_status_message = None

# Checking for current status message
    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

# Asking the user whether to select from an older satus or not
    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\n Choose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message


def add_friend():

    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    if(new_friend.name > 0):
        new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
        if(new_friend.salutation > 0):
            new_friend.name = new_friend.salutation + " " + new_friend.name
        else:
            print 'Provide proper salutation'

        new_friend.age = int(raw_input("Age?"))

        new_friend.rating = float(raw_input("Spy rating?"))

        if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
            friends.append(new_friend)
            print '\n Friend Added!'
        else:
            print '\n Sorry! Invalid entry. We can\'t add spy with the details you provided'
    else:
        print '\n Provide proper name!!'
    return len(friends)


def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)
    
    print "Your secret message has been saved!"


def read_chat_history():

    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:

        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)

def display_msg_acc_spy_rating(spy):

    if spy.rating > 4.5:

        print 'Great ace!'

    elif spy.rating > 3.5 and spy.rating <= 4.5:

        print 'You are one of the good ones.'
    else:

        print 'You can always do better'

def start_chat(spy):

    spy.name = spy.salutation + "." + spy.name


    if spy.age > 12 and spy.age < 50:


        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'


if existing.upper() == "Y":
    start_chat(spy)
elif existing.upper() == "N":

    spy = Spy('','',0,0.0)

    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    try:
        if len(spy.name) > 0 :
             spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

             if len(spy.salutation) >0 :

                try:

                    spy.age = raw_input("What is your age?")
                    spy.age = int(spy.age)
                    if type(spy.age) is int and spy.age > 12 and spy.age < 50:
                        try:
                            spy.rating = raw_input("What is your spy rating?")
                            spy.rating = float(spy.rating)

                            if spy.rating > 0.0 and spy.rating < 5.1:
                                start_chat(spy)
                                display_msg_acc_spy_rating(spy)
                            else:
                                print 'Rating should be between 0 and 5'
                        except Exception:
                            print 'Enter proper rating'
                    else:
                        print 'Enter proper age'

                except Exception:
                    print('Enter proper age')

             else:
                print 'Please provide proper salutation'
                exit()


        else:
             print 'Please add a valid spy name'

    except Exception:
        print 'Enter details properly'
else:
    print 'Provide a valid answer'