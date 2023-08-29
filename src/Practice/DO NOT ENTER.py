import random


user_wins = "0"
AI_wins = "0"

options = ["rock", "paper", "scissor"]
options[0]


while True:
    user_choice=input("Type rock, paper,scissor or q to leave: ")
    if user_choice == "q":
        break

    if user_choice not in options:
        continue

    random_number = random.randint(0, 2)

    AI_chose=options[random_number ]
    print("AI chose", AI_chose + ".")
    #own try
    if user_choice == "rock" and AI_chose == "scissor":
        print("You Win!")
        continue

    elif user_choice == "paper" and AI_chose == "rock":
        print("You Win!")
        continue


    elif user_choice == "scissor" and AI_chose == "paper":
        print("You Win!")
        continue

    else:
        print("You Lost! :( ")
        continue



print("Goodbye! :) ")
