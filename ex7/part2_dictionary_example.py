fname = input('Enter a file name:')
if len(fname)<1:
    fname = 'clown.txt'
handle = open(fname)
di = dict()
for line in handle:
    line = line.rstrip()
    print(line)
    words = line.split()
   # print(words)
    for wrd in words:
        oldcount = di.get(wrd,0)  # if key doesn't exist, the count is zero
        print(wrd,',old count is:',oldcount)  # prints word and old count
        newcount = oldcount + 1  # increments count when the word is in the dictionary
        di[wrd] = newcount  # assigns new count to the value for each key(counter)
        print(wrd, ',new count is:', newcount)
print(di)  # prints the words in the dictionary and the count of each word
