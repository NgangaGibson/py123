import math
radius=float(input("enter your radius of cylinder="))
height=float(input("enter your height of a cylinder="))
volume=math.pi*radius**2*height
print("the volume of cylinder is=",volume,"m^3")
surface_area=2*math.pi*radius*(radius+height)
print("the surface area of cylinder is:",surface_area,"m^2")