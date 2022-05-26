# the program of page 3 of chapter 4 

R1 = float(input("what is the first circle's radius?\n"))
R2 = float(input("what is the second circle's radius?\n"))
pi = 3.14 

#calculations
S1 = pi * (R1**2)
S2 = pi * (R2**2)

#conditions

if (S1>S2):
    print("s1 is greater than s2\n")
else:
    print("s1 is not greater than s2\n")
