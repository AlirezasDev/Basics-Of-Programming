import re

def check(s):
    possibilities = [s]
    
    while possibilities:
        current = possibilities.pop()
        
        while re.search(r'\(\)', current):
            current = re.sub(r'\(\)', '', current)
        
        if not current:
            return True
        
        if '*' in current:
            possibilities.append(current.replace('*', '', 1))
            possibilities.append(current.replace('*', '(', 1))
            possibilities.append(current.replace('*', ')', 1))
    
    return False

s = input().strip()
result = check(s)
print("True" if result else "False")
