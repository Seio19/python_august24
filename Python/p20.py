'''Program to print the Equi Lateral Triangle of N lines'''

no_of_rows=int(input('Enter the number of rows:'))
for i in range(no_of_rows):
    print(' '* (no_of_rows-i-1),end=' ')
    print( '*'* (2*i+1))