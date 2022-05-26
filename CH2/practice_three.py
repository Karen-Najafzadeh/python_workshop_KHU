s = float (input("what is the speed? (km/h) \n"))
d = float(input(" what is the distance? (km) \n"))
s = s/60  # casting km/h to km/min
time = d/s 
print(f"this trip will take {time} minuets")