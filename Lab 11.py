#A program that generates a specified amount of addition/subtraction problems and prints your results. 
#Created by: Chris Caponi

import random
#mainFunc
def main():
#Track win/loss ratio
    wins = 0
    losses = 0
    action = ["add", "subtract", "stop"]
    flag = True
    while (flag == True):
        #get user input(addition,subtraction, or stop)
        whatKind = input("What would you like to do? Enter\nadd\nsubtract\nor stop to quit. ")
        #validate input (while loop within statement)
        while (not (whatKind in action)):
            whatKind = input("What would you like to do? Enter\nadd\nsubtract\nor stop to quit. ")

        if (whatKind == "stop"):
            print("In total you got {} correct, and {} wrong.".format(wins, losses))
            flag = False
            break
        #get user input(how many problems to solve?)
        howMany = int(input("How many problems do you want to solve? "))
        #call appropriate function(if/elif/else statement)
        if (whatKind == "add"):
            w, l = addFunc(howMany)
            wins = wins + w
            losses = losses + l
        elif (whatKind == "subtract"):
            w, l = subFunc(howMany)
            wins = wins + w
            losses = losses + l

def getRand(min, max):
    #2 parameters: min/max range inclusive
    rand1 = random.randrange(min, max)
    rand2 = random.randrange(min, max)  
    return (rand1, rand2) 

def addFunc(howMany):
    #1 parameter: num of addition questions
    addWin = 0
    addLoss = 0 
    #for loop using num of questions specified by user
    for x in range(howMany):
        r1, r2 = getRand(2, 20)
        answer = int(input("What is {} plus {}? ".format(r1, r2) ))
        #Check user input (Display correct answer if wrong)
        if (answer == (r1 + r2)):
            print("good job!!")
            addWin = addWin + 1
        else: 
            print("sorry, the answer was {}".format(r1 + r2))
            addLoss = addLoss + 1
    #Update win/loss total
    print("You got {} right and {} wrong.".format(addWin, addLoss)) 
    #Return win/loss
    return (addWin, addLoss)


def subFunc(howMany):
    #1 parameter: num of subtraction questions
    subWin = 0
    subLoss = 0 
    #for loop using num of questions specified by user
    for x in range(howMany):
        r1, r2 = getRand(1, 15)
        answer = int(input("What is {} minus {}? ".format(r1, r2) ))
        #Check user input (Display correct answer if wrong)
        if (answer == (r1 - r2)):
            print("good job!!")
            subWin = subWin + 1
        else: 
            print("sorry, the answer was {}".format(r1 - r2))
            subLoss = subLoss + 1
    #Update win/loss total
    print("You got {} right and {} wrong.".format(subWin, subLoss)) 
    #Return win/loss
    return (subWin, subLoss)
#call the main function
main()

print(input("press enter to exit."))

