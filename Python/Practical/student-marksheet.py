"""Write a Python program to generate the marksheet of a student.
The program should accept the student's name, department, year, semester, section, and roll number, along with the marks obtained in the 5-semester subjects.
It should then calculate the total marks and percentage, and display the marksheet in a clean and formatted manner.
The program must take all student details and marks as input, compute the total and percentage, and print the complete marksheet neatly."""

name=(input("Name: "))
dep=(input("Department: "))
yr=(input("Year: "))
sem=(input("Semester: "))
sec=(input("Section: "))
roll=(input("Roll Number: "))
s1=float(input("Enter marks for subject 1: "))
s2=float(input("Enter marks for subject 2: "))
s3=float(input("Enter marks for subject 3: "))
s4=float(input("Enter marks for subject 4: "))
s5=float(input("Enter marks for subject 5: "))

print("STUDENT MARKSHEET")
print("Name:",name)
print("Department:",dep)
print("Year:",yr)
print("Semester:",sem)
print("Section:",sec)
print("Roll Number:",roll)
print("Subject 1 Marks:",float (s1))
print("Subject 2 Marks:",float (s2))
print("Subject 3 Marks:",float (s3))
print("Subject 4 Marks:",float (s4))
print("Subject 5 Marks:",float (s5))

total=(s1+s2+s3+s4+s5)
per=(total/5)

print("Total Marks:",float(total))
print(f"Percentage: {per:.2f}%")