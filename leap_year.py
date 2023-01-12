# leap year
n = 2000
if (n % 400 == 0 or (n % 100 != 0 and n % 4 == 0)):
    print("it is a leap year")

else:
    print("it is not a leap year")
