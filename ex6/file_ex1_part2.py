handle = open('mbox-short.txt')  # opens file and handle is a connection to file's data
for line in handle:  # loops through file
    line = line.rstrip()  # removes whitespace at the end of the line
    wrds = line.split()  # splits the line into words according to its delimiter which is the whitespace
    if len(wrds) < 1 or wrds[0] != 'From':  # checks if length of words is less than 1 or 1st word is not 'From'
        continue  # jumps to the "top" of the loop and starts the next iteration'''
    print(wrds[2])  # prints the 3rd word
