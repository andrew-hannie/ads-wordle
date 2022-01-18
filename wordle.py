from aifc import Error
from re import L


def wordle(word, tries=5):
    word = word.lower()
    print("Input a word:")
    for i in range(tries):
        player_word = input().lower()
        solution = findLetters(word, player_word)
        print(solution)
        isRight = True
        for i in solution:
            if i != "Green":
                isRight = False
        if isRight:
            print("Successfully guessed the word!\n")
            break
                
        
def findLetters(word, playerWord):
    solution = ["" for i in range(len(word))]
    if len(playerWord) != len(word):
        raise Error
    for i in playerWord:
        solutionPos = findOccurrences(word,i)
        playerPos = findOccurrences(playerWord,i)
        for j in playerPos:
            if j in solutionPos:
                solution[j] = "Green"
            else:
                solution[j] = "Yellow"
        if len(solutionPos) == 0:
            for j in playerPos:
                solution[j] = "Grey"
    return solution
            
                

def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]