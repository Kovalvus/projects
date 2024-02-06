from random import *
from time import *

# -------------------------------------------------------------Variables related to accessing menus in main menu-------------------------------------------------------------------

StartAsk = ""  # Var for choosing the category in Main Menu
HelpAsk = ""  # Var for choosing the category in Help Menu
GameAsk = ""
PlayerName = ""

# -----------------------------------------------------------------------Variables related to gameplay-------------------------------------------------------------------

MaxHP = 0
PlayerHP = 0
DealerHP = 0
ChamberCapacity = 0
NoBlanks = 0
NoLives = 0

# ------------------------------------------------------------------------Variables related to items-------------------------------------------------------------------

PlayerInventory = []
DealerInventory = []

# Vars for checking if someone is handcuffed (0 = no, 1 = yes)
PlayerCuffed = 0  
DealerCuffed = 0
ShotgunSawed = 0 # Var for checking if the shotgun is currently sawed

# Vars for checking if Player/Dealer know the next shell via using the magnifying glass
PlayerKnows = 0
DealerKnows = 0

# Vars for checking if Player/Dealer have certain items
HandSaw = 0
HandCuffs = 0
CigarettePack = 0
Beer = 0
MagnifyingGlass = 0
DealerHandSaw = 0
DealerHandCuffs = 0
DealerCigarettePack = 0
DealerBeer = 0
DealerMagnifyingGlass = 0 



# ===================================================================All things related to the main menu=======================================================================

def Start():  # Main Menu
    global StartAsk
    print('*********************\nWelcome to Python Roulette!\n\n"Start" to start the game\n"Help" for game info\n"Quit" to quit the program\n')
    StartAsk = input()

    if(StartAsk == "Start" or StartAsk == "start"):
        Game()

    elif(StartAsk == "Help" or StartAsk == "help"):
        Help()

    elif(StartAsk == "Quit" or StartAsk == "quit"):
        exit()

    else:
        print("Error")
        Start()

def Help():  # Help Menu
        global HelpAsk
        print('\n*********************\n"Rules" to see the rules\n"Shotgun" to see how the shotgun works\n"Items" to see item descriptions\n"Game" for more info about the game\n"Quit" to go back\n')
        HelpAsk = input()

        if(HelpAsk == "Rules" or HelpAsk == "rules"):
            print("\n*********************\nBoth you and the Dealer have from 2 to 5 lives (the amount of lives\nis chosen randomly at the beginning of each round).\nThe goal is to kill the Dealer using the shotgun and given items.\n")
            Help()

        elif(HelpAsk == "Shotgun" or HelpAsk == "shotgun"):
            print("\n*********************\nAt the beginning of each round the shotgun is reloaded with shells that can be live or blanks.\nLive shells will deal 1 life of damage and blanks don't deal any damage.\nYou can choose to shoot yourself or the Dealer.\nIf you shoot yourself with a blank, the Dealer skips next turn.\nPointing the shotgun at the Dealer ends your turn.\n")
            Help()

        elif(HelpAsk == "Items" or HelpAsk == "items"):
            print("\n*********************\nYou will get items at the beginning of game 2 and 3 and after each shotgun reload.\nYou can get from 1 to 4 items.\nYou can hold up to 8 items at a time.\n\nHand Saw - Shotgun deals 2 damage.\nCigarette Pack - Regain 1 life.\nMagnifying Glass - Check the current shell in the chamber.\nBeer - You rack the shotgun, ends round on last shell.\nHandcuffs - Dealer skips the next turn.\n")
            Help()

        elif(HelpAsk == "Game" or HelpAsk == "game"):
            print('\n*********************\nThis game is a direct recreation of "Buckshot Roulette" by Mike Klubnika.\nThis is only a fan project not meant to be a malicious ripoff.\nYou can buy the original game for the minimum price of $1.20 USD on itch.io.\n(you can also copy the following link and paste it into your browser: https://mikeklubnika.itch.io/buckshot-roulette).\n')
            Help()

        elif(HelpAsk == "Quit" or HelpAsk == "quit"):
            Start()

        else:
            print("Error")
            Help()



# --------------------------------------------------------Game 1 code (the easiest one/ some sort of a tutorial)-----------------------------------------------------

# Game 1 rules: 
# round 1 --> guaranteed 2 blanks and 1-2 lives
# You can get 2-4 shells
# Max 3 HP
# No items
            
