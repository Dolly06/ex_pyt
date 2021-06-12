fname = input('Enter a file name:')
if len(fname)<1:
    fname = 'clown.txt'
handle = open(fname)
di = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for wrd in words:
        # if key doesn't exist, the count is zero then adds one as the word has been added to the dictionary
        di[wrd] = di.get(wrd,0) + 1
        # surrounds the wrd in single quotes
        # doesn't gives a space between the wrd and the quotes(using sep)
        # enables the other line be printed on the same line separating it with a space(using end)
        print("'",wrd,"'", sep='',end=' ')
        print('appears', di[wrd], 'time(s)')
print(di)  # prints the words in the dictionary and the count of each word
# checking for the most common word
largest = -1
theword = None
for key,value in di.items():  # loops through items in the dictionary
    print(key, value)  # prints the key and the value
    if value > largest:  # checks for largest value in the dictionary
        largest = value  # assigns largest value to largest
        theword = key  # assigns word with largest value(count) to theword
print(theword, 'is the word with the largest value is :',largest)