"""
		    GNU GENERAL PUBLIC LICENSE
		       Version 2, June 1991

*******************************************************************************************************************
*   Originally Created by Ankit Chand                                                                             *
*   This Program is  a Drive Hide software which takes certain Parameters and hides/unhides a drive that you want.*
*   Any changes and issues/bugs are welcome <constructively>.                                                     *
*   Copyright (C) 2012  <Ankit Chand>                                                                             *
*******************************************************************************************************************

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

"""

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    print "------------------------------------------"
    print "Welcome to THE WORD GAME"
    print "CODED by Anki Chand"
    print "------------------------------------------"
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

#  Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    li_word=list(word)
    suma=0
    for item in li_word:
        suma=suma+SCRABBLE_LETTER_VALUES[item]
    result=suma*len(word)
    if len(word)==n:
        result=result+50
    return result
#getWordScore('waybill',7)


#
#  Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
#  Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
  
    handy=hand.copy()
    for letter in word:
        if letter in handy:
                value=handy[letter]
                value=value-1
                handy[letter]=value
                
    for item in hand:
        if handy[item]==0:
            handy.pop(item)
    return handy
            
#
#  Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    handy=hand.copy()
    Flag=False
    Flag2=False
    counter=0
    for letter in word:
  
        if letter in handy:
  
            Flag=True
            counter=counter+1
            handy[letter]=handy[letter]-1
            if handy[letter]==0:
                handy.pop(letter)
           
        else:
            Flag=False
            counter-=1
    if counter==len(word):
        Flag=True
    else:
        Flag=False

    if word in wordList:
        Flag2=True
    else:
        Flag2=False
    if Flag and Flag2:
        return True
    else:
        return False
  

#wordList = loadWords()
#print isValidWord('vial', {'v':1,'i':1,'a':2,'b':2,'s':2}, wordList)
#print isValidWord('rapture',{'a': 3, 'e': 1, 'p': 2, 'r': 1, 'u': 1, 't': 1}, wordList)
#print isValidWord('kwijibo', {'b': 1, 'i': 2, 'k': 1, 'j': 1, 'o': 1, 'w': 1},wordList)

#
#  Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
  
    suma=0
    for item in hand:
        suma=suma+hand[item]
    return suma
#print calculateHandlen({'v':1,'i':1,'a':2,'b':2,'s':2})

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    
    # Keep track of two numbers: the number of letters left in your hand and the total score
    handy=hand.copy()
    left=calculateHandlen(handy)
    score=0
    
    while left>0:
        print "Current Hand: ",
        displayHand(handy)
        user=raw_input('Enter word, or a "." to indicate that you are finished: ')
        if user==".":
            print "Goodbye!",
            print "Total score: "+str(score)
            return
        elif isValidWord(user, hand, wordList)!=True:
            print "Invalid word, please try again."
        else:
            wordScore=getWordScore(user,n)
            print '"'+user+'"'+" earned "+str(wordScore)+" points.",
            handy=updateHand(handy,user)
            left=calculateHandlen(handy)
            score=score+wordScore
            print "Total score: "+str(score)
            
    print 
    print "Run out of letters. Total score: "+str(score)+" points."     
        
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is a single period:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not a single period):
        
            # If the word is not valid:
            
                # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                # Update the hand 
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score

wordList = loadWords()
#playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
#playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)    
#playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)    
#
#  Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    userin="n"
    hand={}
    handy=hand
    while True:
        print "Menu:"
        print "1. Enter ' n ' to deal a new hand (set of letters)"
        print "2. Enter ' r ' to replay the last hand"
        print "3. Enter ' e ' to end game"
        print
        userin=raw_input("Enter your Choice n/r/e: ")
        if userin=="n":
            hand=dealHand(HAND_SIZE)
            handy=hand.copy()
            playHand(handy, wordList,HAND_SIZE)
        elif userin=="r":
            if len(hand)==0:
                print "You have not played a hand yet. Please play a new hand first!"
            else:
                #displayHand(hand)
                handy=hand.copy()
                playHand(handy, wordList,HAND_SIZE)
        elif userin=="e":
            return
        else:
            print "Invalid command."
        print


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
