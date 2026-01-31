"""Write a Python program to classify temperatures in degrees Celsius based on the following conditions:

If the temperature is less than -273.15, print: "Invalid temperature: below absolute zero".
If the temperature is exactly -273.15, print: "Temperature is absolute zero".
If the temperature is between -273.15 and 0, print: "Temperature is below freezing".
If the temperature is exactly 0, print: "Temperature is at the freezing point".
If the temperature is between 0 and 100, print: "Temperature is in the normal range".
If the temperature is exactly 100, print: "Temperature is at the boiling point".
If the temperature is greater than 100, print: "Temperature is above the boiling point"."""

temp =float(input("Enter temperature in degree Celsius: "))

if temp < -273.15:
	print("Invalid temperature: below absolute zero")
elif temp == -273.15:
	print("Temperature is absolute zero")
elif -273.15 < temp < 0:
	print("Temperature is below freezing")
elif temp == 0:
	print("Temperature is at the freezing point")
elif temp < 100:
	print("Temperature is in the normal range")
elif temp == 100:
	print("Temperature is at the boiling point")
elif temp > 100:
	print("Temperature is above the boiling point")
else:
	print("Invalid entry")