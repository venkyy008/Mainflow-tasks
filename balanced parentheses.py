def is_balanced(s):
    stack = []
    # Dictionary to hold matching parentheses pairs
    matching_parentheses = {')': '(', ']': '['}
    
    for char in s:
        if char in '([':
            # If it's an opening parenthesis, push to stack
            stack.append(char)
        elif char in ')]':
            # If it's a closing parenthesis, check stack