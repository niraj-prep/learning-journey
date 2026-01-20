"""In a steel plant, the quality of steel is graded according to the following conditions:
(i) Hardness must be greater than 50
(ii) Carbon content must be less than 0.7
(iii) Tensile strength must be greater than 5600
The grades are as follows:
Grade is 10 if all three conditions are met
Grade is 9 if conditions (i) and (ii) are met
Grade is 8 if conditions (ii) and (iii) are met
Grade is 7 if conditions (i) and (iii) are met
Grade is 6 if only one condition is met
Grade is 5 if none of the conditions are met
Construct a program, which will require the user to give values of hardness, carbon content and tensile strength of
the steel under consideration and output the grade of the steel"""

hardness = float(input("Enter the hardness of the steel: "))
carbon_content = float(input("Enter the carbon content of the steel: "))
tensile_strength = float(input("Enter the tensile strength of the steel: "))

grade = 0
condition1 = hardness > 50
condition2 = carbon_content < 0.7
condition3 = tensile_strength > 5600

if condition1 and condition2 and condition3:
    grade = 10
elif condition1 and condition2:
    grade = 9
elif condition2 and condition3:
    grade = 8
elif condition1 and condition3:
    grade = 7
elif condition1 or condition2 or condition3:
    grade = 6
else:
    grade = 5
print(f"The grade of the steel is: {grade}")