import random
def game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        game()
    else:
        print("Thank you for playing! Goodbye!")
game()
with open("poem.txt") as f:
    content = f.read()
    if "twinkle" in content:
        print("twinkle is present in the content")
    else:
        print("the word twinkle is not present in the content ")