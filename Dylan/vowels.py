def reverse_and_capitalize_vowels(s):
    vowels = set('aeiouAEIOU')
    chars = list(s)[::-1]
    result = []
    for char in chars:
        if char in vowels:
            result.append(char.upper())
        else:
            result.append(char)
    return ''.join(result)

print(reverse_and_capitalize_vowels("Happy Birthday Trenton"))