from aifc import Error

'''

    This is just wordle, if you pass it a word it will let you play against it if you want to.

'''
def wordle(word, tries=6):
    word = word.lower() # easier for case-sensitivity
    print("Input a word:")
    for i in range(tries):
        player_word = input().lower() 
        solution = findLetters(word, player_word) # gets the solution for wordle.
        print(solution)
        isRight = True
        for i in solution:
            if i != "Green":
                isRight = False # if it finds anything that isn't green it's wrong and sets it wrong
        if isRight:
            print("Successfully guessed the word!\n")
            break # breaks are gross 
                
'''

    Algorithm that finds if the word given by the player, and sees each occurrence in the word,
    Then writes those values to an array.

'''
def findLetters(word, playerWord):
    solution = ["" for i in range(len(word))] # needs to be an empty list of size len(word) so we can manipulate it later
    if len(playerWord) != len(word):
        raise Error("Guess of word is not of the same size.") # Throw a general error if words are not of the same length.
    for i in playerWord:
        solutionPos = findOccurrences(word,i) # find each occurrence of a word, throw it to a list
        playerPos = findOccurrences(playerWord,i) # same here
        for j in playerPos:
            if j in solutionPos:
                solution[j] = "Green" # Correct Placement in word
            else:
                solution[j] = "Yellow" # Letter inside word, but in incorrect place
        if len(solutionPos) == 0:
            for j in playerPos:
                solution[j] = "Grey" # Letter not inside word.
    return solution
            
                

'''

    Returns a list of indices where each letter occurs in the string. 
    Taken from stackoverflow: https://stackoverflow.com/questions/13009675/find-all-the-occurrences-of-a-character-in-a-string 
    Shoutouts that guy

'''

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch] 