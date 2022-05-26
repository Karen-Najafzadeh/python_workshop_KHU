# aprogram to show if a Satellite survives with it's given situations like mass and hight and speed 
# we take Gravitational constant as GC
import math

GC = 6.67e-11

#proof of formula r and v
# F = G m1 m2 /r**2
# m1 a = G m1 m2 /r**2
# m1 v**2/r = G m1 m2 /r**2
# v**2 = G m2 / r
# so that 
# m2 = v**2 r /G
# r =G m2 / v**2

# we will take mass as an input 
# and will show the possible v and r for survival of the satellite

mass = float(input("what is the planet's mass?\n"))


r = float(input("to what orbid this satellite will be sent? \n"))
v = math.sqrt((GC*mass)/r)

print(f"the velocity of satellite must be {v} (m/s) to survive on the orbit or it will fall")


#15/2/1401
#program is finished 