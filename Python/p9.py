# Program to Print Math table of a number
input_num=int(input('Enter the number to create a math table'))
for i in range(1,11):
    print('%02d * %02d = %03d'%(input_num,i,input_num*i))