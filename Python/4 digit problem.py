# 4 digit problem statement

def is_valid_num(num):
    num_str=str(num)
    if len(num_str)!=4:
        return False
digit_count={}
for digit in num_str:
    if digit in digit_count:
        digit_count