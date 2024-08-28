#paranthesis problem

def check_parentheses(s):
    count= []
    pair_count = 0
    
    for char in s:
        if char == '(':
            count.append(char)
        elif char == ')':
            if count:
                count.pop()
                pair_count += 1
            else:
                return "improper arrangement"
    
    if count:
        return "improper arrangement"
    
    return f"{pair_count} pairs"

print(check_parentheses("((()(()()))"))  
print(check_parentheses("((()))"))      
