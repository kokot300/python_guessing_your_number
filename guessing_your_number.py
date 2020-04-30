#!/usr/bin/python3

def user_input():
    while True:
        while True:
            user_tip = input("zgadłem? \n1: tak \n2: nie \n")
            try:
                int(user_tip)
                if int(user_tip)==1:
                    return 1
                else:
                    break
            except:
                print('proszę wpisać numer od 1 do 3 zgodnie z menu!')

        while True:
            user_tip_2= input("za dużo? \n 1: tak \n2: nie \n")
            try:
                int(user_tip_2)
                if int(user_tip_2)==1:
                    return 2
                else:
                    break
            except:
                print('proszę wpisać numer od 1 do 3 zgodnie z menu!')

        while True:
            user_tip_3 = input("za mało? \n 1: tak \n2: nie \n")
            try:
                int(user_tip_3)
                if int(user_tip_3) == 1:
                    return 3
                else:
                    print('nie oszukuj!')
                    return 4
            except:
                print('proszę wpisać numer od 1 do 3 zgodnie z menu!')


def game():
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
        elif tip==2:
            max=guess
            continue
        elif tip==3:
            min=guess
            continue
        else:
            continue

if __name__ == '__main__':
    game()