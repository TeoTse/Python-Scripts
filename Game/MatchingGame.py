import random

#Function that creates all the cards of the game depending on the level the user enters
def CardSet(n,AllCards):
    symbols = ["♥","♦","♠","♣"]
    if(n == 16): #Easy level contains 16 cards
        values = ['10', 'J', 'Q', 'K']
        for symbol in symbols:
            for value in values:
                AllCards.append(Card(symbol,10,value+symbol,False))
    if(n == 40): #Medium level contains 40 cards
        values = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10']
        for symbol in symbols:
            for value in values:
                if(value == "A"):
                    AllCards.append(Card(symbol,1,value+symbol,False))
                if(value != "A"):
                    AllCards.append(Card(symbol,int(value),value+symbol,False))
    if(n == 52):#Hard level contains 52 cards
        values = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for symbol in symbols:
            for value in values:
                if(value == "J" or value == "Q" or value == "K"):
                    AllCards.append(Card(symbol,10,value+symbol,False))
                elif(value == "A"):
                    AllCards.append(Card(symbol,1,value+symbol,False))
                else:
                    AllCards.append(Card(symbol,int(value),value+symbol,False))

#Function that sets all cards at either open or closed(Used to open and show all cards at the start of the game and then close them)
def SetStateAll(state,AllCards,n):
    for i in range(n):
        AllCards[i].SetStat(state)
 
#Function that sets up the graphic part easy difficulty
def Easy(AllCards):
    print("      1     2     3     4")
    print("1     ",end = "")
    for i in range(4):
        if(AllCards[i].GetStat() == False):
            print("X     ",end = "")
        else:
            print(AllCards[i].GetDesc(),"   ",end= "")
    print("")
    print("")
    print("2     ",end = "")
    for i in range(4):
        if(AllCards[i+4].GetStat() == False):
            print("X     ",end = "")
        else:
            print(AllCards[i+4].GetDesc(),"   ",end= "")
    print("")
    print("")
    print("3     ",end = "")
    for i in range(4):
        if(AllCards[i+8].GetStat() == False):
            print("X     ",end = "")
        else:
            print(AllCards[i+8].GetDesc(),"   ",end= "")
    print("")
    print("")
    print("4     ",end = "")
    for i in range(4):
        if(AllCards[i+12].GetStat() == False):
            print("X     ",end = "")
        else:
            print(AllCards[i+12].GetDesc(),"   ",end= "")
    print("")
    print("")

#Function that sets up the graphic part medium difficulty
def Medium(AllCards):
    print("      1     2     3     4     5     6     7     8     9     10")
    print("1     ",end = "")
    for i in range(10):
        if(AllCards[i].GetStat() == False):
            print("X     ",end = "")
        else:
            print(AllCards[i].GetDesc(),"   ",end= "")
    print("")
    print("")
    print("2     ",end = "")
    for i in range(10):
        if(AllCards[i+10].GetStat() == False):
            print("X     ",end = "")
        else:
            print(AllCards[i+10].GetDesc(),"   ",end= "")
    print("")
    print("")
    print("3     ",end = "")
    for i in range(10):
        if(AllCards[i+20].GetStat() == False):
            print("X     ",end = "")
        else:
            print(AllCards[i+20].GetDesc(),"   ",end= "")
    print("")
    print("")
    print("4     ",end = "")
    for i in range(10):
        if(AllCards[i+30].GetStat() == False):
            print("X     ",end = "")
        else:
            print(AllCards[i+30].GetDesc(),"   ",end= "")
    print("")
    print("")

