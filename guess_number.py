
number = 10
max_guesses = 5  
print("I'm thinking of a number...")

guesses_left = max_guesses  
while guesses_left > 0:
    guess = input(f"What number am I thinking of? (Enter 'q' to quit). You have {guesses_left} guesses left: ")
    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break
    try:
        guess = int(guess)
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
<<<<<<< HEAD
        else:
            guesses_left -= 1  
            if guesses_left == 0:
                print(f"Sorry, you're out of guesses. The number was {number}.")
            else:
                print("Sorry! That's not it. Try again.")
=======
        elif guess < number:
            print("Sorry! That's too low. Try again.")
        else:  # This means guess > number
            print("Sorry! That's too high. Try again.")
>>>>>>> guess-hits
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")

if guesses_left == 0 and guess.lower() != 'q':  
    print(f"Sorry, you're out of guesses. The number was {number}.")
