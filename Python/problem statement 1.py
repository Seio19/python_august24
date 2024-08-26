def perfect_squared_numbers(bill_amount):
    count=0
    for amount in bill_amount:
        sqrt = int( amount ** 0.5 )
        if sqrt * sqrt ==amount:
            count += 1
    return count
bill_amount =[25, 56 ,74 ,81, 79, 25, 100, 144, 265, 625]
discounted_numbers =perfect_squared_numbers(bill_amount)
print('The number of people who will be discounted are:',discounted_numbers)
    

