year = int(input("Enter a year (e.g. 2000): "))
leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
print(str(year) + " is a leap year (True/False):" + str(leap))