from datetime import datetime
import time
import sys
from random import randint
import json

log_in, user, won, lost, length = False, '', 0, 0, 0


def register():
    nickname = input('Create a name for your account. Please remember it: ')
    start_time = datetime.now()
    created_file_name = str(nickname + '.json')
    with open(created_file_name, 'x') as account:
        contents = {'name'        : nickname,
                    'all_log-ins' : 1,
                    'longest_game': '0',
                    'most_wins'   : 0,
                    'most_lost'   : 0,
                    'best_game'   : '0',
                    'worst_game'  : '0',
                    'rating'      : 0}
        json.dump(contents, account, ensure_ascii=False)
    global user
    user = created_file_name
    print('Data stored in ' + created_file_name, '\n', 'Account was successfully created in',
          start_time - datetime.now(), 'sec')
    decision_after_registering = int(input('If you want to play, print 1. Print 0 to quit.: '))
    if decision_after_registering == 0:
        time.sleep(3)
        exit()


def casino_machine(choice):
    global length, lost, won
    ans = ''
    print(''.center(47, '*'),
          f'*This is %s turn.{" " * 29}*' % str(len(length) + 1),
          sep='\n')
    if choice == 'red' or choice == 'black':
        ans = ['red', 'black'][randint(0, 1)]
    elif choice == 'odd' or choice == 'not odd':
        ans = ['odd', 'not odd'][randint(0, 1)]
    elif choice == '1 to 18' or choice == '19 to 36':
        ans = ['1 to 18', '19 to 36'][randint(0, 1)]
    elif choice == '!':
        quit()
    else:
        if 0 <= int(choice) <= 36 or int(choice) == 00:
            ans = ([str(j) for j in range(0, 37)] + ['00'])[randint(0, 38)]
    print(f"{'-' * 7} {['red', 'black'][randint(0, 1)]} won {'-' * 7}")
    length = length + 1
    if ans != choice:
        print('Your choice was wrong')
        lost += 1
    else:
        print('Your choice was right')
        won += 1
    print('* You won %s times, lost - %s                 *' % (won, lost))


def game(cli_choosing=''):
    global length, lost, won
    if cli_choosing == '':
        choice = input('Type in your choice: ')
        while choice != '!':
            casino_machine(choice)
            choice = input('\nType in your choice: ')
    else:
        casino_machine(cli_choosing)
        choice = input('Type in your choice: ')
        while choice != '!':
            casino_machine(choice)
            choice = input('Type in your choice: ')
    fh = open(str(user + '.json'))
    data = json.load(fh)
    if data['most_wins'] < won:
        data['most_wins'] = won
    if data['most_lost'] < lost:
        data['most_lost'] = lost
    if int(data['longest_game']) < length:
        data['longest_game'] = length
    if float(data['best_game']) < won / (lost if lost != 0 else 1):
        data['best_game'] = won / (lost if lost != 0 else 1)
        print(''.center(47, '*'),
              '* You have a record: it was your luckiest game*',
              f'* ever. Congratulations!{" " * 22}*',
              ''.center(47, '*'), '\n')
    elif float(data['worst_game']) != 0 and float(data['worst_game']) < lost / (won if won != 0 else 1):
        data['worst_game'] = lost / (won if won != 0 else 1)
        print(''.center(47, '*'), '* You have a record: it was your unluckiest   *',
              '* game ever. Better luck next time.           *', ''.center(47, '*'), sep='\n')
    data['rating'] = (data['most_wins'] - data['most_lost']) / data['all_log-ins']
    fh.close()
    with open(str(user + '.json'), 'w') as f:
        json.dump(data, f)
    print('Bye')
    time.sleep(3)
    quit()


if len(sys.argv) >= 2:
    if sys.argv[1] == 'reg':
        register()
    else:
        game(sys.argv[1])
else:
    if __name__ == '__main__':
        print(''.center(47, '*'), f'*{"***casino game***".center(45, " ")}*', ''.center(47, '*'))
        print(''.center(47, '*'), "* Press nn if you are not registered but you  *", f"*  want to.{' ' * 35}*",
              f"*{''.center(45, ' ')}*", "* If you are and you want to login,  please   *",
              "* make sure that your account's file is in    *", f"* the current directory and press 'y'{' ' * 9}*",
              f"*{''.center(45, ' ')}*", "* If you are registered and you don't want to,*", f"* press 'n'{' ' * 35}*",
              ''.center(47, '*'), sep='\n')
        login_decision = input('y/n/nn: ')
        if login_decision == 'y':
            account_name = input('\nPlease input your account name: ')
            user = account_name
            with open(account_name + '.json') as account:
                data = json.load(account)
                data['all_log-ins'] += 1
                log_in = True
                show_data = input('\nSuccessfully logged-in. Do you want to read all data, \
connected with your account? (y/n): ')
                if show_data == 'y':
                    print(data)
                    time.sleep(5)
            wanna_play = input('Do you want to start playing? If not, the program will close. (y/n): ')
            if wanna_play != 'y':
                quit()
                game()
        elif login_decision == 'nn':
            register()
        print(''.center(47, '*'), "* You're playing the casino. You can choose:  *",
              f'*  - 1 to 18 or 19 to 36{" " * 22}*', f'*  - odd or not odd{" " * 27}*',
              f'*  - red or black{" " * 29}*', f'*  - any number from 1 to 36, 0 and 00        *',
              f'*  - print ! to quit{" " * 26} *', f''.center(47, '*'), '\n')
        game()
