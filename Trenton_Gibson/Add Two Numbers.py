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