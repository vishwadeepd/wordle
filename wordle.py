import sys
import random
#from termcolor import colored
import pandas as pd
import os

# System call
os.system("")

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    

wordle_set=["stand", "stone", "elite", "eight", "prove", "dizzy", "money", "metro", "heart", "reach", "after", "music", "grove", "loose", "trade", "hello", 
            "abuse", "adult", "agent", "anger", "apple", "award", "basis", "beach", "birth", "block", "blood", "board", "brain", "bread", "break", "brown", 
            "buyer", "cause", "chain", "chair", "chest", "chief", "child", "claim", "class", "clock", "coach", "coast", "court", "cover", "cream", "crime", 
            "cross", "crowd", "crown", "cycle", "dance", "death", "depth", "doubt", "draft", "peace", "peter", "phase", "phone", "piece", "pilot", "pitch", 
            "place", "plane", "plant", "plate", "point", "pound", "power", "press", "price", "pride", "prize", "proof", "queen", "radio", "range", "ratio", 
            "reply", "right", "river", "round", "route", "rugby", "scale", "scene", "scope", "score", "sense", "shape", "share", "sheep", "sheet", "shift", 
            "shirt", "shock", "sight", "skill", "sleep", "smile", "smith", "smoke", "sound", "south", "space", "speed", "spite", "sport", "squad", "staff", 
            "stage", "start", "state", "steam", "steel", "stock", "stone", "store", "study", "stuff", "style", "sugar", "table", "taste", "terry", "theme", 
            "thing", "title", "total", "touch", "tower", "track", "trade", "train", "trend", "trial", "trust", "truth", "uncle", "union", "unity", "value", 
            "video", "visit", "voice", "waste", "watch", "water", "while", "white", "whole", "woman", "world", "youth","panic","drive","where"]


#print(len(wordle_set))

#wordOfThday=sys.argv[1]

wordOfThday=wordle_set[random.randrange(len(wordle_set))]



def wordleEngine(wordOfThday,guessWords,val):
    res = []
    anticipatedWord=[]
    wordOfThdayList=list(wordOfThday.lower())
    #print(wordOfThdayList)
    guessWordsList=list(val.lower())
    #print(guessWordsList)
    testList=[]
    idx=0
      
    for i in guessWordsList:
        if i == wordOfThdayList[idx]:
            res.append(idx)
            mtext = style.GREEN + i.upper()
            testList.append(mtext)
        elif i in wordOfThdayList:
            wtext = style.BLUE + i.upper()
            testList.append(wtext)
        else:
            btext = style.RED + i.upper()
            testList.append(btext)
        idx = idx + 1
    #print("testList",testList)          
    print(''.join(testList))   
    return ''.join(testList)         

            
        
     


def userInteractor(wordOfThday):
    count=0
    guessWord=''
    guessWorldList=[]
    print(style.WHITE+"********** WORDLE CONSOLE **********")
    print(style.BLUE+"Blue -> Word exist but wrong index\n"+style.RED+"Red -> Word does not exist\n"+style.GREEN+"Green -> Word in the right index")
    print("* Please only enter a 5 letter valid word * \n")
    while(count<6):
        val = input(style.WHITE+"->")
        if len(val)==5 and val.lower() in wordle_set :
            temp=wordleEngine(wordOfThday,guessWord,val)
            #df = pd.DataFrame (list(temp), columns = ['Letters'])
            #print(df)
            guessWorldList.append(val.upper())
            print(style.MAGENTA+"Attempts",guessWorldList)
            if val == wordOfThday:
                print(style.CYAN+" ****** WINNER! You guessed it right. ****** ")
                break
            else:
                print("You still have chances left {}".format(6-count -1))
            count +=1
        else:
            if len(val)!=5:
                print("Please input a 5 letter word only or word ")
            else:
                print("Word not in wordle dictionary, please try another word ")
    print(style.WHITE+"Word of the day was: ",wordOfThday.upper())
    
if __name__ == "__main__":    
    userInteractor(wordOfThday)
    

