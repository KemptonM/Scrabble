# NAME: KEMPTON MAILLETT
# ASSIGNMENT: PROJECT 1
# COLLABORATION: Elyse Callahan, debugging
import random
from operator import itemgetter

def validate(hand, word):   # boolean function, return true if word is valid
    letterCount = 0         #                   return false if invalid
    tempHand = hand.copy()
    for x in word:
        if x.isalpha() == True:
            letterCount += 1
            if x.upper() not in tempHand:   # if user does not have letter
                print(x.upper(), "is not in your hand.")
                return False                    # return False
            tempHand.remove(x.upper())
    if letterCount < 1:                     # if there are no letters
        print("You've entered no letters.")
        return False                            # return False
    elif len(word) < 3:                     # if word is too short
        print("You've entered a word less than three letters long.")
        return False                            # return False
    else:                                   # if all checks passed
        return True                             # return True
    
def score(word):            # return a score for the word passed in
    # points categories
    s1 = ('E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U') # 1 point
    s2 = ('D', 'G')                                         # 2 points
    s3 = ('B', 'C', 'M', 'P')                               # 3 points
    s4 = ('F', 'H', 'V', 'W', 'Y')                          # 4 points
    s5 = ('K')                                              # 5 points
    s8 = ('J', 'X')                                         # 8 points
    s10 = ('Q', 'Z')                                        # 10 points
    points = 0              # initialize points
    if len(word) == 7:          # if the word is seven letters long
        print("10 extra points for a 7 letter word!")
        points += 10                # 10 extra points!
    for x in word:              # give points for each letter
        if x.upper() in s1:
            points += 1
        elif x.upper() in s2:
            points += 2
        elif x.upper() in s3:
            points += 3
        elif x.upper() in s4:
            points += 4
        elif x.upper() in s5:
            points += 5
        elif x.upper() in s8:
            points += 8
        elif x.upper() in s10:
            points +=10
    print(f"+{points} points!") # print points gained for this word
    return points

def swap(hand, word):       # swap out the letters that were used
    for x in word:
        hand.remove(x.upper())
    return refill(hand)

def refill(hand):           # fill the hand back up to 7 letters
    bag = (                             # tuple of letters
    'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 
    'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 
    'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 
    'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 
    'N', 'N', 'N', 'N', 'N', 'N', 
    'R', 'R', 'R', 'R', 'R', 'R', 
    'T', 'T', 'T', 'T', 'T', 'T', 
    'L', 'L', 'L', 'L', 
    'S', 'S', 'S', 'S', 
    'U', 'U', 'U', 'U', 
    'D', 'D', 'D', 'D', 
    'G', 'G', 'G', 
    'B', 'B',
    'C', 'C', 
    'M', 'M', 
    'P', 'P', 
    'F', 'F', 
    'H', 'H', 
    'V', 'V', 
    'W', 'W', 
    'Y', 'Y', 
    'K', 'J', 'X', 'Q', 'Z')
    for i in range(7-len(hand)):        # fill hand back to 7 letters
        hand.append(random.choice(bag)) # get a random letter from bag
    return hand

def highscore(points):       # adjust highscore text file
    highscores = []
    scores = []
    try:
        f = open("highscores.txt")  # open the file for reading
    except FileNotFoundError:           # if file doesn't exist
        f = open("highscores.txt", 'w')     # create it
        for x in range(5):
            f.write("Empty: 0\n")           # add empty scores
        f.close()
        f = open("highscores.txt")  # open the file for reading
    lines = f.readlines()
    for line in lines:
        line = line.rstrip().split(': ')
        highscores.append(line)
    f.close()
    for x in highscores:
        x[1] = int(x[1])        # turn the score into an integer
        scores.append(x[1])     # put the integers into a list
    if points > int(min(scores)):                       # if user has a high score
        name = input("High score! Enter your name: ")       # ask for name
        highscores.append((name, points))                   # add to list
        print("Highscore recorded. GG!")
    highscores = sorted(highscores, key=itemgetter(1), reverse=True)    # sort highscores
    f = open("highscores.txt", 'w')         # open file for overwrite
    for x in range(5):                                  # only count the first 5
        f.write(f"{highscores[x][0]}: {highscores[x][1]}\n")    # rewrite the file
    f.close()
# is there a better way to do all of that?

def main():
    hand = refill([])                   # initialize hand
    points = 0                          # initialize points
    print("Your hand:", *hand)        
    word = input("Enter your word: ")   # initialize word
# game loop
    while validate(hand, word) == True: # for each new valid word:
        points += score(word)               # score the word
        print("Current score:", points)     # display score
        hand = swap(hand, word)             # get a new hand
        print("\nYour hand:", *hand)            # display new hand
        word = input("Enter your word: ")   # get new word
    print("\nGAME OVER.")
    print(f"Final score: {points}")
    highscore(points)                   # do the highscore thing

main()