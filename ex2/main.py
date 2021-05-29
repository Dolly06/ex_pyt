# Type conversion
ival = '123'
print(type(ival))
sval = int(ival)
print(sval+1)
print(type(sval))

x = 36252.37291
print('x is %2.4f' %x)  # Output formatting

# Exercise on try and except
hrs = input("Enter hours:")  # Gets number of hours from user
rate = input("Enter rate per hour:")  # Gets hourly rate from user

try:  # Checks for error in the block of code
    h = float(hrs)  # Converts input hours(string) to float
    r = float(rate)  # Converts input rate(string) to float
except:  # Handles the error if any
    print("Error,please enter a number(s)")
    quit()  # Stops the program
if h <= 40:
    print("Pay is:", h * r)  # Computes pay for hours <= 40

else:
    reg = h * r  # Computes pay for hours <= 40 and displays(regular hours)
    otp = (h - 40.0) * (r * 0.5)  # Computes pay for extra hours
    tp = reg + otp  # Adds pay for extra and regular hours(<= 40)
    print("Pay is:", tp)  # Displays total pay


