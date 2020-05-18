#!/usr/bin/python3

def user_input():
    '''
    handles user input. user must introduce 0<int<3
    :return: int 1, 2, 3 or 4 according to user input
    '''
    while True:

        while True:
            user_tip = input("zgadłem? \n1: tak \n2: nie \n")

            try:
                user_tip = int(user_tip)
            except ValueError:
                print('proszę wpisać numer od 1 do 2 zgodnie z menu!')
                continue

            if user_tip == 1:
                return 1
            elif user_tip > 2:
                print('proszę wpisać numer od 1 do 2 zgodnie z menu!')
                continue
            else:
                break

        while True:
            user_tip_2 = input("za dużo? \n1: tak \n2: nie \n")
            try:
                user_tip_2 = int(user_tip_2)
            except ValueError:
                print('proszę wpisać numer od 1 do 2 zgodnie z menu!')
                continue
            if user_tip_2 == 1:
                return 2
            elif user_tip_2 > 2:
                print('proszę wpisać numer od 1 do 2 zgodnie z menu!')
                continue
            else:
                break

        while True:
            user_tip_3 = input("za mało? \n1: tak \n2: nie \n")
            try:
                user_tip_3 = int(user_tip_3)
            except ValueError:
                print('proszę wpisać numer od 1 do 2 zgodnie z menu!')
                continue
            if user_tip_3 == 1:
                return 3
            elif user_tip_3 > 2:
                print('proszę wpisać numer od 1 do 2 zgodnie z menu!')
                continue
            else:
                return 4


def game():
    '''
    main function. displays rules of the game and handles min and max variables that allows python to guess the number
    calls user_input and uses it to alter min, max and guess variables
    :return: None
    '''
    min = 0
    max = 1000
    print("Pomyśl liczbę od 0 do 1000 a ja ją zgadnę w max 10 próbach.")
    while True:
        guess = int((max - min) / 2) + min
        print(f'zgaduję {guess}')
        tip = user_input()
        if tip == 1:
            print('wygrałem!')
            return 0
        elif tip == 2:
            max = guess
            continue
        elif tip == 3:
            min = guess
            continue
        else:
            print('nie oszukuj!')
            continue


if __name__ == '__main__':
    game()
