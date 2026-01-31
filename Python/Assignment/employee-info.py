"""Construct a program to store the information of an employee such as name, employee ID, department and generate
the salary as per the following conditions:
(i) DA is 92% of Basic Salary
(ii) HRA is 58% of Basic Salary
(iii) TA is 30% of Basic Salary
(iv) LIC is deducted: Rs. 500 every month"""

name = str(input("Enter Employee Name: "))
empID = (input("Enter Employee ID: "))
department = str(input("Enter Department: "))
salary = float(input("Enter Basic Salary: "))
da = 0.92 * salary
hra = 0.58 * salary
ta = 0.30 * salary
lic_deduction = 500.0
gross_salary = salary + da + hra + ta
net_salary = gross_salary - lic_deduction


print("-----Employee Information-----")
print("Employee Name:", name)
print("Employee ID:", empID)
print("Department:", department)
print("Basic Salary: Rs.", salary)
print("DA : Rs.", da)
print("HRA : Rs.", hra)
print("TA : Rs.", ta)
print("LIC Deduction: Rs.", lic_deduction)
print("Gross Salary: Rs.", gross_salary)
print("Net Salary: Rs.", net_salary)