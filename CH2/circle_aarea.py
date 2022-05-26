# a program to calculate the area of a circle
# inputs
R = input("what is the radius of your circle? \n")
pi = input("How much do you consider the pi number to be?\n")

#data casting
R = float(R)
pi = float(pi)

# calculation
A = pi*(R)**2

#output
print(f"the area of your circle is {A}")