def regex(pattern, string):
    prev = ""
    idx = 0
    try:
        for i in range(len(pattern)):
            el = pattern[i]
            if prev != "":
                if el == "*":
                    idx = do_star(prev, string, idx)
                elif el == ".":
                    string[i]
                else:
                    print("prev and string[idx]", prev, string[idx])
                    if prev != string[idx]:
                        return False
                idx += 1

            prev = el
    except IndexError:
        print("index error")
        return False
    print(idx, len(string) - 1)
    if idx != len(string) -1:
        return False
    return True

def do_star(char, string, idx):
    print("do_star", char, string, idx)
    for i in range(idx, len(string)):
        if string[idx] == char:
            idx += 1
            print("success")
        else:
            print("fail")
            break
    print(idx)
    return idx

print(regex("abc", "abc"))
print(regex("abc", "abcd"))
print(regex("ab*c", "abbbc"))
print(regex("ab*c", "ac"))
print(regex("ab*c.", "acd"))
