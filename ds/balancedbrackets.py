class BalanedBrackets:
    def __init__(self):
        pass
    def areBalancedBrackets(self,expr):
        stack = []
        for char in expr:
            if char in["(","{", "["]:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    char1 = stack.pop()
                    if char1 == "{" and char == "}":
                        return True
                    elif char1 == "(" and char == ")":
                        return True
                    elif char1 == "[" and char == "]":
                        return True
                    else:
                        return False


expr = "{()}[]"
bb = BalanedBrackets()
if bb.areBalancedBrackets(expr):
    print("Balanced Brackets")
else:
    print("unbalanced")
