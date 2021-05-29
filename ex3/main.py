def computepay(hours, rate):
    print("Computing Pay...")
    if h <= 40:
        tp = h * r
        print("Pay is:", tp)  # Computes pay for hours <= 40

    else:
        reg = h * r  # Computes pay for hours <= 40 and displays(regular hours)
        otp = (h - 40.0) * (r * 0.5)  # Computes pay for extra hours
        tp = reg + otp  # Adds pay for extra and regular hours(<= 40)
        print("Pay is:", tp)  # Displays total pay
    return tp


hrs = input("Enter hours:")  # Gets number of hours from user
rte = input("Enter rate per hour:")  # Gets hourly rate from user
h = float(hrs)  # Converts input hours(string) to float
r = float(rte)  # Converts input rate(string) to float

pay = computepay(h, r)
print(pay)
