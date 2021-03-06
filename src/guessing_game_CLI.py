# Importing stuff.
import random
import os 
import time 

# Printing out credits.
print('''
############ Credits ############
#           Panguin6010         #
#           Nosson-P            #
#           Llamalectric        #
#           StackOverflow       #
##################################
''')

print("Please wait 2 seconds.")
time.sleep(1)
print("CTRL + C to Exit")
time.sleep(1)
os.system("cls" if os.name == "nt" else "clear")
# Amount of guesses taken.
guessesTaken = 1
users_name = os.getlogin()
# Asking user what the top number should be, as well as how many guesses they should have.
# Making sure user only inputs str and int in the right places.
while True:
    try:
        Never_Going_To_Use = input("Hi " + users_name + " ready to play the game?\n")
        print("cool")

        os.system("cls" if os.name == "nt" else "clear")

        top_value_of_random_number = int(input("What should the top number be?:\n"))

        print('Ok got it, ' + users_name + ', I am thinking of a number between 1 and ' + repr(top_value_of_random_number) + ':')

        number_of_guesses = int(input("How many guesses do you want?:\n"))

        os.system("cls" if os.name == "nt" else "clear")

        print("Ok lets start!")

                # Generating pseudorandom number.
        answer = random.randint( 1 , top_value_of_random_number )

        for guessesTaken in range(number_of_guesses):

            guess = int(input("Take a guess!:\n"))
            # Guess is too low.
            if guess < answer:
                print('your guess is too low ↓:\n')
    
            # Guess is too high.
            if guess > answer: 
                print('your guess is too high ↑:\n')
    
            # If users guesses correctly exit loop.
            if guess == answer:

                break

    except ValueError:

        # If the inputs are wrong return to start of loop.
        os.system("cls" if os.name == "nt" else "clear")
        print("Sorry, I don't understand you might have typed it in wrong lets try again from the begining.")

        continue

    else:
        # If the inputs are good exit the loop.
        break

# If user guesses tell user they got it right along with some info. 
if guess == answer:
    print("Great job, " + users_name + "! You guessed the number in " + repr(guessesTaken) + " turns! The number of turns was  " + repr(number_of_guesses) +  " turns. The number was " + repr(answer) + ":")
    print("if you want to stop play press CTRL + C.")
# If the number is not guessed in 6 trys convert answer to string and tell users that they did not get it and show the number.
if guess != answer:    
    print("Sorry, " + users_name + " you did not guess the number I was thinking of in " + repr(number_of_guesses) + " trys. The number I was thinking of was " +  repr(answer) + " try again.")
