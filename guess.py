#guessing number game

import random

guessesTaken = 0


print('hello! what is your name?')
myName = raw_input()

number = random.randint(1,20)
print('ok, ' + myName + ', I am thinking of a number between 1 and 20')

for guessesTaken in range(6):
    print('Take a guess!')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('your guess is too low :P')

    if guess > number: 
        print('your guess is too high ^')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('good job, ' + myName + '! you guessed my number in ' + guessesTaken + 'guesses!')

if guess != number:
    number = str(number)    
    print('nope. The number i was thinking of was ' + number + '.')



