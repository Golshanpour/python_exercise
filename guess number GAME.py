import random

def computer_number():
    comp_num = random.randint(1, 101)
    return comp_num
   
def gamer_number():
    gamer_num = int(input("\nguess a number between 1 to 100 : " ))
    return gamer_num

def gamer_number_again():
    gamer_num = int(input("\nguess another number ==>> " ))
    return gamer_num

def continue_game():
    token = input("whoud you like to play game again ? Yes/No ?")
    if token in ['y', 'yes', 'Y', 'Yes']:
        return True
    else:
        return False

#======================================================================== 
def start_game():

    comp_num = computer_number()
    gamer_num = gamer_number()
    counter = 1

    while comp_num != gamer_num:
        
        if comp_num > gamer_num:
            print("\nmy number is GREATER than you !!!")
            gamer_num = gamer_number_again()
            counter += 1
        if comp_num < gamer_num:
            print("\nmy number is SMALLER than you !!!") 
            gamer_num = gamer_number_again()
            counter += 1
        
    print(f"\n WooOOOOOooooOOOOooW \n by {counter} round of game you WIN !!! :) \n")
    
#=============================================================================
def main():
    start_game()
    while continue_game():
        start_game()
    else:
        print("\ngood luck baby :)\n")
    

main()