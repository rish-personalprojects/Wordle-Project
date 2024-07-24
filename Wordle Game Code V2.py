import fileinput

def search_word(file_path, word):
  with open(file_path, 'r') as f:
    content = f.read()
    if word in content:
       return True
    else:
       return False

ans = "hello"
ylist = []
glist = []
blist = []

roundcount = 0;
while(roundcount < 6):
    guess = input()
    if len(guess) != 5:
        print("Make sure your guess is 5 letters")
        continue
    elif search_word("Wordlewords.txt", guess) == False:
        print("Make sure your guess is a valid word")
        continue
    else:
        roundcount += 1
        for j in range(5):
            if guess[j] == ans[j]:
                print('g', end = "")
                if not guess[j] in glist:
                    glist.append(guess[j])
            elif ans.find(guess[j]) == -1:
                print('b', end = "")
                if not guess[j] in blist:
                    blist.append(guess[j])
            else:
                print('y', end = "")
                if not guess[j] in ylist:
                    ylist.append(guess[j])
                for k in range(len(ylist)):
                    if ylist[k] in glist:
                        glist.remove(ylist[k])
        print()
        print("total green: " + ','.join(glist))
        print("total yellow: " + ','.join(ylist))
        print("total black: " + ','.join(blist))
        if guess == ans:
            print("win in " + str(roundcount) + " guesses!")
            exit()
        
print("lose :(")
    