#Function that sets up the graphic part hard difficulty
def Hard(AllCards):
    print("      1     2     3     4     5     6     7     8     9     10    11    12    13")
    print("1     ",end = "")
    for i in range(13):
        if(AllCards[i].GetStat() == False):
            print("X     ",end = "")
        else:
            print(AllCards[i].GetDesc(),"   ",end= "")
    print("")
    print("")
    print("2     ",end = "")
    for i in range(13):
        if(AllCards[i+13].GetStat() == False):
            print("X     ",end = "")
        else:
            print(AllCards[i+13].GetDesc(),"   ",end= "")
    print("")
    print("")
    print("3     ",end = "")
    for i in range(13):
        if(AllCards[i+26].GetStat() == False):
            print("X     ",end = "")
        else:
            print(AllCards[i+26].GetDesc(),"   ",end= "")
    print("")
    print("")
    print("4     ",end = "")
    for i in range(13):
        if(AllCards[i+39].GetStat() == False):
            print("X     ",end = "")
        else:
            print(AllCards[i+39].GetDesc(),"   ",end= "")
    print("")
    print("")

#Function called for the first card that player picks(Checks if card is already open and if it's a new one it is inserted in an array used to select only open cards)
def FirstCard(AllCards,Player,Level,CardsOpen):
    flag = False
    y = input("Παίκτη " + str(Player) + ": Δώσε γραμμή και στήλη πρώτης κάρτας (πχ 1 10):")
    lenh = len(y)
    flags = False
    #Checking if card is entered correctly and if it's not yet opened(Returns False on fail)
    for i in range (lenh):
        if(y[i] != " "):
            if(flag == False):
                if(i+1>lenh):
                    return False
                if(y[i+1]!=" "):
                    return False
                num1 = int(y[i])
                if(num1>4 or num1<1):
                    print("Λάθος στοιχεία επιλογής κάρτας")
                    return False
                flag = True
                Cline1 = num1
            else:
                num1 = int(y[i])
                if(Level == 1):
                    if(num1 == 1 and i+1 == lenh):
                        Crow1 = 1
                    elif(num1 <=4 and i+1 == lenh):
                        Crow1 = num1
                    else:
                        print("Λάθος στοιχεία επιλογής κάρτας")
                        return False
                elif(Level == 2):
                    if(i+2==lenh and num1 == 1 and y[i+1] != " "):
                        num2 = int(y[i+1])
                        if(num2 == 0):
                            Crow1 = 10
                            flags = True
                        else:
                            print("Λάθος στοιχεία επιλογής κάρτας")
                            return False
                    elif(num1 >= 1 and num1 <= 9 and (i+1) == lenh):
                        Crow1 = num1
                    elif(flags == False):
                        print("Λάθος στοιχεία επιλογής κάρτας")
                        return False
                elif(Level == 3):
                    if(i+2 == lenh and num1 == 1 and y[i+1] != " "):
                        num2 = int(y[i+1])
                        if(num2 < 4 and num2 >= 0):
                            Crow1 = 10 + num2
                            flags = True
                        else:
                            print("Λάθος στοιχεία επιλογής κάρτας")
                            return False 
                    elif(num1 >= 1 and num1 <= 9 and (i+1) == lenh and flags == False):
                            Crow1 = num1
                    elif(flags == False):
                        print("Λάθος στοιχεία επιλογής κάρτας")
                        return False
    #Cards are inserted into array to compare them later
    if(Level == 1 and AllCards[(Cline1-1)*4 + Crow1-1].GetStat() == False):
        AllCards[(Cline1-1)*4 + Crow1-1].SetStat(True)
        CardsOpen.append((Cline1-1)*4 + Crow1-1)
        return True
    elif(Level == 2 and AllCards[(Cline1-1)*10 + Crow1-1].GetStat() == False):
        AllCards[(Cline1-1)*10 + Crow1-1].SetStat(True)
        CardsOpen.append((Cline1-1)*10 + Crow1-1)
        return True
    elif(Level == 3 and AllCards[(Cline1-1)*13 + Crow1-1].GetStat() == False):
        AllCards[(Cline1-1)*13 + Crow1-1].SetStat(True)
        CardsOpen.append((Cline1-1)*13 + Crow1-1)
        return True
    else:
        print("Η κάρτα είναι ήδη ανοικτή, δοκιμάστε ξανά")
        return False

