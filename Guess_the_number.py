import random
from re import X

def guess(x):
    random_number = random.randint(1, x)

    guess = 0

    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess<random_number:
            print("too low")
        elif guess>random_number:
            print("too high")
                
    print(f"yay!! made it {random_number}")    

def comp_guess(x) :
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low    
        feedback = input(f'Is {guess} to high (H), too low(L), or correct(C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"yay {guess}")           

comp_guess(1000)