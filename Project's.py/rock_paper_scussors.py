import random
print("""
===================================================================================================================================================================
                                                            ! Welcome to Rock Paper Scissors Game !
===================================================================================================================================================================

""")
user_wins = 0
computer_wins = 0 

options = ['rock','paper','scissors']

while True :
    
    user_input = input ("Type Rock/ Paper/ Scissors or Q to quit  ").lower()
    
    if user_input=="q":
        
        break
        
        
    if user_input not  in options:
        print("Pless only Type Rock/ Paper/ Scissors or Q to quit ")
        continue
    random_number = random.randint(0,2)
    # Rock : 0 , Paper : 1 , scissors : 2
    
    computer_pick = options[random_number]
    
    if computer_pick == user_input :
        print("Draw!( same to same ^!!^ )")
        
    elif computer_pick == options[2] and  user_input == options[0] or \
        computer_pick == options[1] and  user_input == options[2] or \
        computer_pick == options[0] and  user_input == options[1] :
        print("You Win!")
        
        user_wins+=1
    else:
        print(" Computer Win ! ")
        computer_wins+=1
    print("Computer Pick ",computer_pick+".")
          
    
print(f"Your points: {user_wins}")
print(f"Computer points: {computer_wins}")
print(f"Total rounds: {user_wins + computer_wins}")
print("Good Bye!!!!!!!")
        
        
        
        