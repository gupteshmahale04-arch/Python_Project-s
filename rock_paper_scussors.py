import random

user_wins = 0
computer_wins = 0 

options = ['rock','paper','scissors']

while True :
    
    user_input = input ("Type Rock/ Paper/ Scissors or Q to quit  ").lower()
    
    if user_input=="q":
        quit()
        
        
    if user_input not  in options:
        print("Pless only Type Rock/ Paper/ Scissors or Q to quit ")
        continue
    random_number = random.randint(0,2)
    # Rock : 0 , Paper : 1 , scissors : 2
    
    computer_pick = options[random_number]
    
    if computer_pick == user_input :
        pass

    
    
print( f"Your point {user_wins} and computer point {computer_wins} out of {user_wins + computer_wins}")
print("Good Bye!!!!!!!")
        
        
        
        