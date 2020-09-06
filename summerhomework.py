fruits = ["apple", "pear", "orange", "grape", "peach"]

number_fruit = int(input("Please enter a number from 1 - 5 to get a fruit: "))

trials = 1
runs = 0

while trials >= runs:
	if number_fruit == 1:
		print(fruits[0])
		runs += 1
	elif number_fruit == 2:
		print(fruits[1])
		runs += 1
	elif number_fruit == 3:
		print(fruits[2])
		runs += 1
	elif number_fruit == 4:
		print(fruits[3])
		runs += 1
	elif number_fruit == 5:
		print(fruits[4])
		runs += 1
	else:
		print("You did not enter a number from 1-5, you can try again")
		runs += 1