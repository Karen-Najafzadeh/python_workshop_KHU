# a programm to calculate the thermal expantion in a metal stick or surface or mass 
# the formula for Linear thermal expantion is:
# ΔL = L0*𝛼*ΔT
# the formula for Area expantion is:
# ΔA = A0*β*ΔT
# the formula for volume expantion is:
# ΔV = V0*𝛾*ΔT
# where:
# 𝛾 = 3*𝛼
# β = 2*𝛼

# where 𝛼 can be :
#here some Linear coefficient from wikipedia (https://en.wikipedia.org/wiki/Thermal_expansion#Expansion_in_solids)

#Material	       Linear coefficient at 20 °C (x10**-6 (K**-1))
#Water	           69		
#Tungsten	       4.5		
#Titanium	       8.6		
#Steel	           11.0
#Stainless steel   10.1	
#Silver	           18	
#Silicon Carbide   2.77	
#Silicon	       2.56

#inputs

L0 = float(input("what is the primary lengh of the stick? (m)\n"))
A0 = float(input("what is the primary area of the surface? (m2)\n"))
V0 = float(input("what is the primary volume of the object? (m3)\n"))
𝛼  = 1e-6*float(input("what is the Linear coefficient? (e-6 (K-1))\n"))
ΔT = float(input("what is the tempreture change of the object? (K)\n"))
# calculations

𝛾 = 3*𝛼
β = 2*𝛼

ΔL = L0*𝛼*ΔT
ΔA = A0*β*ΔT
ΔV = V0*𝛾*ΔT

#output

print(f"the linear, area and volume expantion of this material is {ΔL} (m), {ΔA} (m2) and {ΔV} (m3)")

# program finished