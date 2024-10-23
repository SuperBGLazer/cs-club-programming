import random

def update(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    c = random.choice(letters)
    pos = random.randint(0, len(word) -1)
    newstring = word[0:pos] + c + word[pos + 1:]
    return newstring

def main():
    happy = "rando"
    birthday = "randommm"
    trenton = "randomm"
    finallineexclamation = "!"
    while happy != "Happy":
        happy = update(happy)
        happy.title()
    while birthday != "birthday":
        birthday = update(birthday)
    while trenton != "Trenton":
        trenton = update(trenton)
        trenton.title()
    print(f"{happy} {birthday} {trenton}{finallineexclamation}")

if __name__ == '__main__':
    main()