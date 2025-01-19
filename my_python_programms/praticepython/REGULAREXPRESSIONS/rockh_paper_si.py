import random
import re
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    game_images=[rock,paper,scissors]
    user_choice=(int)(input("What do you choose? Type 0 for 'rock',type 1 for 'paper' and type 2 for 'scissors'\n"))
    
    if user_choice >=0 and user_choice <=2:
        print(game_images [user_choice ])
        
    computer_choice=random.randint(0,2)
    print("Computer chose:",game_images [computer_choice ])
    
    if user_choice >=3 or user_choice <0:
        print("You typed an invalid number. You lose!")
    elif user_choice ==0 and computer_choice ==2:
        print("You win!")
        start_again = input("do you want to play again enter yes or no")
        start_again = start_again.upper()
        check =  re.compile(r'YES')
        gash = check.search(start_again)
        if gash != None:
           continue
        else:
            break
    elif computer_choice ==0 and user_choice ==2:
        print("You lose!")
        start_again = input("do you want to play again? enter yes or no\n")
        start_again = start_again.upper()
        check =  re.compile(r'YES')
        gash = check.search(start_again)
        if gash != None:
           continue
        else:
            break
    elif computer_choice >user_choice :
        print("You lose!")
        start_again = input("do you want to play again? enter yes or no\n")
        start_again = start_again.upper()
        check =  re.compile(r'YES')
        gash = check.search(start_again)
        if gash != None:
            continue
        else:
           break
    elif user_choice >computer_choice :
        print("You win!")
        start_again = input("do you want to play again? enter yes or no\n")
        start_again = start_again.upper()
        check =  re.compile(r'YES')
        gash = check.search(start_again)
        if gash != None:
           continue
        else:
           break
    elif computer_choice == user_choice :
        print("It's a draw!..")
        start_again = input("do you want to play again? enter yes or no\n")
        start_again = start_again.upper()
        check =  re.compile(r'YES')
        gash = check.search(start_again)
        if gash != None:
           continue
        else:
           break
    