def Game(): # Round 1
    global PlayerName, MaxHP, PlayerHP, DealerHP, ChamberCapacity, NoBlanks, NoLives
    print("*********************\nYou enter the room at the end of the hallway...\n")
    sleep(1.5)
    print('You see the Dealer emerging from the shadows.\nHe hands you a document that reads:\n')
    sleep(2)
    print('"GENERAL RELEASE OF LIABILITY"\n')
    PlayerName = input('Enter Name: ')
    sleep(1)
    print('\nYou give him the document and the first game starts...\n')
    NoBlanks = 2
    NoLives = randint(1,2)
    ChamberCapacity = NoBlanks + NoLives
    NoBlanks = str(NoBlanks)
    NoLives = str(NoLives)
    MaxHP = 3
    PlayerHP = 3
    DealerHP = 3
    print('You both have 3 hp')
    sleep(1.5)
    print('Shells appear on the table...\n')
    sleep(1)
    print(NoBlanks+' Blanks and '+NoLives+' Lives\nDealer inserts the shells in an unknown order\n')
    sleep(3)
    print('*********************\nWhat do you choose to do?')
    PlayerTurn()

def RandomGame1():  # Rounds after round 1
    global PlayerName, MaxHP, PlayerHP, DealerHP, ChamberCapacity, NoBlanks, NoLives
    sleep(2)
    print("\n*********************\nShells have ran out\n")
    sleep(3)
    NoBlanks = randint(1,2)
    NoLives = randint(1,2)
    ChamberCapacity = NoBlanks + NoLives
    NoBlanks = str(NoBlanks)
    NoLives = str(NoLives)
    print('Shells appear on the table...\n')
    sleep(1)
    print(NoBlanks+' Blanks and '+NoLives+' Lives\nDealer inserts the shells in an unknown order\n')
    sleep(3)
    print('*********************\nWhat do you choose to do?')
    PlayerTurn()

# ======================================================================All Player related functions================================================================================

def PlayerTurn():  # Instructions what to type to use certain items / a "main menu"
    global PlayerInventory, HandSaw, CigarettePack, MagnifyingGlass, Beer, HandCuffs, MaxHP, PlayerHP, DealerHP
    sleep(3)
    print("\n\nYou have "+str(PlayerHP)+(" health\nThe Dealer has "+str(DealerHP)+" health\nThe max health for this game is "+str(MaxHP))+"\n")
    if (len(PlayerInventory) == 0):  #checking if you have any items
        print("\nYou have no items")
    else:
        NoItems = len(PlayerInventory)
        NoItems2 = NoItems
        print("Your items:\n")
        while (NoItems>0):  # listing all available items
            print("-"+PlayerInventory[NoItems2-NoItems])
            NoItems = NoItems-1
        print("\n")

    if (("Hand Saw" in PlayerInventory) == True):  # using the hand saw
        print('"Saw" to use the Hand Saw')
        HandSaw = 1

    if (("Cigarette Pack" in PlayerInventory) == True):  # using the cigarette pack
        print('"Cig" to use the Cigarette Pack')
        CigarettePack = 1
        
    if (("Magnifying Glass" in PlayerInventory) == True):  # using the magnifying glass
        print('"Mag" to use the Magnifying Glass')
        MagnifyingGlass = 1
        
    if (("Beer" in PlayerInventory) == True):  # using the beer
        print('"Beer" to use the Beer')
        Beer = 1
        
    if (("HandCuffs" in PlayerInventory) == True):  # using the handcuffs
        print('"Cuff" to use the HandCuffs')
        HandCuffs = 1
    
    print('"Shot" to pick up the shotgun')

    ItemChoice()

