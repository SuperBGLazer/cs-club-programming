import string
BirthDayBoy = []
correct = ['T', 'r', 'e', 'n', 't', 'o', 'n']

print("whos birth is it today?")
answer = input()

for element in answer:
    BirthDayBoy.append(element)



if BirthDayBoy == correct:
    print("Yes thats the BirthDayBoy")
else:
    print("BAH WRONG YOU FOOL")
    print(BirthDayBoy)


