import random

l = ["Rock", "Paper", "Scissor"]

while True:
    ucount = 0
    ccount = 0

    uc = int(input('''
Game Start.....
If you wanna play game type
1 to start the game
2 to exit the game
'''))
    if uc == 1:
        for i in range(1,6):
            ui = int(input('''
                Press 1 for Rock
                Press 2 for Paper
                Press 3 for Scissors
'''))
            if ui == 1:
                uchoice = "Rock"
            elif ui == 2:
                uchoice = "Paper"
            elif ui == 3:
                uchoice = "Scissor"
            else:
                break
            cchoice = random.choice(l)
            if cchoice == uchoice:
                print("Computer Choice", cchoice)
                print("User Choice", uchoice)
                print("Game Draw")
                ccount += 1
                ucount += 1
            elif (uchoice == "Rock" and cchoice == "Scissor") or (uchoice == "Paper" and cchoice == "Rock") or (uchoice == "Scissor" and cchoice == "Paper"):
                print("Computer Choice", cchoice)
                print("User Choice", uchoice)
                print("You Win!")
                ucount += 1
            else:
                print("Computer Choice", cchoice)
                print("User Choice", uchoice)
                print("You Lose!")
                ccount += 1
        print("____________________User Points = ", ucount)
        print("____________________Computer Points = ", ccount)
    else:
        break