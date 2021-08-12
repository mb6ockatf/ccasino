##
# Playing the casino main file
#
from datetime import datetime
import time
import sys
from random import randint
import json


log_in = False


def init():
    try:
        playername = input('Create a name for your account. Please remember it: ')
        start_time = datetime.now()
        created_file_name = str(playername + '.json')
        # Creating a file with user's name.
        with open(created_file_name, 'wb') as account:
            # Initializing data: (name, statistics, rating)
            contents = {'name': playername, 'all_log-ins': 1, 'longest_game': '', 'most_wins': 0, 'most_lost': 0,
                        'best_game': '', 'worst_game': '', 'rating': 0}
            # Writing initialized data into file.
            try:
                json.dump(contents, account)
            except:
                print('Som error appeared when writing data into file. Anyway, file will be created.')
                account.close()
        length = int(start_time) - int(datetime.now())
        print('Data stored in ' + created_file_name + '.' + '\n')
        print('Account was successfully created in %i sec.' % length)
        after_init_decision = input('If you want to play, print 1. Print 0 to quit.: ')
        if after_init_decision == 1:
            global intro, game
            intro()
            game()
    except:
        print('Some error happened. Program will terminate on 3 sec.')
        time.sleep(3)
        quit()


# To store data in account if it's already created.
def login():
    login_decision = input("Do you want to log-in? If not, your statistics won't be counted. (y/n): ")
    if login_decision == 'y':
        ac = input('Please input your account name: ')+'.json'
        try:
            with open(ac) as account:
                data = json.load(account)
                data['all_log-ins'] += 1
                global log_in
                log_in = True
                print('Successfully logged-in.')
                show_data = input('Do you want to read all data, connected with your account? (y/n): ')
                if show_data == 'y':
                    for k, v in data:
                        print(k, v)
                else:
                    wanna_play = input('Do you want to start playing? (y/n): ')
                    if wanna_play == 'y':
                        global intro, game
                        intro()
                        game()
        except:
            print('Some error appeared.')
            time.sleep(3)
            quit()
    else:
        pass


# Define a function to make the code shorter.
def ctw(choice):
    """This function is responsible for choosing the winner and continuing the game."""
    global won, lost
    ans = ''
    # Some import to make random choice possible
    if choice == 'red' or choice == 'black':
        # Chooses the winner if the color type of choice
        aa = ['red', 'black']
        ans = aa[randint(0, 1)]
        if ans == 'red':
            print(ans, 'won')
        else:
            print(ans, 'won')

    elif choice == 'odd' or choice == 'not odd':
        # Chooses the winner if odd is the type of choice
        aa = ['odd', 'not odd']
        ans = aa[randint(0, 1)]
        if ans == 'odd':
            print(ans, 'won')
        else:
            print(ans, 'won')

    elif choice == '1 to 18' or choice == '19 to 36':
        # Chooses the winner if one of two big groups is the type of choice
        aa = ['1 to 18', '19 to 36']
        ans = aa[randint(0, 1)]
        if ans == '1 to 18':
            print(ans, 'won')
        else:
            print(ans, 'won')

    elif choice == '!':
        # Makes an opportunity to quit not manually
        quit()

    else:
        # Chooses the winner if the certain number is the type of choice
        aa = int(choice)
        if 1 <= aa <= 36 or aa == 00 or aa == 0:
            b = randint(0, 36)
            c = b, 00
            listofpossibles = [b, c]
            ans = listofpossibles[randint(0, 1)]
            print(ans, 'won.')
    if ans != choice:
        print('Your choice was wrong')
        lost.append(1)

    else:
        print('Your choice was right')
        won.append(1)
    print('You won %s times, lost - %s' % (len(won), len(lost)))


# Introduction
def intro():
    """This function is responsible for describing the rules."""

    print("You're playing the casino. You can choose:")
    print(' - 1 to 18 or 19 to 36')
    print(' - odd or not odd')
    print(' - red or black')
    print(' - any number from 1 to 36, 0 and 00')
    print(' - print ! to quit')


# Game started
def game(cli_choosing=''):
    """This function is responsible for start and finish of the game."""
    if cli_choosing == '':
        choice = input('Type in your choice: ')
        while choice != '!':
            ctw(choice)
            choice = input('Type in your choice: ')
    else:
        ctw(cli_choosing)
        choice = input('Type in your choice: ')
        while choice != '!':
            ctw(choice)
            choice = input('Type in your choice: ')
    '''TODO: add all data counted in this session into the account file.'''
    #
    #
    #
    #
    #
    print('Bye')
    time.sleep(3)
    quit()


# Choosing: if it's a CLI run with args or (ClI line without args / Idle).
if len(sys.argv) >= 2:
    print()
    # Create an account for player to collect his statistics
    # TODO: add more functionality
    if sys.argv[1] == 'reg':
        init()
    else:
        game(sys.argv[1])
else:
    if __name__ == '__main__':
        intro()
        won = []
        lost = []
        game()
