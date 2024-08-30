import random
random_number = random.randint(1, 100)
# print(f'Debug: The random number is {random_number}')
guess = 0
while guess != random_number:
    guess = int(input("Enter your number between 1 and 100: "))
    # print(f'Debug: Player guessed {guess}')
    if guess > random_number:
        print("Your guess is too high")
    elif guess < random_number:
        print("Your guess is too low")
    else:
        print("Your guess is correct")