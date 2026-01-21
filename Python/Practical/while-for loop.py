"""Write a Python program to print the statement "Hello Students" exactly twenty times using both:

.a while loop, and
.a for loop"""

n = int(input("Enter the number of times to print: "))
# Using while loop
print("Using while loop:")

i=1
while i <= n:
	print("Hello Students")
	i=i+1

# Using for loop
print("Using for loop:")
for i in range(1,n+1    ):
	print("Hello Students")