def ItemChoice():  # Choosing and using items
    global HandSaw, CigarettePack, MagnifyingGlass, Beer, HandCuffs, PlayerInventory, shoot, DealerCuffed, ChamberCapacity, PlayerKnows, ShotgunSawed, PlayerHP, MaxHP
    ItemChoicevar = input()
    if (ItemChoicevar == "Saw" or ItemChoicevar == "saw" and HandSaw == 1):  # Checking if the player chose saw and if they have it in the inventory 
        if (HandSaw == 1 and ShotgunSawed == 0):
            print("\nYou sawed off the shotgun")
            HandSaw = 0
            ShotgunSawed = 1
            PlayerInventory.remove("Hand Saw")
        PlayerTurn()

    elif (ItemChoicevar == "Cig" or ItemChoicevar == "cig" and CigarettePack == 1):  # Checking if the player chose ciggaretes and if they have it in the inventory 
        if (PlayerHP == MaxHP):
            print("You already have max HP")
        else:
            PlayerHP += 1
            print("You smoke a cigarette, now you have "+PlayerHP+" HP")
            CigarettePack = 0
            PlayerInventory.remove("Cigarette Pack")
        PlayerTurn()

    elif (ItemChoicevar == "Mag" or ItemChoicevar == "mag" and MagnifyingGlass == 1):  # Checking if the player chose magnifying glass and if they have it in the inventory 
        NextUp = randint(1,ChamberCapacity)
        if (NextUp <= int(NoBlanks)):  # it was a blank
            print("A Blank is next")
            PlayerKnows = 1  # Var checking if the player knows what shell will be next (via using the magnifying glass) 0 - doesn't know, 1 - knows and it's a blank, 2 - knows and it's a live
        else:
            print("A live is next")
            PlayerKnows = 2
        MagnifyingGlass = 0
        PlayerInventory.remove("Magnifying Glass")
        PlayerTurn()

    elif (ItemChoicevar == "Beer" or ItemChoicevar == "beer" and Beer == 1):  # Checking if the player chose beer and if they have it in the inventory 
        NextUp = randint(1,ChamberCapacity)
        if (NextUp <= int(NoBlanks)):  # it was a blank
            NoBlanks = int(NoBlanks)
            NoBlanks -= 1
            ChamberCapacity -= 1
            print("A blank fell out")
        else:
            NoLives = int(NoLives)
            NoLives -= 1
            ChamberCapacity -= 1
            print("A live fell out")
        Beer = 0
        PlayerInventory.remove("Beer")
        PlayerTurn()

    elif (ItemChoicevar == "Cuff" or ItemChoicevar == "cuff" and HandCuffs == 1):  # Checking if the player chose handcuffs and if they have it in the inventory 
        if (DealerCuffed == 0):
            HandCuffs = 0
            DealerCuffed = 1
            PlayerInventory.remove("HandCuffs")
        else:
            print("\nThe Dealer is already handcuffed")
        PlayerTurn()

    elif (ItemChoicevar == "Shot" or ItemChoicevar == "shot"):  #picking up the shotgun
        print("\nYou picked up the shotgun\nWho do you want to shoot?")
        print('"Dealer" to shoot the Dealer\n"Self" to shoot yourself\n"Cancel" to put the shotgun back')
        ShootTheShotgun()

    else:
        print("Enter a valid item name")
        ItemChoice()

