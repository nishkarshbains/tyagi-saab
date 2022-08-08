import random
import pyfiglet
a = print('''                                           WELCOME TO ROCK PAPER SCISSOR GAME''')
b = input("Enter Your Name ")

user_wins = 0
computer_wins = 0



Option =["rock","paper","scissors"]


while True : 
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break


    if user_input not in ["rock","paper","scissors"]:
        continue


    random_number = random.randint(0,2)
    # rock: 0 , paper: 1 , scissors: 2
      
    computer_pick = Option[random_number]
    print("Computer picked", computer_pick + ".") 

    if user_input == "rock" and computer_pick == "scissors":
        print("YOU WON!")
        user_wins += 1


    elif user_input == "paper" and computer_pick == "rock":
        print("YOU WON!")    
        user_wins += 1


    elif user_input == "scissors" and computer_pick == "paper":
        print("YOU WON!")
        user_wins += 1  

    else:
        print("YOU LOST!")
        computer_wins += 1
     

 
print("You won", user_wins, "times.")
print("the computer won", computer_wins, "times.") 
print()
print()
print("THANK YOU FOR PLAYING",b)



print()
print()
print()
print()

print(pyfiglet.figlet_format("ANSH TYAGI",justify="center"))
             

print()
print()


print('''     GOODBYE!''')