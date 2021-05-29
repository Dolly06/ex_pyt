num = 0
total = 0.0
while True:  # loops indefinitely till stopped
    sval = input("Enter a number:")  # prompts user input
    if sval == 'done':  # checks if input matches "done" and then exits the while loop after printing "Done!"
        print('Done!')
        break  # exits while loop
    try:
        fval = float(sval)  # converts input to float
    except:
        print("Invalid input")  # prints "Invalid input" if input is wrong
        continue  # goes back to beginning of while loop to start the iteration again
    num = num + 1  # increments count by one for correct inputs
    total += fval  # sums inputs
    ave = total/num  # calculates average

print('sum:', total, ',count:', num, ',average:', ave)  # Displays sum, count and average