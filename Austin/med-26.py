def balanced_paren(string):
    current_level = 0
    for el in string:
        if el == "(":
            current_level += 1
        elif el == ")":
            current_level -= 1
        if current_level < 0:
            return False
    return current_level == 0

print(balanced_paren("(())"))
print(balanced_paren("())"))
print(balanced_paren(")(())("))