#Function called for the second card that player picks(Checks if card is already open and if it's a new one it is inserted in an array used to select only open cards)
def SecondCard(AllCards,Player,Level,CardsOpen):
    flag = False
    y = input("Παίκτη " + str(Player) + ": Δώσε γραμμή και στήλη δεύτερης κάρτας (πχ 1 10):")
    lenh = len(y)
    flags = False
    #Checking if card is entered correctly and if it's not yet opened(Returns True on success)
    for i in range (lenh):
        if(y[i] != " "):
            if(flag == False):
                if(i+1>lenh):
                    return False
                if(y[i+1]!=" "):
                    return False
                num1 = int(y[i])
                if(num1>4 or num1<1):
                    print("Λάθος στοιχεία επιλογής κάρτας")
                    return False
                flag = True
                Cline1 = num1
            else:
                num1 = int(y[i])
                if(Level == 1):
                    if(num1 == 1 and i+1 == lenh):
                        Crow1 = 1
                    elif(num1 <=4 and i+1 == lenh):
                        Crow1 = num1
                    else:
                        print("Λάθος στοιχεία επιλογής κάρτας")
                        return False
                elif(Level == 2):
                    if(i+2==lenh and num1 == 1 and y[i+1] != " "):
                        num2 = int(y[i+1])
                        if(num2 == 0):
                            Crow1 = 10
                            flags = True
                        else:
                            print("Λάθος στοιχεία επιλογής κάρτας")
                            return False
                    elif(num1 >= 1 and num1 <= 9 and (i+1) == lenh):
                        Crow1 = num1
                    elif(flags == False):
                        print("Λάθος στοιχεία επιλογής κάρτας")
                        return False
                elif(Level == 3):
                    if(i+2 == lenh and num1 == 1 and y[i+1] != " "):
                        num2 = int(y[i+1])
                        if(num2 < 4 and num2 >= 0):
                            Crow1 = 10 + num2
                            flags = True
                    elif(num1 >= 1 and num1 <= 9 and (i+1) == lenh and flags == False):
                        Crow1 = num1
                    elif(flags == False):
                        print("Λάθος στοιχεία επιλογής κάρτας")
                        return False
    #Cards are inserted into array to compare them later
    if(Level == 1 and AllCards[(Cline1-1)*4 + Crow1-1].GetStat() == False):
        AllCards[(Cline1-1)*4 + Crow1-1].SetStat(True)
        CardsOpen.append((Cline1-1)*4 + Crow1-1)
        return True
    elif(Level == 2 and AllCards[(Cline1-1)*10 + Crow1-1].GetStat() == False):
        AllCards[(Cline1-1)*10 + Crow1-1].SetStat(True)
        CardsOpen.append((Cline1-1)*10 + Crow1-1)
        return True
    elif(Level == 3 and AllCards[(Cline1-1)*13 + Crow1-1].GetStat() == False):
        AllCards[(Cline1-1)*13 + Crow1-1].SetStat(True)
        CardsOpen.append((Cline1-1)*13 + Crow1-1)
        return True
    else:
        print("Η κάρτα είναι ήδη ανοικτή, δοκιμάστε ξανά")
        return False

#Function called on every Turn so that each player can play
def Turn(AllCards,Player,Level,CardsOpen):
    check = FirstCard(AllCards,Player,Level,CardsOpen)
    #If first card is correct we can continue
    if(check == True):
        if(Level == 1):
            Easy(AllCards)
        elif(Level == 2):
            Medium(AllCards)
        else:
            Hard(AllCards)
        check2 = SecondCard(AllCards,Player,Level,CardsOpen)
        #If second card is correct we can continue
        while(check2 == False):
            check2 = SecondCard(AllCards,Player,Level,CardsOpen)
        if(Level == 1):
            Easy(AllCards)
        elif(Level == 2):
            Medium(AllCards)
        else:
            Hard(AllCards)
        return True
    else:
        return False

