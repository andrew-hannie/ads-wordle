words = open("words_alpha.txt", 'r')
newFile = open("words_5_letter.txt", "w")
for i in words:
    if len(i) == 6:
        newFile.write(i)