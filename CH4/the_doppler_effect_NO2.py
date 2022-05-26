# a program to determine the wavelenth of a moving light source (red/blue shift)
# suppose we have a light source at x=0 and an observor in x >> 0
# if :
# fs = frequency of light source 
# fo = frequency that observer reseives from the source
# c = the speed of light 
# vo = speed of observer
# vs = speed of source
# then the doppler effect for the case that source and observer are moving toward each other is calculated by:
# fo = fs*((c+vo)/(c-vs))
# and the doppler effect for the case that source and observer are moving away from each other is calculated by:
# fo = fs*((c-vo)/(c+vs))


#inputs



fs = int(input("what is the emmited frequency? (Hz)\n"))
print("please notice that speed of source, observer and travelling wave must have the same unit (m/s)(km/h)...\n")
vs = int(input("what is the speed of source? \n"))
vo = int(input("what is the speed of observer? \n"))
c = int(input("what is the speed of travelling wave ? \n"))
status = None

#algorithm

#determining the type of movement

if ((vs and vo) > 0):
    if(abs(vs)<abs(vo)):
        status = "away"
    else:
        status = "toward"
elif((vs and vo) < 0):
    if(abs(vs)<abs(vo)):
        status = "toward"
    else:
        status = "away"


if(vs*vo<0):
    if ( vs>0 and vo<0):
        status = "toward"
    else:
        status = "away"

# now that we have the status of motion we can use formula

if (status == "away"):
    fo = fs*(c-abs(vo))/(c+abs(vs))
else:
    fo = fs*(c+abs(vo))/(c-abs(vs))

#output
print(fo,status)