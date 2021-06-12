name = input("Enter file:")  # prompts input of filename
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()
lst = list()
for line in handle:
    if not line.startswith('From '):  # checks if line begins with 'From '
        continue  # starts next iteration if it does not
    else:
        line = line.rstrip()  # removes whitespaces
        line = line.split()  # splits line into a list of words
        line = line[5]  # line is now equal to words at 5th position
        line = line[:2]  # slices the string to only 2 strings
        print(line)
        count[line] = count.get(line, 0) + 1  # counts the occurrence of each word, if word doesn't exist it gives it a default value(0) then adds 1
        print(count[line])

for key, val in count.items():  # loops through the items in the dictionary
    tup = key, val  # creates new tuple
    lst.append(tup)  # adds the tuple to the list
    lst.sort()  # sorts list
print(lst)  # prints list of tuples
for key, val in lst:  # loops through list of tuples
    print(key, val)
