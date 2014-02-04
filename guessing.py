#!/usr/bin/python

print "What is your name?"
name = raw_input()
#print "Hello %s" % name
#print type(name) #check type of our input

print "%s, i'm thinking of a number between 1 and 100. try to guess my number." % name

secret_number = 40
input_number = 1
guesses = 0
while input_number != secret_number:
 #   print "At the top input_number %d" % input_number
    input_number = int(raw_input())
    guesses += 1
    print guesses
    if input_number > secret_number:
        print ("Ha Ha that's too big!")
    elif input_number < secret_number:
        print ("Tee hee  -- that's too small!")

print( "You got it %s I was thinking of %d .  It took you %d tries") % (name, secret_number, guesses)