def ShootTheShotgun():  # Shooting the shotgun, damaging yourself or the Dealer
    global shoot, NoBlanks, NoLives, ChamberCapacity, PlayerHP, DealerHP, ShotgunSawed, PlayerKnows, DealerCuffed
    shoot = input()
    if (shoot == "Dealer" or shoot == "dealer"):
        print("*********************\nYou point the shotgun at the Dealer...")  # pointing the shotgun at the Dealer
        sleep(3)
        if (PlayerKnows == 0):  # Player hasn't used the magnifying glass
            NextUp = randint(1,ChamberCapacity)  # randomising next shell in the chamber
        
        elif (PlayerKnows == 1):  # Player knows that it's gonna be a blank
            NextUp = int(NoBlanks)
            PlayerKnows = 0

        elif (PlayerKnows == 2):  # Player knows that it's gonna be a live
            NextUp = int(NoBlanks) + 1
            PlayerKnows = 0

        if (NextUp <= int(NoBlanks)):  # it was a blank
            print("*click*\n")
            sleep(1.5)
            print("It was a blank")
            NoBlanks = int(NoBlanks)
            NoBlanks -= 1
            ChamberCapacity -= 1
            if (ShotgunSawed == 1):
                print("\nThe barrel on the shotgun grew back...")
                ShotgunSawed = 0

            if (ChamberCapacity == 0):  # The round ended, cuz no shells are left
                RandomGame1()
            elif (ChamberCapacity > 0 and DealerCuffed == 1):  # Dealer is handcuffed so Player gets a second turn
                DealerCuffed = 0
                PlayerTurn()
            elif (ChamberCapacity > 0 and DealerCuffed == 0):  # Dealer isn't handcuffed so it's his turn
                DealerTurn()

        else:
            print("*BOOM*\n")  # it was a live
            sleep(1.0)
            print("It was a live")
            NoLives = int(NoLives)
            NoLives -= 1
            ChamberCapacity -= 1
            if (ShotgunSawed == 1):
                DealerHP -= 2
                ShotgunSawed = 0
                print("\nThe barrel on the shotgun grew back...")
            else:
                DealerHP -= 1

            if (ChamberCapacity == 0):  # The round ended, cuz no shells are left
                RandomGame1()
            elif (ChamberCapacity > 0 and DealerCuffed == 1):  # Dealer is handcuffed so Player gets a second turn
                DealerCuffed = 0
                PlayerTurn()
            elif (ChamberCapacity > 0 and DealerCuffed == 0):  # Dealer isn't handcuffed so it's his turn
                DealerTurn()
            
    elif (shoot == "Self" or shoot == "self"):
        print("*********************\nYou point the shotgun at yourself...")  # pointing the shotgun at yourself
        sleep(3)
        if (PlayerKnows == 0):  # Player hasn't used the magnifying glass
            NextUp = randint(1,ChamberCapacity)  # randomising next shell in the chamber
        
        elif (PlayerKnows == 1):  # Player knows that it's gonna be a blank
            NextUp = NoBlanks
            PlayerKnows = 0

        elif (PlayerKnows == 2):  # Player knows that it's gonna be a live
            NextUp = NoBlanks + 1
            PlayerKnows = 0
        if (NextUp <= int(NoBlanks)):  # it was a blank
            print("*click*\n")
            sleep(1.5)
            print("It was a blank")
            NoBlanks = int(NoBlanks)
            NoBlanks -= 1
            ChamberCapacity -= 1
            if (ShotgunSawed == 1):
                print("\nThe barrel on the shotgun grew back...")
                ShotgunSawed = 0

            if (ChamberCapacity == 0):  # If you blank yourself you skip Dealers turn by default so he doesn't get uncuffed here
                RandomGame1()
            else:
                PlayerTurn()
            
        else:
            print("*BOOM*\n")  # it was a live
            sleep(1.0)
            print("It was a live")
            NoLives = int(NoLives)
            NoLives -= 1
            ChamberCapacity -= 1
            if (ShotgunSawed == 1):
                PlayerHP -= 2
                ShotgunSawed = 0
                print("\nThe barrel on the shotgun grew back...")
            else:
                PlayerHP -= 1

            if (ChamberCapacity == 0):  # The round ended, cuz no shells are left
                RandomGame1()
            elif (ChamberCapacity > 0 and DealerCuffed == 1):  # Dealer is handcuffed so Player gets a second turn
                DealerCuffed = 0
                PlayerTurn()
            elif (ChamberCapacity > 0 and DealerCuffed == 0):  # Dealer isn't handcuffed so it's his turn
                DealerTurn()

    elif (shoot == "Cancel" or shoot == "cancel"):
        PlayerTurn()
    else:
        print("Enter a valid action")
        ShootTheShotgun()



# ========================================================================All Dealer related functions==============================================================================

def DealerTurn():  # the "main menu" of Dealers turn
    global DealerInventory, DealerHandSaw, DealerCigarettePack, DealerMagnifyingGlass, DealerBeer, DealerHandCuffs, MaxHP, PlayerHP, DealerHP, DealerKnows
    sleep(3)
    print("\n*********************\nYou have "+str(PlayerHP)+(" health\nThe Dealer has "+str(DealerHP)+" health\nThe max health for this game is "+str(MaxHP))+"\n")
    print("Now it's the Dealers turn...\n")
    sleep(2)
    if (len(DealerInventory) == 0):
        print("\n*********************\nThe Dealer has no items")
    else:
        NoItems = len(DealerInventory)
        NoItems2 = NoItems
        print("\n*********************\nDealers items:\n")
        while (NoItems>0):  # listing all available items
            print("-"+DealerInventory[NoItems2-NoItems])
            NoItems = NoItems-1
        print("\n")
        DealerKnows = 0
    sleep(2)
    DealerItemChoice()

# ----------------------------------------------------------------------The Dealers "AI" when using items--------------------------------------------------------------------------------

