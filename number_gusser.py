import random

print("""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                == Welcome to Random Number Guess ==
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")

top_of_range = input("Type the largest number: ").strip()

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a valid positive integer next time.")
    quit()

# random.randint(1, top_of_range) includes both endpoints 1 and top_of_range
random_number = random.randint(1, top_of_range)

guesses = 0
right_guesses = 0

print("Tip: Enter 'P' at any time to stop the game.\n")

while True:
    user_input = input("Make a guess: ").strip()

    # Check for quit command first before digit validation
    if user_input.upper() == "P":
        break

    if not user_input.isdigit():
        print("Please enter a valid number or 'P' to quit.\n")
        continue

    user_guess = int(user_input)
    guesses += 1

    if user_guess == random_number:
        print("You got it right! 🎉")
        right_guesses += 1
        break  # Game ends on correct guess (or generate a new random_number here)
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("\n--- Game Over ---")
print(f"Total guesses: {guesses}")
print(f"Correct guesses: {right_guesses}")
print(f"Wrong guesses: {guesses - right_guesses}")