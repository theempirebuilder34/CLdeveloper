import random
import time

try:
    print("Hi! Welcome to my guessing game. I am going to pick a number between 1 and 100")
    time.sleep(1)
    print("Processing....")
    time.sleep(3)
    print("Number has been chosen!")
    time.sleep(1)
    secret_number = random.randint(1,100)
    guess = int(input("What is your guess?:"))
    guess_count = 1

    out_of_guesses = False

    while guess != secret_number and guess_count <= 9:
        if guess < secret_number:
            guess = int(input(f"Count:{guess_count}, Wrong! You need to guess higher. What is your guess?:" ))
            guess_count += 1
        else:
            guess = int(input(f"Count:{guess_count}, Wrong! You need to guess lower. What is your guess?:"))
            guess_count += 1
    if guess == secret_number:
        print(f"You win! it took you {guess_count} guesses")
    else:
        print(f"You have guessed {guess_count} times, out of guesses, YOU LOSE!")

except:
    print("Invalid input, please restart game")



print("Thanks for playing!")
