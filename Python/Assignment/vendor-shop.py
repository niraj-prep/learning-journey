"""Construct a program to store the following details of a Vendor of a Shop.
a) Name of vendor
b) Year of association
c) Contact number
d) eMail ID
Read the details of monthly purchases from Vendor and generate a Annual Purchase/Billing report"""

name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = int(input("Enter Contact Number: "))
email = input("Enter Email ID: ")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
purchases = []

print("\nEnter Monthly Purchases:")
for month in months:
    amount = float(input(f"{month}: "))
    purchases.append(amount)

print("\n" + "="*50)
print("ANNUAL PURCHASE REPORT")
print("="*50)
print(f"Vendor Name: {name}")
print(f"Year of Association: {year}")
print(f"Contact: {contact}")
print(f"Email: {email}")
print("="*50)

print(f"\n{'Month':<10} {'Amount':<10}")
print("-"*20)
for i in range(12):
    print(f"{months[i]:<10} ₹{purchases[i]:<10.2f}")

total = sum(purchases)
print("-"*20)
print(f"{'TOTAL':<10} ₹{total:<10.2f}")
print("="*50)