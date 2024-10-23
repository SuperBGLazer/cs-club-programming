import random

b_day="Happy Birthday Trenton"
strings=[]
char_ascii=[]
bin_char=[]
hex_char=[]
message_list=[]
message_list2=[]
message=""

for char in b_day:
	strings.append(char)
	
print(strings)
count=0
while count < 22:
	rand=random.randrange(0, 22)
	rand_char=ord(strings[rand])
	if rand_char==ord(strings[count]):
		char_ascii.append(rand_char)
		count+=1

print(char_ascii)

for char in char_ascii:
	char=bin(int(char))
	bin_char.append(char)

print(bin_char)
for char in bin_char:
	binary_str = char.lstrip('0b')
	decimal = int(binary_str, 2)
	hex_str = hex(decimal)[2:]
	hex_char.append(hex_str)
	
print(hex_char)
for char in hex_char:
	char=int(char, 16)
	message_list.append(char)

print(message_list)
for char in message_list:
	char=chr(char)
	message_list2.append(char)
	
print(message_list2)
for char in message_list2:
	message+=char

print(message)
