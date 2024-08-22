'''Program to find biggest (smallest) digit in a number'''

number=input('Enter the digit you want to find smallest and biggest digit from: ')

biggest_digit = '0'
smallest_digit= '9'

for char in number:
    if char.isdigit():
        if char > biggest_digit:
            biggest_digit = char
        if char < smallest_digit:
            smallest_digit = char
print('biggest digit:',biggest_digit)
print('smallest digit:',smallest_digit)



