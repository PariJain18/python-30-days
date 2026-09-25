import random
secretno=random.randint(1,10)
attempts=0
while True:
    guess=int(input("Guess the number (1-10)"))
    attempts=attempts+1
    if guess<secretno:
        print("Too low")
    elif guess>secretno:
        print("Too high")
    else:
        print("Correct")
        print("Attempts:",attempts)
        break
