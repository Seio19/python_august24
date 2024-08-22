# Program to check if user given year is a Leap year.

given_year=int(input("Enter the year: "))

if given_year % 4 == 0 and (given_year % 100 != 0 or given_year % 400 ==0):
    print("The given year is a leap year")
else:
     print('Given year is not a leap year')
   