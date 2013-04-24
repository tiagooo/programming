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

# libraries Import
import random

# function to convert number into name
def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "The number does not match!"
    return name    
    
# function to convert name into number    
def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "The name does not match!"
    return number

def rpsls(name): 
    # Conversion of the players play (name) into number
    number = name_to_number(name)
    # Randomly generated number for computer play 
    comp_number = random.randrange(0,5)
    # Conversion of the computer number into name
    comp_name = number_to_name(comp_number)
    # The remainder of the modular division between the difference of comp_number and number
    rem_diference = (comp_number - number)%5
    # Computation of the different options and display of the results
    if rem_diference == 0:
        print "Player chooses",name
        print "Computer chooses",comp_name
        print "Player and computer tie!"
        print ""
    elif rem_diference > 0 and rem_diference <=2:
        print "Player chooses",name
        print "Computer chooses",comp_name
        print "Computer wins!"
        print ""
    elif rem_diference >= 2 and rem_diference <=4:
        print "Player chooses",name
        print "Computer chooses",comp_name
        print "Player wins!"
        print ""
    return

#plays
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")