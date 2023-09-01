import random

choice=["Rock","Paper","Scissor"]
while True:
    try:
        ui=int(input("Enter 0 for Rock , 1 for Paper and 2 for Scissor : "))
    except ValueError:
        print("Please enter a valid choice!")
        continue

    if (ui<0 or ui>2):
        print("Please enter a valid choice!")
        continue

    ci=random.randint(0,2)
    
    user_input=choice[ui]
    comp_input=choice[ci]

    if (ui==0 and ci==2) or (ui==1 and ci==0) or (ui==2 and ci==1):
        print(f"You chose {user_input}.")
        print("You Won!")
        print(f"Computer chose {comp_input}.")
    
    elif (ui==0 and ci==1) or (ui==1 and ci==2) or (ui==2 and ci==0):
        print(f"You chose {user_input}.")
        print("You Lost!")
        print(f"Computer chose {comp_input}.")

    elif (ui==ci):
        print(f"You chose {user_input}.")
        print("It's a Draw!")
        print(f"Computer also chose {comp_input}.")

    again=input("Would you like to play again ? ( Y/N ) : ")

    while again.upper() not in("Y","N"):
            print("Please enter a valid choice!")
            again=input("Would you like to play again ? ( Y/N ) : ")

    if again.upper()=="Y":
        continue

    elif again.upper()=="N":
        print("Thank you for using the Password Generator. Goodbye!")
        break