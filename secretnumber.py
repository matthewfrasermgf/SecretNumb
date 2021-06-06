# Guess the number game
import random
print('Hello. What is your name?')
name = input()
secret = random.randint(1, 20)
print('Hello, ' + name + '. Guess a number from 1 to 20.')

# Guess 5 times
for guesses in range(1, 6):
    print('\nTake a guess.')
    guess = input()
    if guess.isdigit() == False:
        print('Please enter a valid integer.')
    elif int(guess) > 20:
        print('Please make a valid selection between 1 and 20.')
    elif int(guess) <1:
        print('Please make a valid selection between 1 and 20.')
    elif int(guess) < secret:
        print('Your guess is too low.')
    elif int(guess) > secret:
        print('Your guess is too high.')
    else:
        break # Correct!

# Guessing responses
if int(guess) == secret:
    print('Congrats, ' + name + '! You guessed correctly!')
else:
    print('Sorry! The correct answer is ' + str(secret))
