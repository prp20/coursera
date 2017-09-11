#http://www.codeskulptor.org/#user40_V2VAV3jEJ8ANlH8.py
#Hi...............Welcome to the game of ....
#Guess The Number!!!!!!!!!.........


#TO PALY THIS GAME YOU NEED TO PRESS THE ARROW BUTTON ON  
#THE TOP LEFT OF YOUR SCREEN


#This is simple game where the player has to first select 
# his range of number that he wants to play with
# And he has to input the number that he guesses in the box given
# But its not that easy as you think 
# It becomes difficult as we have some hurdles
# i.e we have restricted your number of guesses
# So becareful and play the game.......................
#.....................................................
import random
import simplegui
import sys
number=0
i=0
limit=0
# This is an event handler for the input part of the program
# The input taken from the user arrives here
def input_guess(inp):
    global  i, limit, num
    input=int(inp)
    print' The guess was', input
# The main comparison part of the program begins here
    if(input==number): 
        print" AND the guess is right"
        print" CONGRATULATIONS!!!!!!!!!!!!!!!"
        print
        print" please play again"
        print 
        i=0
        new_game()
    elif(input<number):
        print"higher!"
        i=i+1
        if((i<num)and(input!=number)):
            print" Number of remining guesses is",num-i
            print
        else:
            print
            print"You just ran out of guesses"
            print" BETTER LUCK NEXT TIME!!!!!!"
            print"The number was :", number
            print
            print" Please play again"
            print
            new_game()
    elif(input>number):
        print"lower!"
        i=i+1
        if((i<num)and(input!=number)):
            print" Number of remining guesses is",num-i
            print
        else:
            print
            print"You just ran out of guesses"
            print"The number was", number
            print" BETTER LUCK NEXT TIME!!!!!!!"
            print
            print" Please play again"
            print
            new_game()
#This is the end of the main function that is used in the program
#Now the next function used here is to initialise a new game
              
def new_game():
    global limit, num
    num=0
    if(limit==100):
        range100()
    else:
        range1000()
#This is the handler that is used by the button "range 0 to 100
#It also initialises the secret number
   
def range100():
    global number, limit, num
    num=7
    limit=100
    number=random.randrange(0, 100)
    print"New Game. Range is from 0 to 100"
    print"The number of guesses you have is 7"
    print
#This is the handler that is used by the button " Range 0 to1000" 
# It alsoinitialises a secter number
def range1000():
    global number, limit, num
    num=10
    limit=1000
    number=random.randrange(0, 1000)
    print"New Game.Range is from 0 to 1000"
    print"The number of guesses you have is 10"
    print
# This is where the frame gets initialised and all that 
#appears on the screen begins to take shape
user_input.set_text("")
    
f=simplegui.create_frame("guess the number", 200, 200)
f.add_button("Range 0 to 100", range100, 100)
f.add_button("Range 0 to 1000", range1000, 100)
f.add_input("Guess", input_guess, 200)
# This is the end of programme 
# Hope you have enjoyed the game
# Please play once again for better guessing!!!!!!!!!!!

  





# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

no_of_guesses = 0
low = 0 
high= 0
secret_number = 0


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number,  no_of_guesses, low, high
    
    secret_number = random.randrange(low,high)
    #print "secret number:" + str(secret_number)
    
    no_of_guesses = int(math.ceil(math.log((high - low + 1), 2)))
    print "New game. Range is from " + str(low) + " to " + str(high)
    print "Number of remaining guesses is " + str( no_of_guesses)
    print
    
    # remove this when you add your code    
    #pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global  no_of_guesses, high
    high = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global  no_of_guesses, high
    high = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global  no_of_guesses, secret_number, high
    
    player_guess = int(guess) 
    print "Guess was "+ guess
    
    no_of_guesses =  no_of_guesses - 1
    print "Number of remaining guesses: "+ str( no_of_guesses)
        
    if  no_of_guesses == 0 and player_guess != secret_number:
        print "You ran out of guesses. The number was " + str(secret_number)
        print
        new_game()
    elif player_guess == secret_number:
        print "Correct!"
        print
        new_game()
    elif player_guess < secret_number:
        print "Higher"
        print
    elif player_guess > secret_number:
        print "Lower"
        print
    # Clear the text box by setting it to an empty string
    user_input.set_text("")
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)
f.set_canvas_background("blue")

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100]", range100, 200)
f.add_button("Range is [0, 1000]", range1000, 200)
user_input = f.add_input("Enter a guess", input_guess, 200)

# call new_game 
range100()
f.start()
