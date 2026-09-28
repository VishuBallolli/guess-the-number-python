import random
# Import the random module to generate a random number


def guess_the_number():
    # Define a function called guess_the_number()
    # This function contains the complete game


    """
    A simple number guessing game where the user tries
    to guess a random number between 1 and 100.
    """
    # This is a docstring.
    # It describes what the function does.


    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    # randint() generates a random integer between 1 and 100
    # The generated number is stored in secret_number


    attempts = 0
    # Variable to count the number of valid guesses


    guessed = False
    # Initially, the user has not guessed the number


    # Display the game title and instructions
    print("=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 100.")
    print("Can you guess what it is?")
    print("=" * 50)
    print()


    # Continue the game until the user guesses correctly
    while not guessed:
        # while loop runs as long as guessed is False
        try:



            # Get input from the user
            guess = int(input("Enter your guess: "))
            # input() takes the user's input
            # int() converts the input from string to integer


            # Check whether the number is between 1 and 100
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
                # continue skips the remaining code
                # and starts the next loop iteration


            # Increase the attempt count by 1
            attempts += 1


            # Check whether the user's guess is correct
            if guess == secret_number:

                # The user guessed the correct number
                guessed = True

                print()

                print("=" * 50)

                print("🎉 Congratulations! You guessed it!")

                print(f"The number was {secret_number}.")

                print(f"Total attempts: {attempts}")

                print("=" * 50)


            # Check if the guess is smaller than the secret number
            elif guess < secret_number:
                print(
                    f"Too low! Try a higher number. "
                    f"(Attempt #{attempts})"
                )


            # If it is not equal or smaller, it must be higher
            else:
                print(
                    f"Too high! Try a lower number. "
                    f"(Attempt #{attempts})"
                )


        except ValueError:
            # This runs if the user enters something
            # that cannot be converted into an integer
            print("Invalid input. Please enter a valid number.")


# Check whether this Python file is being run directly
if __name__ == "__main__":
    # Start the number guessing game
    guess_the_number()