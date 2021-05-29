handle = open('mbox-short.txt')  # opens file and handle is a connection to file's data
for line in handle:  # loops through file
    line = line.rstrip()  # removes whitespace at the end of the line
    wrds = line.split()  # splits the line into words according to its delimiter which is the whitespace
    if len(wrds) < 1:  # checks if length of words in a line is less than 1
        continue  # jumps to the "top" of the loop and starts the next iteration
    if wrds[0] == 'From':  # checks if 1st word is 'From'
        print(wrds[2])  # prints the 3rd word
    else:  # if the first word is not 'From'
        continue  # jumps to the "top" of the loop and starts the next iteration