def DealerItemChoice():
    global DealerHandSaw, DealerCigarettePack, DealerMagnifyingGlass, DealerBeer, DealerHandCuffs, DealerInventory, DealerHP, PlayerHP, MaxHP, PlayerCuffed, NoBlanks, NoLives, DealerKnows, ChamberCapacity, ShotgunSawed
    if (("Hand Saw" in DealerInventory) == True):  #Checking which items the Dealer has
        DealerHandSaw = 1

    if (("Cigarette Pack" in DealerInventory) == True):  
        DealerCigarettePack = 1
        
    if (("Magnifying Glass" in DealerInventory) == True):  
        DealerMagnifyingGlass = 1
        
    if (("Beer" in DealerInventory) == True):  
        DealerBeer = 1
        
    if (("HandCuffs" in DealerInventory) == True): 
        DealerHandCuffs = 1

    if (DealerCigarettePack == 1 and DealerHP < MaxHP):  # Deciding if the Dealer will use the cigarettes
        print("\nThe Dealer used his Cigarette Pack")
        DealerHP += 1
        DealerCigarettePack = 0
        DealerInventory.remove("Cigarette Pack")
        sleep(3)
        DealerItemChoice()

    if (DealerHandCuffs == 1 and PlayerCuffed == 0):  # Deciding if the Dealer will use the handcuffs
        print("\nThe Dealer handcuffed you")
        DealerHandCuffs = 0
        PlayerCuffed = 1
        DealerInventory.remove("HandCuffs")
        sleep(3)
        DealerItemChoice()

    if (DealerMagnifyingGlass == 1 and NoLives != 0 and DealerKnows == 0):  # Deciding if the Dealer will use the magnifying glass
        print("\nThe Dealer used his magnifying glass and looked at the next shell")
        print('\n"Hmmm very interesting..."')

        NextUp = randint(1,ChamberCapacity)
        if (NextUp <= int(NoBlanks)):  # it was a blank
            DealerKnows = 1  # Var checking if the Dealer knows what shell will be next (via using the magnifying glass) 0 - doesn't know, 1 - knows and it's a blank, 2 - knows and it's a live
        else:
            DealerKnows = 2
        DealerMagnifyingGlass = 0
        DealerInventory.remove("Magnifying Glass")
        sleep(3)
        DealerItemChoice()
    
    if (DealerBeer == 1 and DealerKnows == 0 and NoBlanks != 0):
        print("\nThe Dealer drank the beer and racked the shotgun")
        NextUp = randint(1,ChamberCapacity)
        if (NextUp <= int(NoBlanks)):  # it was a blank
            NoBlanks = int(NoBlanks)
            NoBlanks -= 1
            ChamberCapacity -= 1
            print("A blank fell out")
        else:
            NoLives = int(NoLives)
            NoLives -= 1
            ChamberCapacity -= 1
            print("A live fell out")
        DealerBeer = 0
        DealerInventory.remove("Beer")
        sleep(3)
        DealerItemChoice()
    
    if (DealerHandSaw == 1 and ShotgunSawed == 0):
        print("\nThe Dealer sawed off the shotgun")
        DealerHandSaw = 0
        ShotgunSawed = 1
        DealerInventory.remove("Hand Saw")
        sleep(3)
        DealerItemChoice()
    
    DealerShoots()

# ----------------------------------------------------------------------the Dealers "AI" when shooting----------------------------------------------------------------

