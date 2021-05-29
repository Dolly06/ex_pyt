num = 0
total = 0.0
while True:  # loops indefinitely till stopped
    try:
        sval = input("Enter a number:")  # prompts user input
        if sval == 'done':  # checks if input matches "done" and then exits the while loop after printing "Done!"
            print('Done!')
            break
        fval = float(sval)  # converts input to float
        num = num + 1  # increments count by one for correct inputs
        total += fval  # sums inputs
        ave = total/num  # calculates average
    except:
        print("Invalid input")  # prints "Invalid input" if input is wrong

print('sum:', total, ',count:', num, ',average:', ave)  # Displays sum, count and average