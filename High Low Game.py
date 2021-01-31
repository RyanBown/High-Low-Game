import random
import time

def getRandomNumber(low, high):
    return random.randrange(low, high)


def getUserInput(message, expectedInput = ['Y', 'N']):
    user_input = input(message+ ' \n')
    if user_input.upper() in expectedInput:
        return user_input.upper()
    else:
        print('That was not expected, please type', expectedInput)
        getUserInput(message, expectedInput)


def printList(scrollList, t = 1.25):
    for item in scrollList:
        print(item)
        time.sleep(t)



def getGameStarted(difficulty, diffList, diffPrintList ):
    settingMessage = "What diffuculty do you choose?"
    userDiffuculty = getUserInput( settingMessage, diffList)

    pickedSetting = difficulty[userDiffuculty]
    continuePlaying = True
    playMessage = "Do you want to play again? [Y]/[N]"
    
    playGame(pickedSetting)
    while continuePlaying:
        resp = getUserInput(playMessage)
        if resp == 'N':
            continuePlaying = False
        else:
            printList(diffPrintList, 0.5)
            userDiffuculty = getUserInput( settingMessage, diffList)
            pickedSetting = difficulty[userDiffuculty]
            playGame(pickedSetting)

def playGame(settings):    
    guessAmt = settings[0]
    startRange = settings[1]
    endRange = settings[2]
    guessedRight = True
    rangeMessage = "Your range: " + str(startRange) + "-" + str(endRange) + '\n'
    guessMessage = "Make your guess, next number will be [E]qual, [H]igher or [L]ower than"
    hlInput = ['H', 'L', 'E']
    initNum = getRandomNumber(startRange, endRange)
    guessedWrong = "You've guessed wrong and it should have been"

    while guessAmt > 0 and guessedRight:
        printMessage = rangeMessage + guessMessage +  str(initNum)
        resp = getUserInput(printMessage, hlInput)
        genNum = getRandomNumber(startRange, endRange)
        if resp in ['H','E'] and initNum > genNum:
            guessedRight = 0
            print(guessedWrong, "[L]ower, the number was", str(genNum))
            break
        if resp in ['L','E'] and initNum < genNum:
            guessedRight = 0
            print(guessedWrong, "[H]igher , the number was",str(genNum))
            break
        if resp in ['H','L'] and initNum == genNum:
            guessedRight = 0
            print(guessedWrong[:20], ",the number was equal to",str(genNum))
            break
        print("You've guessed right!")
        initNum = genNum
        guessAmt -= 1

    if guessedRight:
        print("You've won!")


def printRules(difficulty, diffDef):
    lineOne = "This game will generate a number and you can guess if the next number is Higher or Lower."
    lineTwo =  "If you guess correctly, you can guess again against that new number"
    lineThree = "When the game is over, you can start another game or end it."
    lines = [lineOne,lineTwo,lineThree]
    print()
    printList(lines)
    print()
    modeList = []
    for mode,s in difficulty.items():
        modeList.append("For " + diffDef[mode] + " [" + mode + "], you have to make " + str(s[0]) + " consecutive guesses for a random number between " + str(s[1]) + " and " + str(s[2]) )
    printList(modeList)
    print()
    

##  Dictionary 'Mode': [Number of Guess, Range Start, Range End] 
difficulty = { 'E': [3, 1, 100],
                'M': [5, 1, 50],
               'H': [7, 1, 20],
               'V': [9, 1, 10]
               }

diffDef = {'E': 'Easy',
                 'M':'Medium',
                 'H':'Hard',
                 'V':'Very Hard'
                 }


introMessage = 'Do you know how the High Low game works?[Y/N]'


if getUserInput(introMessage) == 'N':
    printRules(difficulty, diffDef)
else:
    print("Okay, hotshot let's do this!")

diffList = []
diffPrintList = []
for key, value in diffDef.items():
    diffPrintList.append(value + ' [' + key +']')
    print(value, '[' + key +']')
    time.sleep(.5)
    diffList.append(key)

print()
getGameStarted(difficulty, diffList, diffPrintList )



##print(difficultyDef)
