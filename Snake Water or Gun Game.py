import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Computer's turn: Snake(s) Water(w) or Gun(g)? ")

randno = random.randint(1,3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'w'
else:
    comp = 'g'

you = input("Player's turn: Snake(s) Water(w) or Gun(g)? ")

print(f"Computer choose {comp}")
print(f"you choose {you}")

a = gamewin(comp, you)

if a == None:
    print("It's a Tie")
elif a == True:
    print("You Win!")
else:
    print("You Lose")
