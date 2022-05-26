def my_func ( *numbers ):
	sum = 0
	for i in range(len(numbers)):
		sum += numbers[i]
	print(numbers)
my_func(1,1,1,1,1,1,1,1,1,1)