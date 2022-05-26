#BMI Calculator


#Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²

#The resulting number indicates one of the following categories:
#Underweight = less than 18.5
#Normal = more or equal to 18.5 and less than 25
#Overweight = more or equal to 25 and less than 30
#Obesity = 30 or more

#Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.

#Sample Input
#85
#1.9

#Sample Output
#Normal

#code :

weight = input("gimme your weight (Kg) \n")
height = input("gimme your height (cm) \n")

weight=float(weight)
height=float(height)
BMI = float((weight/(height**2)))

if BMI<18.5:
    print ("Underweight")
if ( BMI>=18.5 and BMI<25 ):
    print("Normal ")
if ( BMI>=25 and BMI<30 ):
    print ("Overweight ")
if (BMI >= 30):
    print ("Obesity")
