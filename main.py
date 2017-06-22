# Importing details from various classes

from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from termcolor import colored
from datetime import datetime

# Initializing a list containing status messages
STATUS_MESSAGES = ['My name is Udit, James Bond', 'Sleeping', 'Keeping the British end up, Sir']

# Welcoming the user
print "Hello! Let\'s get started !!"

# Asking for aproval to continue as default existing user
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "

# Getting user input to continue as existing or not
existing = raw_input(question)

# Defining a function to add/update status message
def add_status():

    # Setting updated_status_message to None
    updated_status_message = None

    # Checking for current status message
    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:

        print 'You don\'t have any status message currently \n'

    # Asking the user whether to select from an older satus or not
    default = raw_input("Do you want to select from the older status (y/n)? ")

    # If N is selected, requesting to enter a new message
    if default.upper() == "N":

        new_status_message = raw_input("What status message do you want to set? ")
        # Checking the length of status message entered by user
        if len(new_status_message) > 0:
            # updating the status messages list
            STATUS_MESSAGES.append(new_status_message)

            updated_status_message = new_status_message

    # If Y is selected, asking the user to select from existing messages
    elif default.upper() == 'Y':

        item_position = 1

        # Printing the existing status messages
        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1
        # Status selection by user
        message_selection = int(raw_input("\n Choose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'
    # Displaying the updated status message
    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    # Function returns updated Status message
    return updated_status_message


# Function to add friend
def add_friend():

    new_friend = Spy('', '', 0, 0.0)

    # Asking details of new friend
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

    # Returning length of friends list i.e  number of friends
    return len(friends)

# Function for selection of friend
def select_a_friend():
    item_number = 0

    # Printing the list of friends
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)

        item_number = item_number + 1

    # Choosing a friend from friend list
    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1
    # If selection valid, return index of friend selected.

    if friend_choice_position < len(friends):

        return friend_choice_position
    else:

        print 'Choose from the people given above'
        exit()

# Define a function to send message
def send_message():

    # Selcting a friend
    friend_choice = select_a_friend()
    # Entering name of image
    original_image = raw_input("What is the name of the image?")
    # Defining output encoded image name
    output_path = "output.jpg"
    # Inputting the message to be sent
    text = raw_input("What do you want to say? ")
    # Checking if a valid message
    if len(text) >0:
        # Encoding the message
        Steganography.encode(original_image, output_path, text)

        new_chat = ChatMessage(text,True)
        # Appending the new message into chats list
        friends[friend_choice].chats.append(new_chat)

        print "Your secret message image is ready!"
    else:
        print 'Enter a valid message '

# Defining a function to read a message
def read_message():

    # Selecting a friend
    sender = select_a_friend()
    # Inputting name of file
    output_path = raw_input("What is the name of the file?")
    # Decoding the secret message
    secret_text = Steganography.decode(output_path)
    number_of_words = len(secret_text.split())

    # Checking the number of words in incoming message
    if number_of_words > 100:
        # If number of words in message is greater than 100 , we delete the friend who sent it.
        print 'This friend talks too much, Unfriending!! '
        del friends[sender]
    else:
        # Check for empty secret message
        if len(secret_text) > 0:
            # Checking for special cases of emergency
            if secret_text == "SOS" or secret_text == "SAVE ME" or secret_text == "HELP":
                print 'Immediate help required.'

            new_chat = ChatMessage(secret_text,False)
            friends[sender].chats.append(new_chat)

            print "Your secret message has been saved!"
        else:
            print 'Empty message'


# Defining function to read chat history
def read_chat_history():
# Selecting a friend

    read_for = select_a_friend()

    print '\n'

    # Displaying chat history
    for chat in friends[read_for].chats:

        # Using various colors for printing chat history
        if chat.sent_by_me:
            print '[%s]' % (colored([chat.time.strftime("%d %B %Y")] ,'blue'))
            print '%s:' % (colored('You said:','red'))
            print '%s:' % (colored(chat.message,'yellow'))
        else:
            print '[%s] ' % (colored([chat.time.strftime("%d %B %Y")],'blue'))
            print '%s said:' %(colored((friends[read_for].name),'red'))
            print ' %s ' % (colored((chat.message),'yellow'))


# Function to display message corresponding to different spy ratings
def display_msg_acc_spy_rating(spy):

    if spy.rating > 4.5:

        print 'Great ace!'

    elif spy.rating > 3.5 and spy.rating <= 4.5:

        print 'You are one of the good ones.'
    else:

        print 'You can always do better'


# Function to start chat
def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name

    # Checking for age verification of spy
    if spy.age > 12 and spy.age < 50:

        # Printing spy details after authentication
        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True

        # Display menu of options for a spy
        while show_menu:

            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n " \
                           "3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n" \
                           " 6. Close Application \n"
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

# Checking for spy input for login with existing account or creating new user
if existing.upper() == "Y":
    start_chat(spy)
elif existing.upper() == "N":

# Initializing the spy object
    spy = Spy('','',0,0.0)

# Inputting spy details and applying corresponding validations
    # Enter spy name
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    try:
        if len(spy.name) > 0 :
            # Enter spy spy salutation
             spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

             if len(spy.salutation) >0 :

                try:
                    #Enter spy age

                    spy.age = raw_input("What is your age?")
                    spy.age = int(spy.age)
                    # Check for age validations
                    if type(spy.age) is int and spy.age > 12 and spy.age < 50:

                        try:
                            # Enter spy rating
                            spy.rating = raw_input("What is your spy rating?")
                            spy.rating = float(spy.rating)

                            # Applying validations on spy rating
                            if spy.rating > 0.0 and spy.rating < 5.1:

                               # Calling  various functions after getting proper details
                                display_msg_acc_spy_rating(spy)
                                start_chat(spy)
                            else:
                               # Printing appropritate message for out of range spy rating
                                print 'Rating should be between 0 and 5'

                        except Exception:
                            # Printing appropritate message for invalid spy rating
                            print 'Enter proper rating'
                    else:
                        # Printing appropritate message for invalid spy age
                        print 'Age of spy doesn\'t match requirements'

                except Exception:
                    # Printing message if invalid age is entered
                    print('Enter proper age')

             else:
                 # Printing message corresponding to empty salutation
                print 'Please provide proper salutation'
                exit()
        else:
            # Printing message corresponding to empty name entry
             print 'Please add a valid spy name'

    except Exception:
        print 'Enter details properly'

else:
    # Printing a message if user gives a choice other than Y or N
    print 'Provide a valid answer'