##
# Playing the casino main file
#
from datetime import datetime
import time
import sys
from random import randint
import json

log_in = False
user = ''
won = []
lost = []
length = []


def register():
    required_account_creating = input('Do you want to make an account in this game? (y/n)')
    if required_account_creating == 'y':
        playername = input('Create a name for your account. Please remember it: ')
        start_time = datetime.now()
        created_file_name = str(playername + '.json')
        # creating user account's file
        with open(created_file_name, 'x') as account:
            # Initializing data: (name, statistics, rating)
            contents = {'name': playername, 'all_log-ins': 1, 'longest_game': '0', 'most_wins': 0, 'most_lost': 0,
                        'best_game': '0', 'worst_game': '0', 'rating': 0}
            # writing initialized data into file.
            json.dump(contents, account, ensure_ascii=False)
        long = start_time - datetime.now()
        global user
        user = created_file_name
        print('Data stored in ' + created_file_name)
        print('Account was successfully created in', long, 'sec')
        decision_after_registering = int(input('If you want to play, print 1. Print 0 to quit.: '))
        if decision_after_registering == 1:
            rules()
            game()
        elif decision_after_registering == 0:
            time.sleep(3)
            exit()
    else:
        pass


# To store data in account if it's already created.
def login():
    print('***********************************************')
    print("* Press nn if you are not registered but you  *")
    print("*  want to.                                   *")
    print('*                                             *')
    print("* If you are and you want to login,  please   *")
    print("* make sure that your account's file is in    *")
    print("* the current directory and press 'y'         *")
    print('*                                             *')
    print("* If you are registered and you don't want to,*")
    print( "* press 'n'                                   *")
    print('***********************************************')
    login_decision = input('y/n/nn: ')
    print()
    if login_decision == 'y':
        account_name = input('Please input your account name: ')
        print()
        global user
        user = account_name
        ac = account_name + '.json'
        with open(ac) as account:
            data = json.load(account)
            data['all_log-ins'] += 1
            global log_in
            log_in = True
            print('Successfully logged-in.')
            show_data = input('Do you want to read all data, connected with your account? (y/n): ')
            if show_data == 'y':
                print(data)
                time.sleep(5)
            else:
                wanna_play = input('Do you want to start playing? If not, the program will close. (y/n): ')
                if wanna_play == 'y':
                    pass
                else:
                    quit()
    elif login_decision == 'nn':
        register()
    else:
        pass


# Game function
def casino_machine(choice):
    """This function is responsible for choosing the winner and continuing the game."""
    ans = ''
    print('***********************************************')
    print(*'This is %s turn.                             *' % str(len(length) + 1))
    if choice == 'red' or choice == 'black':
        # Chooses the winner if the color type of choice
        aa = ['red', 'black']
        ans = aa[randint(0, 1)]
        print('-------', ans, 'won', '-------')

    elif choice == 'odd' or choice == 'not odd':
        # Chooses the winner if odd is the type of choice
        aa = ['odd', 'not odd']
        ans = aa[randint(0, 1)]
        print('-------', ans, 'won', '-------')

    elif choice == '1 to 18' or choice == '19 to 36':
        # Chooses the winner if one of two big groups is the type of choice
        aa = ['1 to 18', '19 to 36']
        ans = aa[randint(0, 1)]
        print('-------', ans, 'won', '-------')

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
            print('-------', ans, 'won', '-------')
    if ans != choice:
        print('Your choice was wrong')
        lost.append(1)
        length.append(1)

    else:
        print('Your choice was right')
        won.append(1)
        length.append(1)
    print('* You won %s times, lost - %s                 *' % (len(won), len(lost)))


# Introduction
def rules():
    print('***********************************************')
    print("* You're playing the casino. You can choose:  *")
    print('*  - 1 to 18 or 19 to 36                      *')
    print('*  - odd or not odd                           *')
    print('*  - red or black                             *')
    print('*  - any number from 1 to 36, 0 and 00        *')
    print('*  - print ! to quit                          *')
    print('***********************************************')
    print()


# game
def game(cli_choosing=''):
    if cli_choosing == '':
        choice = input('Type in your choice: ')
        while choice != '!':
            casino_machine(choice)
            print()
            choice = input('Type in your choice: ')
    else:
        casino_machine(cli_choosing)
        choice = input('Type in your choice: ')
        while choice != '!':
            casino_machine(choice)
            choice = input('Type in your choice: ')
    # loading statistics to the account's file after the game
    fh = open(str(user+'.json'))
    data = json.load(fh)
    # checking if updating parameter required and doing it
    if data['most_wins'] < len(won):
        data['most_wins'] = len(won)  # most_wins
    if data['most_lost'] < len(lost):
        data['most_lost'] = len(lost)  # most_lost
    if int(data['longest_game']) < len(length):
        data['longest_game'] = len(length)  # longest_game
    try:
        if float(data['best_game']) < float(len(won) / len(lost)):
            data['best_game'] = (len(won) / len(lost))  # best_game (for player)
            print('***********************************************')
            print('* You have a record: it was your luckiest game*')
            print('* ever. Congratulations!                      *')
            print('***********************************************')
            print()
            # No congs if 'won', 'lost', 'length' are bit, in order not to have too many 'congratulations'.
    except ZeroDivisionError:
        if float(data['best_game']) < float(len(won) / 1):
            data['best_game'] = (len(won) / 1)  # best_game (for player)
            print('***********************************************')
            print('* You have a record: it was your luckiest     *')
            print('* game ever. Congratulations!                 *')
            print('***********************************************')
            print()
            # No congs if 'won', 'lost', 'length' are bit, in order not to have too many 'congratulations'.
    try:
        if float(data['worst_game']) != 0 and float(data['worst_game']) < len(lost) / len(won):
            data['worst_game'] = (len(lost) / len(won))
            print('***********************************************')
            print('* You have a record: it was your unluckiest   *')
            print('* game ever. Better luck next time.           *')
            print('***********************************************')
            print()
    except ZeroDivisionError:
        if data['worst_game'] != 0 and data['worst_game'] < (len(lost) / 1):
            data['worst_game'] = (len(lost) / 1)
            print('***********************************************')
            print('* You have a record: it was your unluckiest   *')
            print('* game ever. Better luck next time.           *')
            print('***********************************************')
            print()
    data['rating'] = (data['most_wins'] - data['most_lost']) / data['all_log-ins']  # rating is always updated
    fh.close()
    with open(str(user+'.json'), 'w') as f:
        json.dump(data, f)
    print('Bye')
    time.sleep(3)
    quit()


# Choosing: if it's a CLI run with args or (ClI line without args / Idle).
if len(sys.argv) >= 2:
    print()
    # Create an account for player to collect his statistics
    if sys.argv[1] == 'reg':
        register()
    else:
        game(sys.argv[1])
else:
    if __name__ == '__main__':
        print('***********************************************')
        print('*          ***casino game***                  *')
        print('***********************************************')
        print()
        login()
        rules()
        # init list to collect statistics in this session
        game()
