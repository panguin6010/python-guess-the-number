#guessing number game
#importing stuff

import random

#guesses taken
guessesTaken = 0

# asking user whats there name and saving it
print('hello! what is your name?')
users_name = raw_input()

# making a random number and asking user to geuss number
number = random.randint(1,20)
print('ok, ' + myName + ', I am thinking of a number between 1 and 20')
 
# loop 6 times 
for guessesTaken in range(6):
    print('Take a guess!')
    guess = input()
    guess = int(guess)
    
    # guess to low 
    if guess < number:
        print('your guess is too low :P')
    
    # guess to high
    if guess > number: 
        print('your guess is too high ^')
    
    #if users guess correctlty exit loop
    if guess == number:
        break

# if users guess correctly then take number of guess convert to string and add one and tell users they got it right 
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('good job, ' + users_name + '! you guessed my number in ' + guessesTaken + ' guesses!')

# if not guessed in 6 trys convert number to string and tell users that they did not get it and show the number
if guess != number:
    number = str(number)    
    print('nope. The number i was thinking of was ' + number + '.')



