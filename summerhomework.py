apple = 1
pear = 2
orange = 3
grape = 4
peach = 5
list = [apple, pear, orange, grape, peach]
num = 0
while num == 1:
	number_fruit = input(int("Please enter a number from 1-5 to get a fruit:"))
	if number_fruit == 1:
		print(list[0])
		num = num + number_fruit
	elif number_fruit == 2:
		print(list[1])
		num = num + number_fruit
	elif number_fruit == 3:
		print(list[2])
		num = num + number_fruit
	elif number_fruit == 4:
		print(list[3])
		num = num + number_fruit
	elif number_fruit == 5:
		print(list[4])
		num = num + number_fruit
	else:
		print("You did not enter a number from 1-5, you can try again")