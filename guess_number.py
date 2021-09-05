import random

# GUESS THE NUMBER GAME

play="y"
flag=True
print("------------------------------")
print("Guess The Number Game")
print("------------------------------")
print("Rules: \n 1. Number should be in range of 1 to 20")
print("------------------------------")
# For Plaing Game Again And Again
while play.lower()=="y":
    # Computer Choosing Random Number From The Range Mentioned
    comp_num=random.randint(1,20)
    #print(comp_num)
    # Setting Flag, Because To Continue From Here After The 'continue' in while
    # It Will Not Go To Outside While, So Computer Will Not Generate Random Variable Again And Again After Getting 'continue'
    while flag==True:
        # To Check If Input Is Integer Or Not
        try:
            your_num=int(input("Enter a number in range of 1 to 20 : "))
            # TO Check If Entered Variable Is In THe Range Or Not
            if your_num>=1 and your_num<=20:
                pass
            else:
                print("Invalid Input")
                continue
            # To Check Wheather Input From User Is Greater Than, Smaller Than Or Equal To Computer Generated Number
            if your_num>comp_num:
                print("Your Guessed Number is Larger")
                continue
            elif your_num<comp_num:
                print("Your Guessed Number is Smaller")
                continue
            elif your_num==comp_num:
                print("------------------------------")
                print("Hooray! You Guessed correct Number")
                print("------------------------------")
                break
        # If Input Is Not Integer Then It Will Display This
        except:
            print("Invalid Input: Enter only number")
            continue
    # Input For Playing Again
    play=input("If you want to play again enter 'y' : ")
    print("------------------------------")
print("Thanks For Playing")
print("------------------------------")