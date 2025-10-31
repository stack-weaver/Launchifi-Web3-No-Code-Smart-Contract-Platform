# Simple guessing game
secret_number = 7
guess = int(input("Guess the number (1-10): "))

if guess == secret_number:
    print("You guessed it right!")
else:
    print("Try again. The number was", secret_number)
