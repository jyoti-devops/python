"""
Python3 program to check for balanced brackets.

"""


def are_brackets_balanced(expr):
    """
    Check that given symbol expression is balaced or not
    """
    stack = []
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:
            # Push the element in the stack
            stack.append(char)
        else:
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            is_bal = False
            current_char = stack.pop()
            if current_char == '(' and char == ')':
                is_bal = True
            if current_char == '{' and char == '}':
                is_bal = True
            if current_char == '[' and char == ']':
                is_bal = True

            return is_bal
    # Check Empty Stack
    if stack:
        return False
    return True


# Driver Code
if __name__ == "__main__":
    EXPR = "{()}[]"

    # Function call
    if are_brackets_balanced(EXPR):
        print("Balanced")
    else:
        print("Not Balanced")

# This code is contributed by AnkitRai01 and improved
# by Raju Pitta
