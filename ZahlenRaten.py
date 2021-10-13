from numpy import random

def generate_random(upper_limit):
    number = random.randint(upper_limit) + 1
    return number; 

def isPrime(number):
    for i in range(2, int(number/2)+1):
        if (number%i) == 0:
            return False
    return True

def checkIfTipped(tip, tip_list):
    for i in tip_list:
        if tip == i:
            return True
    return False

    
try:
    quit = ''
    upper_limit = 0
    while quit != 'j':
        upper_limit = int(input("Bitte eine Obergrenze eingeben:"))
        rand_num = generate_random(upper_limit)
        # rand_num = 11
        print("Zahl generiert !!!")
        correct = True
        tip_list = []
        guess_count = 1
        while correct:
            tip = int(input(f"Gib deinen {guess_count}. Tipp ab:"))
            if checkIfTipped(tip, tip_list):
                print(f"Du hast es mit {tip} schon einmal versucht ...")
            elif  guess_count == 1 and isPrime(rand_num) and tip != rand_num:
                print(f"Dein {guess_count}. Tipp ist Falsch... Die Zufallszahl ist eine Primzahl!")
            elif tip < rand_num:
                print(f"Dein {guess_count}. Tipp ist zu niedrig...")
            elif tip > rand_num:
                print(f"Dein {guess_count}. Tipp ist zu hoch...")
            else:
                print(f"Richtig!!! Du hast {guess_count} Versuche gebraucht")
                correct = False
            guess_count += 1
            tip_list.append(tip)
        quit = input('Willst du das Spiel beenden? (j):')
except ValueError:
    print("Wrong input!!!")
