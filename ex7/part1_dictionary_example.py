fname = input('Enter a file name:')  # prompts input of filename
if len(fname)<1:  # checks if length of filename is 0(no filename entered)
    fname = 'clown.txt'  # assigns clown.txt if no filename was entered
handle = open(fname)  # opens file
di = dict()  # creates dictionary
for line in handle:  # loops through file
    line = line.rstrip()  # removes whitespaces at the end of the line
    print(line)
    words = line.split()  # splits the line into a list of words
    print(words)
    for wrd in words:
        if wrd in di:  # checks if each word is in the dictionary
            di[wrd] = di[wrd] + 1  # if it is then it increments the count of the word already in the dictionary
            print("**EXISTING**")
        else:
            di[wrd] = 1  # if not it sets the count of the new word to one
            print("**NEW**")
        print(wrd,di[wrd])  # prints the word and its count
print(di)  # prints the words in the dictionary and the count of each word
