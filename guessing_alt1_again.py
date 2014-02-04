#!/usr/bin/python

import random

print "What is your name?",
name = raw_input()
#print "Hello %s" % name
#print type(name) #check type of our input

print "%s, i'm thinking of a number between 1 and 100. try to guess my number." % name

secret_number = random.randint(0,100)
print secret_number
input_number = 1
guesses = 0
bad_guesses = 0

while input_number != secret_number:

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


print( "You got it, %s I was thinking of %d.  It took you %d good tries, and %d bad tries.") % (name, secret_number, guesses, bad_guesses)



