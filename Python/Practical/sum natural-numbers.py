"""Write a Python program to calculate the sum of all natural numbers starting from 1 up to a given number n.
The program should:

.Accept a positive integer n from the user.
.If n is less than 1, display an appropriate message.
.Otherwise, compute the sum of numbers from 1 to n and display the result."""

num = int(input("Enter a positive integer: "))

if num < 1:
    print("Please enter a number greater than 0")
else:
    s = 0
    for i in range(1, num + 1):
        s += i
    print("The sum of numbers from 1 to %d is:" % num, s)
