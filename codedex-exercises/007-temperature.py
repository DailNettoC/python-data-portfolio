"""
Title: 007 - Temperature
Source: Codedex

"""

#Creating a program to convert a number from  Fahrenheit (°F) to Celsius (°C).

fahrenheit = float(input('Enter the temperature: ')) #Using float to allow decimal numbers
celsius = (fahrenheit - 32) / 1.8 #Conversion formula
print(f"{fahrenheit}°F is {celsius:.2f}°C")

