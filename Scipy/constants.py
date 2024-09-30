# Constansts in Scipy

# from scipy.constants import pi,golden_ratio
# print(f"Pi: {pi}")
# print(f"Golden_ratio: {golden_ratio}")
# radius = 22
# print("Area of Circle:", (pi*radius*radius))

# from scipy.constants import m_n, Avogadro
# print("Mass of neutron:", m_n, "Kg")
# print("Avogadro No:", Avogadro)

# from scipy.constants import physical_constants
# print(physical_constants["alpha particle mass"]) # here we use square brackets becoz the output is in dictionary form
# print(physical_constants["atomic unit of time"]) 
# for key,value in physical_constants.items():
#     print(f"{key}:{value}")

# conversion of units
# from scipy.constants import kilo
# print(kilo)
# meters = 50
# print("Convert meter into kilo:", meters/kilo)

# from scipy.constants import deci,yotta
# print(deci)
# print(yotta)
# meters = 100
# print("Convert meter into yotta:", meters/yotta)
# print("Convert meter into decimeter:", meters/deci)

# Conversion of temperature
from scipy.constants import convert_temperature
fehrenheit = 90
celsius = convert_temperature(fehrenheit, "F", "C")
kelvin = convert_temperature(celsius, "C", "K")
print("Celsius:", celsius)
print("Kelvin:", kelvin)
