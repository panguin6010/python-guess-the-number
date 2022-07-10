import random
import os 
import time
GuessesTaken = int(0)
Users_name = os.getlogin()
Credits = ('''
############ Credits ############
#           Panguin6010         #
#           Llamalectric        #
#           Nosson-P            #
#           StackOverflow       #
##################################
''')
print(Credits)
print("Please wait 2 seconds.")
time.sleep(1)
print("CTRL + C to Exit")
time.sleep(1)
def Clear_screen():
    os.system("cls" if os.name == "nt" else "clear")# Clearing screen. 
Clear_screen() 
def If_user_gets_right_answer():# If users guesses tell users they got it right along with some info.
    Clear_screen()
    print("great job, " + Users_name + "! You guessed the number in " + repr(GuessesTaken) + " turns! out of " + repr(Number_of_guesses) +  " turns the number was " + repr(Answer) + ":")
    print("Getting new random number:")
def Adding_to_amounts_of_guesses():# Adding to amount of guesses.
    guessesTaken += 1
while True:
    try:
        input("Hi " + Users_name + " ready to play the game?\n")
        Clear_screen()
        Top_value_of_random_number = int(input("What should the top number be?:\n")) # Asking user for top value of random number.
        Answer = random.randint( 1 , Top_value_of_random_number )# Generating sudo random number.
        print('Ok got it, ' + Users_name + ', I am thinking of a number between 1 and ' + repr(Top_value_of_random_number) + ':')
        Number_of_guesses = int(input("How many guesses do you want?:\n")) # Getting amont of guesses that user has.
        Clear_screen()
        print("Ok lets start!")
        while GuessesTaken < Number_of_guesses: # If guesses taken is less than number of guesses, keep guessing eles tell user they lost and restart game.
            Guess = int(input("Take a guess!:\n"))# Clearing screen.
            # Guess is to low.
            if Guess < Answer: # If the guess is less than answer, tell user guess is to low.
                Adding_to_amounts_of_guesses()
                Clear_screen()
                print('your guess is too low ↓:\n')
            if Guess > Answer:# If the guess is greater than answer, tell user guess is to high.
                Adding_to_amounts_of_guesses()
                Clear_screen()
                print('your guess is too high ↑:\n')
            if Guess == Answer:# If the guess is equal to answer  call function that tells user they got it right.
                Adding_to_amounts_of_guesses()
                If_user_gets_right_answer() # Calling function to check if user got it right.
                Answer = random.randint( 1 , Top_value_of_random_number ) # Generating new random number if user did not guess correctly or if users ran out of guesses.
        # If user ran out of guesses.
        Clear_screen() 
        print("Sorry, " + Users_name + " you did not guess the number I was thinking of in " + repr(Number_of_guesses) + " trys The number I was thinking of was " +  repr(Answer) + " try agian.")
        print("Restarting game:")
    # f user puts in wrong values.
    except ValueError:
        Clear_screen()
        print("Sorry, I don't understand you might have typed it in wrong lets try again from the begining.")
        continue
    except KeyboardInterrupt:# If user presses CTRL + C exit.
        Clear_screen()
        print("Thanks for playing " + Users_name + "! I hope you had fun playing!")
        print(Credits)
        time.sleep(3) 
        break