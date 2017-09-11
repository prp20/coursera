#http://www.codeskulptor.org/#user40_6c0pLiasi7mIpre_3.py
#http://www.codeskulptor.org/#user40_L4WoDyUJW5J3OiC.py
#http://www.codeskulptor.org/#user40_uDxfckSJeSsxUKF.py
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
# The user inputs the value of his choice 
# Accordingly the copmputer generates a choice of its 
# Then with comparison of both the options the winneris decided
# YIPIEE !!!!!!!!!!!!!!!!!!so lets begin the game

# Firstly we import the file
import random

# This is a function that accepts the above name and
# assigns to its the respective number 
# according to the  above mentioned list
def name_to_number(name):
    if(name=="rock"):
        n=0
        return n
    elif(name=="spock"):
        n=1
        return n
    elif(name=="paper"):
        n=2
        return n
    elif(name=="lizard"):
        n=3
        return n
    elif(name=="scissors"):
        n=4
        return n
    else:
        n=5
        return n
    
# This function accepts the number and assign to it its 
# respective names according to the above list
def number_to_name(number):
    if(number==0):
        name="rock"
        return name
    elif(number==1):
        name="spock"
        return name
    elif(number==2):
        name="paper"
        return name
    elif(number==3):
        name="lizard"
        return name
    elif(number==4):
        name="scissors"
        return name
    else:
        name="invalid input"
        return name
    
# This is the main function of the program where the
# real game begins
# the player input and the copmuter generated input is  accepted 
# ,compared and the results are announced 
def rpsls(guess):
    player_choice=name_to_number(guess)
    print "                                  "
    print "player chooses",number_to_name(player_choice)
    comp_number=random.randrange(0, 5)
    print "computer chooses", number_to_name(comp_number)

# The logic that decides who is the winner begins here
# the value of computer and palyer are taken and subtracted
# The result of the above expression is then made to undergo modulo division
# i.e %5
# if the result is more than or equal to 3 than player wins
# if result is equal then it is a tie between computer and player
# If the result is less than 3 than computer wins
    if(((comp_number-player_choice)%5)>=3):
        print "Player wins!"
    elif(comp_number==player_choice):
        print "Player and Computer tie!"
    else:
        print "Computer wins!"

# the program written above needs to be tested 
# So lets enter few values and see what happens to code
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# This is the end of the program
# Hope you have enjoyed the game

