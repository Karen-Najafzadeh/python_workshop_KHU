# a program to predict when does a moon collaps in it's primary planet's gravitual field
# the roche limit formula is :
# d = 1.26R(𝜌M/𝜌m)^3/2
#where 𝜌M is the density of the primary planet and 𝜌m is the density of the satellite
# and R is the radius of the primary planet


#just to know

# density and radius of some objects

#Primary	Density (kg/m3)	Radius (km)
#Sun	    1,408	        696,000
#Earth	    5,513	        6,378
#Moon	    3,346	        1,737
#Jupiter	1,326	        71,493
#Saturn	    687	            60,267
#Uranus	    1,318	        25,557
#Neptune	1,638	        24,766


# inputs
𝜌M = float(input("what is the primary's density? (kg/m3)\n"))
𝜌m = float(input("what is the satellite's density? (kg/m3)\n"))
R = float(input("what is the radius of the primary? (km)\n"))

# calculations
d = 1.26*R*((𝜌M/𝜌m)**(1/3))

# output
print(f"the roche limit for this planet and it's satellite is : {d} (km)")

#some results from wikipedia  (https://en.wikipedia.org/wiki/Roche_limit#Rigid-satellite_calculation)

#Body	Satellite	    Roche limit (km)	
#Earth	Moon	        9,492				
#Sun	Earth	        556,397		
#Sun	Jupiter	        894,677		
#Sun	Moon	        657,161	


#program finished