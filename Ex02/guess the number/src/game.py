import random

money = 100
print("Welcome to the Guess The Number Game!")
print(f"You have ${money} to start. Each game costs $5.")

while money >= 5:
    print("\nChoose difficulty level:")
    print("1. Easy (10 guesses)")
    print("2. Medium (6 guesses)")
    print("3. Hard (3 guesses)")
    level = input("Enter 1, 2, or 3: ")

    if level == "1":
        max_attempts = 10
    elif level == "2":
        max_attempts = 6
    elif level == "3":
        max_attempts = 3
    else:
        print("Invalid choice. Defaulting to Easy.")
        max_attempts = 10

    money -= 5
    print(f"\nYou have ${money} left.")

    number = random.randint(1, 100)
    attempts = 0
    won = False

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}. Guess the number (1-100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
            won = True
            money += 10
            break

    if not won:
        print(f"Sorry! You didn't guess the number. It was {number}.")

    print(f"Current money: ${money}")

    if money < 5:
        print("You don't have enough money to continue playing. Game over!")
        break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print(f"\nThanks for playing! You finished with ${money}.")
