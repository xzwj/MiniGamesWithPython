# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

secret_number = None
range = 100
remain_num = 7
is_begin = True


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, range, remain_num, is_begin
    
    if(is_begin):
        is_begin = False
    else:
        print
    remain_num = int(math.ceil(math.log(range + 1, 2)))
    print "New game. Range is from 0 to",range
    print "Number of remaining guesses is", remain_num
    secret_number = random.randrange(0, range)
    # print "secret_number =", secret_number

    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game    
    global range
    range = 1000    
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number, remain_num
    
    guess_number = int(guess)
    remain_num = remain_num - 1
    print
    print "Guess was", guess_number
    print "Number of remaining guesses is", remain_num
    
    # compares the entered number to secret_number
    if(secret_number == guess_number):
        print "Correct!"
        new_game()
    else:
        if(secret_number > guess_number):       print "Higher!"
        elif(secret_number < guess_number):     print "Lower!"
        
        if(remain_num <= 0):
            print "hahahaha~~ YOU LOSE! The number was", secret_number
            new_game()
    
    
# create frame
frame = simplegui.create_frame("Guess the number", 200,200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)
#frame.start()

# call new_game 
new_game()
frame.start()
