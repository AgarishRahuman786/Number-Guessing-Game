import random
random_number = random.randint(1, 100)
while True:
    try:
        Guess = int(input("Guess the number between 1 and 100:"))
        if Guess > random_number:
            print("Too high")
        elif Guess < random_number:
            print("Too low")
        else:
            print("Congratulations! You guessed the number")
            break
    except ValueError:
        print("Please enter a valid number")
