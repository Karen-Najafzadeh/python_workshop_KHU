# here we wanna manage a bunch of students with functional programming

students= []
loop= int(input("\n how many students does your class have? \t"))
for i in range(loop):
    students.append(input(f"\n enter student number {i+1} \t"))

print("\n OK students are done.\n")


#we'll define our functions here

def Add (name):
    students.append(name)
    print (f"\nAdding {name} to the list was succesfull!\n")

def Delete (name):
    students.remove(name)
    print (f"\n Deleting {name} from the list was succesfull!\n")

def Quit ():
    print(f"\n\n here are your students\n\n {students} \n\n")

def show():
    print(f"your current students are {students}")


#here we write our loop
var=12
while(var!="Exit"):
    condition= input("\n Now what do you want to do? Just type the exact words (pay attention to capital letters) \n Add (Adds someone to the list)\n Delete (Deletes somebody of the list)\n Quit (End the programm and see the result)\n Show (Show me what I got here)\n\n")
    
    if(condition=="Add"):
        name=input("\nEnter the name you want to add \n")
        Add(name)
    elif(condition=="Delete"):
        name=input("\nEnter the name you want to delete \n")
        Delete(name)
    elif(condition=="Show"):
        show()
    elif(condition=="Quit"):
        Quit()
        break
