import fileinput
import random
import time
startTime = time.time();

def search_word(file_path, word):
  with open(file_path, 'r') as f:
    content = f.read()
    if word in content:
       return True
    else:
       return False
    
    
black = []
green = [""] * 5
yellow = []

def checkBlack(s):
    for i in range(5):
        for j in range(len(black)):
            if green[i] == "" and s[i] == black[j]:
                return False
    return True

def checkGreen(s):
    for i in range(5):
        if green[i] != "" and s[i] != green[i]:
            return False
    return True

def checkYellow(s):
    for i in range(5):
        for j in range(len(yellow)):
            tempChar, tempNum = yellow[j].split()
            if s[int(tempNum)] == tempChar or s.find(tempChar) == -1:
                return False
    return True
    

ansList = []
for word in fileinput.input(files="Wordleanswers.txt"):
    ansList.append(word);
tempAnsList = []
for i in range(1):
    tempAnsList.append(ansList[random.randint(0, len(ansList))]);
wordList = []
for word in fileinput.input(files="Wordlewords.txt"):
    wordList.append(word);
    

for start in range(4):
    for first in range(26):
        for second in range(26):
            guess = "   "[0 : start] + chr(97+first) + chr(97+second) + "   "[start : 3]
            for ans in tempAnsList:
                
                
                black = []
                green = [""] * 5
                yellow = []
                tempList = wordList.copy()
                
                for letter in range(5):
                    if (guess[letter] != " "):
                        if guess[letter] == ans[letter]:
                            green[letter] = guess[letter]
                        elif ans.find(guess[letter]) == -1:
                            if not guess[letter] in black:
                                black.append(guess[letter])
                        else:
                            yellow.append(guess[letter] + " " + str(letter))
                
                count = 0
                for i in range(len(wordList)):
                    if checkBlack(tempList[i]) and checkGreen(tempList[i]) and checkYellow(tempList[i]):
                        count += 1
                print(ans + "   " + guess + ": ", end = "")
                print(count/len(wordList))
                
endTime = time.time()
print("Time: " + str(endTime-startTime))
                
                
# first create a test guess with the 2-letter pair being tested
# input it as a guess with the answer, see whether any letter comes up as black, green, or yellow
# use the feedback to filter out all the words from wordList that do not follow the feedback
# find the ratio of after to before (lower ratio means better guess)
# repeat with every answer
# record data in a 2d matrix - average data every time compilation is done to make sure no memory crash

