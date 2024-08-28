# Check if a number is Prime

number=int(input('ENter the number you want to check:'))
if number<=1:
    print('The number',number,'is not a prime number')
elif number==2:
    print('The number',number,'is a prime number')
else:
    for i in range(2,number):
        if number%i==0:
            print('The number',number,'is not a prime number')
            break
    else:
        print('The number',number,'is a prime number')
