"""Write a Python program that accepts three different integer numbers from the user
and determines which one is the largest among them."""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num2 < num1 >num3:
	print("The largest number is:",num1)
elif num2 > num3:
	print("The largest number is:",num2)
else:
	print("The largest number is:",num3)