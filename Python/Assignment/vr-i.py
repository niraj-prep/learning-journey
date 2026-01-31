"""Develop a Python program that takes a voltage (V) and resistance (R) as inputs from the user and calculates the
current (I) using Ohm’s Law
Modify the above program to display the nature of current:
If current < 0.5 A, print Low current
If 0.5 A ≤ current ≤ 2 A, print “Normal current”
If current > 2 A, print High current"""

# Ohm's Law: I = V / R
voltage = float(input("Enter Voltage (V) in volts: "))
resistance = float(input("Enter Resistance (R) in ohms: "))
current = voltage / resistance

print(f"Calculated Current (I): {current:.2f} A")
if current < 0.5:
    print("Nature of Current: Low current")
elif 0.5 <= current <= 2:
    print("Nature of Current: Normal current")
else:
    print("Nature of Current: High current")
