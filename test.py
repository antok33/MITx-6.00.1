import random
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

SCRABBLE_LETTER_VALUES = {
'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}


def loadWords():

    print "Loading word list from file..."

    inFile = open('words.txt', 'r')

    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def displayHand(hand):

    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,
    print


def getWordScore(word, n):

    score = 0
    length = len(word)

    if length > 0:
        for char in word:
            score = score + SCRABBLE_LETTER_VALUES[char]
        score = score * length

    if length == n:
        score = score + 50

    return score



def updateHand(hand, word):
    test = {}
    for char in hand:
        test[char] = hand[char]
    for char in word:
        if char in test and test[char] > 0:
            test[char] = test[char] - 1
        else:
            return hand
    return test
# print updateHand({'a': 1, 'p': 2, 'l': 1, 'e': 1}, 'apple')



def getFrequencyDict(sequence):

    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def isValidWord(word, hand, wordlist):
    test_hand = getFrequencyDict(word)
    if word in wordlist:
        for char in word:
            if char in hand:
                for key in test_hand:
                    if key in hand:
                        if test_hand[key] > hand[key]:
                            return False
            else:
                return False
        return True
    else:
        return False

# isValidWord('apple', {'a': 1, 'p': 2, 'l': 1, 'e': 1},['apple'])

def calculateHandlen(hand):
    handlen = 0
    for char in hand:
        handlen = handlen + hand[char]
    return handlen


def playHand(hand, wordlist, n, score=0):

    displayHand(hand)
    ans = raw_input('Enter word, or a "." to indicate that you are finished: ')

    if ans != '.':
        if isValidWord(ans, hand, wordlist):
            temp_score = getWordScore(ans, n)
            score = score + temp_score
            print ans, "earned", temp_score, "points. Total:", score, 'points'
            hand = updateHand(hand, ans)
            if calculateHandlen(hand) > 0:
                playHand(hand, wordlist, n, score)
            else:
                print ''
                print 'Run out of letters. Total score:', score, 'points.'
        else:
            print 'Invalid word, please try again.'
            playHand(hand, wordlist, n, score)
    else:
        print  'Goodbye! Total score:' ,score ,'points.'

#wordList = loadWords()
#playHand({'a': 2, 'p': 1, 'r': 1, 'e': 2, 't': 1},wordList, 7)

HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
    'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def dealHand(n):

    hand={}
    numVowels = n / 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

def playGame(wordlist, hand={}, already_Play=False):
    choice = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")

    if choice == 'n':
        hand = dealHand(HAND_SIZE)
        playHand(hand, wordlist,HAND_SIZE)
        playGame(wordlist, hand, already_Play=True)


    elif choice == 'r':
        if already_Play == True:
            playHand(hand, wordlist,HAND_SIZE)
            playGame(wordlist,hand,already_Play)
        else:
            print "You have not played a hand yet. Please play a new hand first!"
            playGame(wordlist)

    elif choice == 'e':
        pass
    else:
        print "Invalid input"
        playGame(wordlist,hand,already_Play)


playGame(loadWords())


