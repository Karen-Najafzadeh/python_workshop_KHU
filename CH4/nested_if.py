# a program that checks the education of a person 


# person
education = {"elementary_school" : "Iran" , "Primary_school" : "Iran" , "high_school" : "Iran"}

#algorithm
if (education["elementary_school"]=="Iran"):
	print("elementary school in Iran")

	if (education["Primary_school"]=="Iran"):
		print("primary also Iran")

		if (education["high_school"]=="Iran"):
			print("high school also Iran ")

		else:
			print("high school in other contry")

	else:
		print("Primary school in other country")

else:
	print("elementary school in other country")

#checking if the person might be persian or not
# commented but effective and tested
#if (education["elementary_school"]=="Iran" and education["Primary_school"]=="Iran" and education["high_school"]=="Iran"): print("persian")
#if (education["elementary_school"]=="Iran" and education["Primary_school"]=="Iran" and education["high_school"]=="Iran"): print("may be Persian")