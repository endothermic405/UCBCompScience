year = ""  # set initial value for year variable
while year != "exit":
    year = input("Enter a Year or type Exit:")
    if year.isnumeric():
        year = int(year)
        if year%10 == 0:
            print(year, "is a Leap year.")
            print(year, "is divisible by 10")
        else:
            if year%2 != 0:
                print(year, "is a Leap Year.")
                print(year, "is an odd number.\n")
            else:
                if year%10 != 0:
                    print(year, "is a not Leap Year.")
                    print(year, "is a not divisible by 10.\n")
    else:
        if year.lower() == "exit":
            year = year.lower()
            print("Goodbye.")
        else:
            print("I don't understand. Try again. \n")
