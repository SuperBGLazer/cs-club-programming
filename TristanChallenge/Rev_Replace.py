
word=input("Enter a word:")

wordlist=list(word)
newwordlist=[]
for char in wordlist:
    temp = ord(char)
    if temp == 97 or temp == 101 or temp == 105 or temp == 111 or temp == 117:
        newchar=char.capitalize()
        newwordlist.append(newchar)

    else:
        newwordlist.append(char)

newwordlist.reverse()
print(newwordlist)


        




