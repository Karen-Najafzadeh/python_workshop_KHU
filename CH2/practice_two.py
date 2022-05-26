import math


R =  float ( input("what is the radius of youre sphere? (m)\n"))
#R = R*100 # casting m to cm
V = (4/3)*math.pi*(R**3)
print(" your volume is",V,"cm3")