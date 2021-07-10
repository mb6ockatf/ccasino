# Define a function to make the code shorter

def ctw(a):
    ans = ''
    # Some import to make random choice possible
    from random import randint
    if a == 'red' or a == 'black':
        # Chooses the winner if the color type of choice
        aa = ['red', 'black']
        ans = aa[randint(0, 1)]
        if ans == 'red':
            print(ans, 'won')
        else:
            print(ans, 'won')

    elif a == 'odd' or a == 'not odd':
        # Chooses the winner if odd is the type of choice
        aa = ['odd', 'not odd']
        ans = aa[randint(0, 1)]
        if ans == 'odd':
            print(ans, 'won')
        else:
            print(ans, 'won')

    elif a == '1 to 18' or a == '19 to 36':
        # Chooses the winner if one of two big groups is the type of choice
        aa = ['1 to 18', '19 to 36']
        ans = aa[randint(0, 1)]
        if ans == '1 to 18':
            print(ans, 'won')
        else:
            print(ans, 'won')

    elif a == '!':
        # Makes an apportunity to quit not manually
        quit()

    else:
        # Chooses the winner if the certain number is the type of choice
        aa = int(a)
        if 1 <= aa <= 36 or aa == 00 or aa == 0:
            b = randint(0, 36)
            c = b, 00
            listofpossibles = [b, c]
            ans = listofpossibles[randint(0, 1)]
            print(ans, 'won.')
    if ans != a:
        print('Your choice was wrong')
    else:
        print('Your choice was right')