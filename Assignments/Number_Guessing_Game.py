
import random

print("Welcome to the Number Guessing Game!\n")

print("Try to guess a number between 1 and 100.")

generate_random_number = random.randint(1, 100)
count = 1

while(True):
    try:
        user_input = int(input("Enter your guess: "))
        
        if(user_input == generate_random_number):
            print(f"\nCongratulations! You have guessed the right number in {count} attempt")
            exit()
        else:
            while(True):
                if(user_input < generate_random_number):
                    print("Too low!")
                elif(user_input > generate_random_number):
                    print("Too high!")
                else:
                    print(f"\nCongratulations! You have guessed the right number in {count} attempts")
                    exit()
                user_input = int(input("Enter your guess again: "))
                count += 1
    except ValueError:
        print("Invalid input. Please choose a number between 1 and 100 (inclusive)")
        continue