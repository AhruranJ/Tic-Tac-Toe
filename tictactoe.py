import time

unclaimed = ["1A", "2A", "3A", "1B", "2B", "3B", "1C", "2C", "3C"]
X = []
O = []

XA = 0
XB = 0
XC = 0
Xone = 0
Xtwo = 0
Xthree = 0

OA = 0
OB = 0
OC = 0
Oone = 0
Otwo = 0
Othree = 0

gameEnded = False

print()
print("#########################")
print("###### TIC TAC TOE ######")
print("#########################")
print()
print()
print("A B C")
print("□ □ □  1")
print("□ □ □  2")
print("□ □ □  3")
print()
time.sleep(1.5)
print("To play, add the number digit first, then the letter second to create your coordinate, it would be like 1A, 2B, 3C, etc.")
print()



def Xinput():
    global XA, XB, XC, Xone, Xtwo, Xthree
    Xask = input("What do you claim for X? ")
    if Xask in unclaimed:
        if Xask[0] == "1":
            Xone += 1
        elif Xask[0] == "2":
            Xtwo += 1
        elif Xask[0] == "3":
            Xthree += 1
        if Xask[1] == "A":
            XA += 1
        elif Xask[1] == "B":
            XB += 1
        elif Xask[1] == "C":
            XC += 1
    
        unclaimed.remove(Xask)
        X.append(Xask)
        print(f"X captures {Xask}")
    else:
        print("Invalid, try again")
        Xinput()

def Oinput():
    global OA, OB, OC, Oone, Otwo, Othree
    Oask = input("What do you claim for O? ")
    if Oask in unclaimed:
        if Oask[0] == "1":
            Oone += 1
        elif Oask[0] == "2":
            Otwo += 1
        elif Oask[0] == "3":
            Othree += 1
        if Oask[1] == "A":
            OA += 1
        elif Oask[1] == "B":
            OB += 1
        elif Oask[1] == "C":
            OC += 1
        unclaimed.remove(Oask)
        O.append(Oask)
        print(f"O captures {Oask}") 
    else:
        print("Invalid, try again")
        Oinput()

def victoryCheck():
    if unclaimed == []:
        print("It's a Draw!")
        endgame()
    elif "1A" in X and "2B" in X and "3C" in X: #Diagonal victories
        print("X wins!")
        endgame()
    elif "1C" in X and "2B" in X and "3A" in X:
        print("X wins!")
        endgame()
    elif "1A" in O and "2B" in O and "3C" in O:
        print("O wins!")
        endgame()
    elif "1C" in O and "2B" in O and "3A" in O:
        print("O wins!")
        endgame()
    elif XA == 3 or XB == 3 or XC == 3 or Xone == 3 or Xtwo == 3 or Xthree == 3: #Straight Cross victory of X
        print("X wins!")
        endgame()
    elif OA == 3 or OB == 3 or OC == 3 or Oone == 3 or Otwo == 3 or Othree == 3: #Straight Cross victory of O
        print("O wins!")
        endgame()

def endgame(): #Ends the game
    gameEnded = True
    time.sleep(5)
    
#Circulation of Turns      
while gameEnded == False:
    Xinput()
    print()
    victoryCheck()
    Oinput()
    print()
    victoryCheck()
    

        
