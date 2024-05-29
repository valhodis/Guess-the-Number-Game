import random

print("Welcome to Guess the Number Game.")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
print()
print("Let's play!")

attempt = 0
myNumber = random.randint(1, 1000000)

while True:
    user_guess = int(input("Pick a number between 1 and 1,000,000: "))
    attempt += 1
    if user_guess < myNumber:
        if myNumber - user_guess <= 100:
            print("🔥 The number is a little bigger. Try again!")
        else:
            print("🥶 That number is too low. Try again!")
    elif user_guess > myNumber:
        if user_guess - myNumber <= 100:
            print("🔥 The number is a little lower. Try again!")
        else:
            print("🥶 That number is too high. Try again!")
    else:
        print("You are a winner! 🥳🥳")
        break

print(f"It took you {attempt} attempt(s) to get the correct answer.")
