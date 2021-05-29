text = "X-DSPAM-Confidence:    0.8475"
col = text.find(':')  # searches for colon(:)
print(col)  # prints index of colon
piece = text[col + 1:]  # prints characters from after the colon till the end of the line
word = float(piece.lstrip())  # removes whitespace from the string "piece"(left side) and converts it to float
print(word)
for letter in 'banana' :
    print(letter)