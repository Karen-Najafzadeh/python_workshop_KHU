# if the rate of copy is 2 copy/min the the total number of bacteria is given by 2**n
rate = 2 #copy/min
time = int ( input("how long the process in going on (min)?\n")) # min
n = time*rate # copy/min * min = copy

amount = 2**n

print(f"after {time} minuets, you will have {amount} bacteria ")