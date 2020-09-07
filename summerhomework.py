fruits = ["apple", "pear", "orange", "grape", "peach"]
trials = 2
rounds = 1

while trials >= rounds:
	number_fruit = int(input("Please enter a number from 0 - 4 to get a fruit: "))
	if number_fruit == 1:
		print(fruits[0])
		rounds += 1
	elif number_fruit == 2:
		print(fruits[1])
		rounds += 1
	elif number_fruit == 3:
		print(fruits[2])
		rounds += 1
	elif number_fruit == 4:
		print(fruits[3])
		rounds += 1
	elif number_fruit == 5:
		print(fruits[4])
		rounds += 1
	else:
		print("You did not enter a number from 0-4, you can try again")
		rounds += 1

