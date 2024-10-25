# Winners

| Place | Name    | Points |
|-------|---------|--------|
| 1     | Austin  | 201    |
| 2     | Josie   | 174    |
| 3     | Trenton | 140    |
| 4     | Mason   | 50     |
| 5     | William | 45     |
| 6     | Andrew  | 35     |
| 7     | Dylan   | 10     |
| 8     | Tristan | 8      |

# Bad grades challenge winners

## Complicated Hello World
Winner: Mason

```python
Winner: Mason

```python
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
```


## Add two number
Winner: Trenton

```python
import random

random_num=0
random_num2=0

random_word=""
random_word2=""

count=0
char=''
while count< 10:
	char=random.randrange(0,256)
	if char%2==0:
		count+=1
	char = str(char)
	random_word+=char

print(random_word)
count=0
while count< 10:
	char=random.randrange(0,256)
	if char%2==0:
		count+=1
	char=str(char)
	random_word2+=char

print(random_word2)
random_num=int(random_word)**int(random_word2)
random_num2=int(random_word)/int(random_word2)
print(random_num)
print(random_num2)

print(random_num+random_num2)
# random_num=chr(random_num)
# random_num2=chr(random_num2)
#
# print(random_num)
# print(random_num2)
```

## List program
Winner: Trenton

```python
Robot_Mood="Unsatisified"
input_list=[]
while Robot_Mood!="Satisfied":
	user_input=input(str("Let's play a game! Tell me something, and I'll add it to a list that'll\n"
						 "you'll see again later. Tell me the right thing and I'll let you go. If\n"
						 "you don't, well ... ;)"))
	if "what" in user_input or "What" in user_input:
		print("Glad you asked!\n")
		riddle=input(str("Answer this riddle you'll be free from your torment... maybe ;). \n"
						 "The more you code, the more of me there is. I may be gone for now\n"
						 " but you can’t get rid of me forever. What am I?\n"))
		if "bug" in riddle or "Bug" in riddle:
			print("Well done. Come back so we can have fun again tee hee hee!:P")
			input_list.append(riddle)
			Robot_Mood="Satisfied"
		else:
			input_list.append(riddle)
	input_list.append(user_input)
print(input_list)
```

## Average
Winner: No one attempted it