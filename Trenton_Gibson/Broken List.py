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
			input_list.append(riddle)
			Robot_Mood="Satisfied"
		else:
			input_list.append(riddle)
	input_list.append(user_input)
print(input_list)