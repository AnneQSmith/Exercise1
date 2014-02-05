#!/usr/bin/python
# make sure the environment variable "DEBUGE1" exists before running this.
import random
import os

print "What is your name?",
name = raw_input()

keep_playing = True
while (keep_playing):

    print "%s, i'm thinking of a number between 1 and 100. try to guess my number." % name

    secret_number = random.randint(0,100)
    secret_number = 1
    if os.environ['DEBUGE1'] == 'Y':
        print secret_number
    else:
        pass
    input_number = -1
    guesses = 0
    bad_guesses = 0

    while (input_number != secret_number):

        user_input = raw_input()
        if user_input.isdigit():
            input_number = int(user_input)
            guesses += 1

            if input_number > secret_number:
                print ("Ha Ha that's too big!")
            elif input_number < secret_number:
                print ("Tee hee  -- that's too small!")
           
        else:
            print ("You need to enter an integer")
            bad_guesses += 1

    print( "You got it, %s I was thinking of %d.  It took you %d good tries, and %d bad tries.")\
     % (name, secret_number, guesses, bad_guesses)
    
    print ("Enter 'y' to keep playing!")
    if raw_input().lower() != "y":
        keep_playing = False

