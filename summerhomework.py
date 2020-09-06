fruits = ["apple", "grape", "orange", "peach", "pear"]
trials = 2
rounds = 1
message1 = f"Please enter a number from 1 - {len(fruits)} to get a fruit: "
message2 = f"You did not enter a number. Try again!\n"
message3 = f"You number is not from 1 - {len(fruits)}. Try again!\n"

while trials >= rounds:
	try:
	   fruit_number = int(input(message1))
	except ValueError:
	   print(message2)
	else:
		if fruit_number < 0 or fruit_number > len(fruits):
			print(message3)
		else:
			fruits.sort()
			print(fruits[fruit_number - 1], "\n")
			rounds += 1
