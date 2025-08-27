import random

print("Welcome to the Tài/Xỉu Dice Game!")

while True:
    try:
        money = float(input("Enter the amount of money you want to play with: $"))
        if money <= 0:
            print("Please enter a positive amount.")
            continue
        break
    except ValueError:
        print("Invalid input. Enter a number.")

game_count = 0
win_count = 0
lose_count = 0

while money > 0:
    print(f"\nYou currently have ${money:.2f}")

    while True:
        try:
            bet = float(input("Enter your bet for this round: $"))
            if bet <= 0:
                print("Bet must be positive.")
            elif bet > money:
                print("You cannot bet more than you have.")
            else:
                break
        except ValueError:
            print("Invalid input. Enter a number.")

    guess = input("Guess 'Tài' or 'Xỉu': ").strip().lower()
    while guess not in ['tài', 'tai', 'xỉu', 'xiu']:
        guess = input("Invalid choice. Guess 'Tài' or 'Xỉu': ").strip().lower()

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    result = "tài" if total > 5 else "xỉu"

    print(f"Dice rolled: {dice1} + {dice2} = {total} -> {result.capitalize()}")

    game_count += 1
    if guess in ['tài', 'tai'] and result == "tài" or guess in ['xỉu', 'xiu'] and result == "xỉu":
        print(f"You won ${bet:.2f}!")
        money += bet
        win_count += 1
    else:
        print(f"You lost ${bet:.2f}!")
        money -= bet
        lose_count += 1

    if money <= 0:
        print("You ran out of money! Game over.")
        break

    cont = input("Do you want to play another round? (yes/no): ").strip().lower()
    if cont != "yes":
        break

print("\nGame Summary:")
print(f"Total games played: {game_count}")
print(f"Games won: {win_count}")
print(f"Games lost: {lose_count}")
print(f"Ending money: ${money:.2f}")
