trials = 2
round = 1
fruits = ["apple", "grape", "orange", "peach", "pear", "banana"]
m1 = f"\nYou can pick {trials} fruits."
m2 = f"You did not enter a number. Try again!\n"
m3 = f"You number is not from 1 - {len(fruits)}. Try again!\n"

def get_user_input(m):
	while True:
		try:
			fruit_number = int(input(m))
		except ValueError:
			print(m2)
		else:
			if fruit_number < 1 or fruit_number > len(fruits):
				print(m3)
			else:
				return fruit_number

fruits.sort()
print(m1)
while trials >= round:
	m = f"\nEnter a number from 1 - {len(fruits)} to pick fruit #{round}: "
	print(fruits[get_user_input(m) - 1])
	round += 1
