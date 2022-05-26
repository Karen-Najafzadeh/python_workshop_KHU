# a program to determine Even or Odd numbers which are given from user in a list


#taking numbers from user

number = int (input("how many numbers do you have? \n"))
list_of_numbers = []
for i in range (number):
    list_of_numbers.append(int (input(f"give me number {i+1} \t")))



# Creating a list for Odd numbers and Even numbers to show them later
Even = []
Odd = []

# algorithm and calculations
#looping the list
for i in range (len(list_of_numbers)):

    #checking even and not zero
    if(list_of_numbers[i] % 2 == 0 and list_of_numbers[i] != 0):
        Even.append(list_of_numbers[i])

    #checking odd
    elif(list_of_numbers[i] % 2 != 0):
        Odd.append(list_of_numbers[i])

#printing result

print(f"\n Your Even numbers are {Even} ")
print(f"\n And your Odd numbers are {Odd} ")