def DealerShoots():
    global ShotgunSawed, DealerKnows, PlayerHP, MaxHP, NoBlanks, NoLives, ChamberCapacity, DealerHP
    print("\n*********************\nThe Dealer picked up the shotgun...")
    sleep(3)
    
    if (DealerKnows == 0):  # Dealer hasn't used the magnifying glass
        NextUp = randint(1,ChamberCapacity)  # randomising next shell in the chamber
        
    elif (DealerKnows == 1):  # Dealer knows that it's gonna be a blank
        NextUp = int(NoBlanks)

    elif (DealerKnows == 2):  # Dealer knows that it's gonna be a live
        NextUp = int(NoBlanks) + 1
    
    if (NextUp <= int(NoBlanks) and DealerKnows == 1):  # Dealer knew it was a blank
        print("The Dealer points the shotgun at himself")
        sleep(3)
        print("*click*\n")
        print("It was a blank")
        NoBlanks = int(NoBlanks)
        NoBlanks -= 1
        ChamberCapacity -= 1
        if (ShotgunSawed == 1):
            print("\nThe barrel on the shotgun grew back...")
            ShotgunSawed = 0

        if (ChamberCapacity == 0):  # Even if you're handcuffed Dealer by blanking himself skips your turn so you'd stay cuffed
            RandomGame1()
        else:
            DealerTurn()

    elif (NextUp > int(NoBlanks) and DealerKnows == 2):  # Dealer knew it was a live
        print("The Dealer points the shotgun at you")
        sleep(3)
        print("*BOOM*\n")
        print("It was a live")
        NoLives = int(NoLives)
        NoLives -= 1
        ChamberCapacity -= 1
        if (ShotgunSawed == 1):
            PlayerHP -= 2
            print("\nThe barrel on the shotgun grew back...")
            ShotgunSawed = 0
        else:
            PlayerHP -= 1

        PlayerIsCuffedCheck()

    elif (DealerKnows == 0):

        # -------------------------------------------------------------------Dealer has more HP---------------------------------------------------------------------
        if (DealerHP > PlayerHP):
            shootchoice = randint(1,3)  # Dealer has more HP than the player so he has a bigger chance of pointing the shotgun at himself (1-2)
            if (shootchoice <= 2):
                print("The Dealer points the shotgun at himself")
                sleep(3)
                if (NextUp <= int(NoBlanks)):  # It's a blank (Dealer at himself)
                    print("*click*\n")
                    sleep(1.5)
                    print("It was a blank")
                    NoBlanks = int(NoBlanks)
                    NoBlanks -= 1
                    ChamberCapacity -= 1
                    if (ShotgunSawed == 1):
                        print("\nThe barrel on the shotgun grew back...")
                        ShotgunSawed = 0

                    if (ChamberCapacity == 0):  # Even if you're handcuffed Dealer by blanking himself skips your turn so you'd stay cuffed
                        RandomGame1()
                    else:
                        DealerTurn()

                else:  # It's a live (Dealer at himself)
                    print("*BOOM*\n")
                    sleep(1.0)
                    print("It was a live")
                    NoLives = int(NoLives)
                    NoLives -= 1
                    ChamberCapacity -= 1
                    if (ShotgunSawed == 1):
                        DealerHP -= 2
                        print("\nThe barrel on the shotgun grew back...")
                        ShotgunSawed = 0
                    else:
                        DealerHP -= 1

                    PlayerIsCuffedCheck()

            else:
                print("The Dealer points the shotgun at you")
                sleep(3)
                if (NextUp <= int(NoBlanks)):  # It's a blank (Dealer at you)
                    print("*click*\n")
                    sleep(1.5)
                    print("It was a blank")
                    NoBlanks = int(NoBlanks)
                    NoBlanks -= 1
                    ChamberCapacity -= 1
                    if (ShotgunSawed == 1):
                        print("\nThe barrel on the shotgun grew back...")
                        ShotgunSawed = 0

                    PlayerIsCuffedCheck()

                else:  # It's a live (Dealer at you)
                    print("*BOOM*\n")
                    sleep(1.0)
                    print("It was a live")
                    NoLives = int(NoLives)
                    NoLives -= 1
                    ChamberCapacity -= 1
                    if (ShotgunSawed == 1):
                        PlayerHP -= 2
                        print("\nThe barrel on the shotgun grew back...")
                        ShotgunSawed = 0
                    else:
                        PlayerHP -= 1
                        
                    PlayerIsCuffedCheck()

        # ------------------------------------------------------------------Dealer has less HP---------------------------------------------------------------------
        elif (DealerHP < PlayerHP):
            shootchoice = randint(1,3)
            if (shootchoice == 1):
                print("The Dealer points the shotgun at himself")
                sleep(3)
                if (NextUp <= int(NoBlanks)):  # It's a blank (Dealer at himself)
                    print("*click*\n")
                    sleep(1.5)
                    print("It was a blank")
                    NoBlanks = int(NoBlanks)
                    NoBlanks -= 1
                    ChamberCapacity -= 1
                    if (ShotgunSawed == 1):
                        print("\nThe barrel on the shotgun grew back...")
                        ShotgunSawed = 0

                    if (ChamberCapacity == 0):  # Even if you're handcuffed Dealer by blanking himself skips your turn so you'd stay cuffed
                        RandomGame1()
                    else:
                        DealerTurn()

                else:  # It's a live (Dealer at himself)
                    print("*BOOM*\n")
                    sleep(1.0)
                    print("It was a live")
                    NoLives = int(NoLives)
                    NoLives -= 1
                    ChamberCapacity -= 1
                    if (ShotgunSawed == 1):
                        DealerHP -= 2
                        print("\nThe barrel on the shotgun grew back...")
                        ShotgunSawed = 0
                    else:
                        DealerHP -= 1

                    PlayerIsCuffedCheck()

            else:
                print("The Dealer points the shotgun at you")
                sleep(3)
                if (NextUp <= int(NoBlanks)):  # It's a blank (Dealer at you)
                    print("*click*\n")
                    sleep(1.5)
                    print("It was a blank")
                    NoBlanks = int(NoBlanks)
                    NoBlanks -= 1
                    ChamberCapacity -= 1
                    if (ShotgunSawed == 1):
                        print("\nThe barrel on the shotgun grew back...")
                        ShotgunSawed = 0

                    PlayerIsCuffedCheck()

                else:  # It's a live (Dealer at you)
                    print("*BOOM*\n")
                    sleep(1.0)
                    print("It was a live")
                    NoLives = int(NoLives)
                    NoLives -= 1
                    ChamberCapacity -= 1
                    if (ShotgunSawed == 1):
                        PlayerHP -= 2
                        print("\nThe barrel on the shotgun grew back...")
                        ShotgunSawed = 0
                    else:
                        PlayerHP -= 1

                    PlayerIsCuffedCheck()

        # -----------------------------------------------------Dealer has the same amount of HP as the Player---------------------------------------------------
        else:
            shootchoice = randint(1,2)
            if (shootchoice == 1):
                print("The Dealer points the shotgun at himself")
                sleep(3)
                if (NextUp <= int(NoBlanks)):  # It's a blank (Dealer at himself)
                    print("*click*\n")
                    sleep(1.5)
                    print("It was a blank")
                    NoBlanks = int(NoBlanks)
                    NoBlanks -= 1
                    ChamberCapacity -= 1
                    if (ShotgunSawed == 1):
                        print("\nThe barrel on the shotgun grew back...")
                        ShotgunSawed = 0

                    if (ChamberCapacity == 0):  # Even if you're handcuffed Dealer by blanking himself skips your turn so you'd stay cuffed
                        RandomGame1()
                    else:
                        DealerTurn()

                else:  # It's a live (Dealer at himself)
                    print("*BOOM*\n")
                    sleep(1.0)
                    print("It was a live")
                    NoLives = int(NoLives)
                    NoLives -= 1
                    ChamberCapacity -= 1
                    if (ShotgunSawed == 1):
                        DealerHP -= 2
                        print("\nThe barrel on the shotgun grew back...")
                        ShotgunSawed = 0
                    else:
                        DealerHP -= 1

                    PlayerIsCuffedCheck()

            else:
                print("The Dealer points the shotgun at you")
                sleep(3)
                if (NextUp <= int(NoBlanks)):  # It's a blank (Dealer at you)
                    print("*click*\n")
                    sleep(1.5)
                    print("It was a blank")
                    NoBlanks = int(NoBlanks)
                    NoBlanks -= 1
                    ChamberCapacity -= 1
                    if (ShotgunSawed == 1):
                        print("\nThe barrel on the shotgun grew back...")
                        ShotgunSawed = 0

                    PlayerIsCuffedCheck()

                else:  # It's a live (Dealer at you)
                    print("*BOOM*\n")
                    sleep(1.0)
                    print("It was a live")
                    NoLives = int(NoLives)
                    NoLives -= 1
                    ChamberCapacity -= 1
                    if (ShotgunSawed == 1):
                        PlayerHP -= 2
                        print("\nThe barrel on the shotgun grew back...")
                        ShotgunSawed = 0
                    else:
                        PlayerHP -= 1

                    PlayerIsCuffedCheck()



# ====================================================================-Other Miscellaneous functions==============================================================================
                    
def PlayerIsCuffedCheck():
    global ChamberCapacity, PlayerCuffed
    if (ChamberCapacity == 0):  # The round ended, cuz no shells are left
        RandomGame1()
    elif (ChamberCapacity > 0 and PlayerCuffed == 1):  # Player is handcuffed so Dealer gets a second turn
        PlayerCuffed = 0
        DealerTurn()
    elif (ChamberCapacity > 0 and PlayerCuffed == 0):  # Player isn't handcuffed so it's their turn
        PlayerTurn()

Start()  # Launch the game
input()