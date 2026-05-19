# 9. Program using and & or operators
age=int(input("Enter Your Age:"))
marks=int(input("Enter Your Marks:"))
if age>=18 and marks>=50:
    print("You are eligible")
else:
    print("You are not eligible")

if age < 18 or marks < 40:
    print("Condition using OR is True")