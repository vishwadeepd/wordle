import sys
import random
##from termcolor import colored
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
    

wordle_set=["stand",
            "stone",
            "elite",
            "eight",
            "prove",
            "dizzy",
            "money",
            "metro",
            "heart",
            "reach",
            "after",
            "music",
            "grove",
            "loose",
            "trade",
            "hello",
            ""]


#print(len(wordle_set))

#wordOfThday=sys.argv[1]

wordOfThday=wordle_set[random.randrange(len(wordle_set))]



def wordleEngine(wordOfThday,guessWords,val):
    res = []
    anticipatedWord=[]
    wordOfThdayList=list(wordOfThday)
    #print(wordOfThdayList)
    guessWordsList=list(val)
    #print(guessWordsList)
    testList=[]
    idx=0
      
    for i in guessWordsList:
        if i == wordOfThdayList[idx]:
            res.append(idx)
            #print("Matched with index ",i)
            #mtext = colored(i.upper(), 'green', attrs=['reverse', 'blink'])
            mtext = style.GREEN + i.upper()
            testList.append(mtext)
        elif i in wordOfThdayList:
            #wtext = colored(i.upper(), 'blue', attrs=['reverse', 'blink'])
            wtext = style.BLUE + i.upper()
            testList.append(wtext)
            #print("present in  list ",i)
        else:
            #btext = colored(i.upper(), 'grey', attrs=['reverse', 'blink'])
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
    while(count<6):
        val = input(style.WHITE+"->")
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
    print(style.WHITE+"Word of the day was: ",wordOfThday.upper())
    
if __name__ == "__main__":    
    userInteractor(wordOfThday)
    

