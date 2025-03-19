import random


#Establish a score system from the start
round = 0
wins = 0
loss = 0

#These are the possible options for the game 
Options = ['r' , 'p' , 's']

while True:
    response = input('Type either "R" ,"P" or "S" to start or type "Q" to quit: ').lower()
    if response == 'q':
        break 

    #The break will close the whole loop and reveal the scores 


    if response not in Options:
        continue

    #The continue will just re-prompt the question if a non valid answer was given



    Random = random.randint(0,2) # This establishes that only 0 , 1 and 2 can be picked
    computer = Options[Random] # r = 0 , p = 1 and s = 2

    print("Computer picked " + computer)


# These are all the conditions for the user to win

    if response == 'r' and computer == 's':
        print("Computer picked scissors!")
        print("YOU WIN!")
        round += 1
        wins += 1
    
    
    elif response == 'p' and computer == 'r':
        print("Computer picked rock!")
        print("YOU WIN!")
        round += 1
        wins += 1

    
    elif response == 's' and computer == 'p':
        print("Computer picked paper!")
        print("YOU WIN!")
        round += 1
        wins += 1


    
# These are the conditions for a draw

    elif response == 's' and computer == 's':
        print("Computer picked scissors!")
        print("Draw!")
        round +=1
    


    elif response == 'p' and computer == 'p':
        print("Computer picked paper!")
        print("Draw!")
        round += 1

    

    elif response == 'r' and computer == 'r':
        print("Computer picked rock!")
        print("Draw!")
        round += 1



# These are the conditions for a loss
    else:
        print('Computer won')
        round +=1
        loss += 1



print('There were ' + str(round) + ' rounds')
print('You have won ' + str(wins) + ' times')
print('The computer has won ' + str(loss) + ' times')
print('Til next time!')