#Function that checks if game is over(If there is no open card returns True since game is over,otherwise returns False)
def CheckGame(AllCards):
    x = len(AllCards)
    for i in range (x):
        if(AllCards[i].GetStat() == False):
            return False
    return True

#Function that prints the player that won the game(If 2 players have the same points it prints draw)
def GameWinner(PlayerPoints):
    max = 0
    maxs = -1
    flag = False
    for i in range (len(PlayerPoints)):
        if(max < PlayerPoints[i]):
            max = PlayerPoints[i]
            maxs = i
            flag = False
        elif(max == PlayerPoints[i]):
            flag = True
    if(flag == False):
        print("Νίκησε ο παίχτης " + str(maxs+1))
    else:
        print("Υπάρχει ισοβαθμία μεταξύ παιχτών")

#Main function that calls all functions and is terminated when game is over
def main():
    #Checking player and level number to be eligible
    print("Καλώς ήρθατε στο Matching Game")
    flag = False
    while (flag == False):
        x = input("Δώστε αριθμό παιχτών:")
        x = int(x)
        if (x >= 2):
            flag = True
        else:
            print("Δώστε έγκυρο αριθμό παιχτών (τουλάχιστον 2)")
    flag2=False
    while (flag2 == False):
        y = input("Δώστε επίπεδο δυσκολίας Εύκολο (1), Μέτριο (2), Δύσκολο (3) :")
        y = int(y)
        if ((y == 1) or (y == 2) or (y == 3)):
            flag2 = True
        else:
            print("Δώστε έγκυρο επίπεδο δυσκολίας")
    #Initializiting arrays and using if condition to start game according to level
    gamefinished = False
    PlayerPoints = [0] * x
    CardsOpen = []
    Player = 1
    if(y == 1):
        #Showing cards and then dissapearing them
        PlayerTurn = False
        AllCards = []
        CardSet(16,AllCards)
        random.shuffle(AllCards)
        SetStateAll(True,AllCards,16)
        Easy(AllCards)
        SetStateAll(False,AllCards,16)
        Easy(AllCards)
        #While game is still running
        while(gamefinished == False):
            check = False
            while (check == False):
                check = Turn(AllCards,Player,1,CardsOpen)
            desc1 = AllCards[CardsOpen[0]].GetDesc()
            desc2 = AllCards[CardsOpen[1]].GetDesc()
            #If player found 2 same cards takes points otherwise everything closes again
            if(desc1[0] == desc2[0]):
                PlayerPoints[Player-1] += AllCards[CardsOpen[0]].GetValue()
                print("Επιτυχές ταίριασμα +"+ str(AllCards[CardsOpen[0]].GetValue()) +" πόντοι! Παίκτη " + str(Player) + " έχεις συνολικά " + str(PlayerPoints[Player-1]) +" πόντους.")
                #Special cards
                if(desc1[0] == "J"):
                    PlayerTurn = True
                elif(desc1[0] == "K"):
                    if(Player+1 > x):
                        Player = 1
                    else:
                        Player += 1
                CardsOpen.clear()
            else:
                AllCards[CardsOpen[0]].SetStat(False)
                AllCards[CardsOpen[1]].SetStat(False)
                CardsOpen.clear()
            if (Player+1 > x and PlayerTurn == False):
                Player = 1
            elif(PlayerTurn == False):
                Player += 1
            PlayerTurn = False
            gamefinished = CheckGame(AllCards)
        GameWinner(PlayerPoints)
    elif(y == 2):
        #Showing cards and then dissapearing them
        PlayerTurn = False
        AllCards = [] 
        CardSet(40,AllCards)
        random.shuffle(AllCards)
        SetStateAll(True,AllCards,40)
        Medium(AllCards)
        SetStateAll(False,AllCards,40)
        Medium(AllCards)
        #While game is still running
        while(gamefinished == False):
            check = False
            while (check == False):
                check = Turn(AllCards,Player,2,CardsOpen)
            desc1 = AllCards[CardsOpen[0]].GetDesc()
            desc2 = AllCards[CardsOpen[1]].GetDesc()
            #If player found 2 same cards takes points otherwise everything closes again
            if(desc1[0] == desc2[0]):
                PlayerPoints[Player-1] += AllCards[CardsOpen[0]].GetValue()
                print("Επιτυχές ταίριασμα +"+ str(AllCards[CardsOpen[0]].GetValue()) +" πόντοι! Παίκτη " + str(Player) + " έχεις συνολικά " + str(PlayerPoints[Player-1]) +" πόντους.")
                #Special cards
                if(desc1[0] == "J"):
                    PlayerTurn = True
                elif(desc1[0] == "K"):
                    if(Player+1 > x):
                        Player = 1
                    else:
                        Player += 1
                CardsOpen.clear()
            else:
                AllCards[CardsOpen[0]].SetStat(False)
                AllCards[CardsOpen[1]].SetStat(False)
                CardsOpen.clear()
            if (Player+1 > x and PlayerTurn == False):
                Player = 1
            elif(PlayerTurn == False):
                Player += 1
            PlayerTurn = False
            gamefinished = CheckGame(AllCards)
        GameWinner(PlayerPoints)
    else:
        #Showing cards and then dissapearing them
        PlayerTurn = False
        AllCards = []
        CardSet(52,AllCards)
        random.shuffle(AllCards)
        SetStateAll(True,AllCards,52)
        Hard(AllCards)
        SetStateAll(False,AllCards,52)
        Hard(AllCards)
        #While game is still running
        while(gamefinished == False):
            check = False
            while (check == False):
                check = Turn(AllCards,Player,3,CardsOpen)
            desc1 = AllCards[CardsOpen[0]].GetDesc()
            desc2 = AllCards[CardsOpen[1]].GetDesc()
            #If player found 2 same cards takes points otherwise everything closes again
            if(desc1[0] == desc2[0]):
                PlayerPoints[Player-1] += AllCards[CardsOpen[0]].GetValue()
                print("Επιτυχές ταίριασμα +"+ str(AllCards[CardsOpen[0]].GetValue()) +" πόντοι! Παίκτη " + str(Player) + " έχεις συνολικά " + str(PlayerPoints[Player-1]) +" πόντους.")
                #Special cards
                if(desc1[0] == "J"):
                    PlayerTurn = True
                elif(desc1[0] == "K"):
                    if(Player+1 > x):
                        Player = 1
                    else:
                        Player += 1
                CardsOpen.clear()
            else:
                AllCards[CardsOpen[0]].SetStat(False)
                AllCards[CardsOpen[1]].SetStat(False)
                CardsOpen.clear()
            if (Player+1 > x and PlayerTurn == False):
                Player = 1
            elif(PlayerTurn == False):
                Player += 1
            PlayerTurn = False
            gamefinished = CheckGame(AllCards)
        GameWinner(PlayerPoints)

#Class that creates cards as suggested in the instructions
class Card:
    #Constructor
    def __init__(self,symbol,value,desc,status):
        self._symbol = symbol
        if(symbol == "♥"):
            self._color = "Hearts"
        if(symbol == "♦"):
            self._color = "Diamonds"
        if(symbol == "♠"):
            self._color = "Clubs"
        if(symbol == "♣"):
            self._color = "Spades"
        self._value = value
        self._desc = desc
        self._status = status
    #Setters-Getters
    def GetSymb(self):
        return self._symbol
    def GetDesc(self):
        return self._desc
    def GetValue(self):
        return self._value
    def GetStat(self):
        return self._status
    def GetColor(self):
        return self._color
    def SetStat(self,status):
        self._status = status

main()

