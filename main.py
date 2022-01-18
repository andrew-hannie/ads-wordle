from wordle import wordle
from random import randint

'''
    
    This is just a basic main method.

'''

def main():
    print("Welcome to Wordle!\n")
    words = getWords(3) # gets a list of words to use
    for i in words:
        wordle(i) # run wordle on the values of the word list
'''
    
    Returns a list of random words that we are going to use for wordle.

'''

def getWords(value):
    wordsFile = open("py/ads-wordle/words_5_letter.txt", "r")
    words = [i for i in wordsFile] # I can make this more efficient but whatever
    picked_words = []
    for i in range(value):
        number = randint(0, len(words))
        picked_words.append(words[number].replace("\n", ""))
    return picked_words
main()
