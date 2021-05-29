fhand = open('mbox-short.txt')  # opens file and fhand is a connection to the file's data

for line in fhand:  # loops through handle of file
    line_ = line.rstrip()  # removes whitespaces at the end of the line like the newline
    print(line_.upper())  # changes everything to uppercase

