#Summer Homework Times Tables#

n = 1
times = int(input("What times table would you like to print? (1-12) >> "))

if times <= 12:
    if times >= 1:
        for x in range(12):
            print(times*n)
            n = n+1
    else:
        print("Please choose a number in range.")

else:
    print("Please choose a number in range.")
