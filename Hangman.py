from random import choice
import time
with open("Words.txt") as f:
    Words = f.readlines()

The_Dict = {}
for i in range(len(Words)):
    The_Dict.update({Words[i].split(".")[0]:Words[i].split(".")[1]})

    
# Extracting Word from the dictionary to a list
Word_List = []
for items in The_Dict.keys():
    Word_List.append(items)

# Function for Extracting a random word from the Given List
def RanWord(List):
    return choice(List)

# Function for analysing the user input in the word        
def Analysis(Word ,UserInput):
    No_Of_Occurence = Word.count(UserInput)
    if No_Of_Occurence == 1:
        return [Word.index(UserInput)]
    
    elif No_Of_Occurence >= 2:
        O1 = Word.index(UserInput)
        O2 = Word.rindex(UserInput)
        return [O1,O2] 

    elif No_Of_Occurence == 0:
        return []
    
#Function for Filtering the word for More then 2 occurence of a given input    
def Filter(Word, UserInput, IndexList):
    No_Of_Occurence = Word.count(UserInput)
    
    if No_Of_Occurence>len(IndexList):
        
        while No_Of_Occurence >= len(IndexList):
            Sliced_Word = Word[IndexList[-2]+1:IndexList[-1]]
                
            a = Sliced_Word.find(UserInput)
            b = Sliced_Word.rfind(UserInput)
        
            if a != None and b == None:
                IndexList.append(a + len(Word[:IndexList[-2]+1]))
            elif a != None and b != None:
                IndexList.append(a + len(Word[:IndexList[-2]+1]))
                IndexList.append(b + len(Word[:IndexList[-1]-1]))
                Filter(Word, UserInput, IndexList)

        return IndexList.pop(len(IndexList)-1)
    else:
        return IndexList

# Function for Replacing the dash Dashed List with the User input
def Dash_Replace(DashList, IndexList, UserInput):
    if len(IndexList) == 0:
            DashList = DashList    
    else:
        for Index in IndexList:
            DashList.pop(Index)
            DashList.insert(Index, UserInput)
    return DashList

# Function for Replacing the word with New word with removed alphabets
def Word_Replace(New_Word, UserInput):
        
    return New_Word.replace(UserInput, "")

def Main_Game():
    # Generating the Random Word
    Word = RanWord(Word_List)   
    New_Word = Word 

    # Generating the DashList for Word
    DashList = []
    for i in range(len(Word)):
        DashList.append("_ ")

    # Generating the Dashlist for Hangman
    H_Dashlist = ["_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ ","_ "]
    HangManList = ["Y","O", "U", "H", "A", "N", "G", "M", "A", "N"]
    HangmanEnd = []
    Already_Guessed = []
    i = 0
    while i<11:
        
        # print("\nTo Quit Enter 'QUIT'\n".center(100))
        print(f'ChancesLeft:{10-i}\n'.center(100))
        if (10-i) ==1:
            print("Last Chance!!\n".center(100)) 

        # Making the Dashed String for Hangman
        
        H_Dash_Str = ""
        for j in range(len(H_Dashlist)):
            H_Dash_Str = H_Dash_Str + H_Dashlist[j]
        print(H_Dash_Str.center(100),"\n")

        # Making a Dashed String for Word
        
        Dash_Str = "".center(42)
        for k in range(len(DashList)):
            Dash_Str = Dash_Str + DashList[k]
        print(Dash_Str,"\n")
        print(f"HINT:{The_Dict.get(Word)}".center(100),)

        # Setting the Loosing game Settings
        
        if H_Dash_Str == 'YOUHANGMAN':
                print(f"You Loose the Game The Word Was:{Word}\n".center(100))
                break
        else:
            try:
                if New_Word == "":
                    print("******************You Won the Game!*******************\n".center(100))
                    print("********************************************************************************************************************************".center(20))
                    time.sleep(2)
                    break
                else:
                    # Taking the User's Input
                    UserInput = input("Enter Your Guess: \n".center(100)).capitalize()
                    
                    if UserInput in Already_Guessed:
                        print(f"You Already guessed {UserInput}".center(100))
                    else:
                        if UserInput in New_Word:
                            # Generating the Index List
                            IndexList = Analysis(Word, UserInput)
                            # print(IndexList, 'From Program')       #   ERROR CHECKING HERE
                            Filter(Word, UserInput, IndexList)
                            # print(IndexList, 'After filter')      #  ERROR CHECKING

                            # Generating the DashList with Replaced word
                            DashList = Dash_Replace(DashList, IndexList, UserInput)
                            
                            # print(DashList)            # CHECKING FOR ERROR!

                            # Genrating the New Word
                            New_Word = Word_Replace(New_Word, UserInput)
                            # print(New_Word)
                            # print(Word)                 # SETTED HERE FOR CHECKING FOR AN ERROR.
                            print("Your Guess was True!".center(100))
                            Already_Guessed.append(UserInput)

                        elif UserInput not in New_Word:
                            print("Your Guess was Wrong!\n".center(100))
                            H_Dashlist.pop(i)
                            H_Dashlist.insert(i, HangManList[i])
                            HangmanEnd.append(i)
                            i += 1        
            except Exception as e:
                print("You Just Entered Something Wrong raising error", e,"Please Try Again!")            
        
        print("****************************************************************************************************".center(30))
        time.sleep(1)
    YourChoise = input("To Play Again Enter 'Y' else 'N':".center(60)).capitalize()
    if YourChoise == "Y":
        Main_Game()
    else:
        print("*********************************Thanks for playing!**************************".center(100))
        time.sleep(3)
        quit()
            
Main_Game()
