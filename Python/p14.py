'''Program to find 2nd smallest digit in a number'''

n = int(input("Enter a number: "))
digits = list(set(str(n)))
digits.sort()
if len(digits) < 2:
    print("No 2nd smallest digit")
else:
    print("2nd smallest digit is:", int(digits[1]))