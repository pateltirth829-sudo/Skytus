#1 Handle Division by Zero Error
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

#2 Handle Invalid Integer Input
try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input") 

#3 Handle File Not Found Error
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found")

#4 Demonstrate Multiple Exception Blocks
try:
    num = int(input("Enter number: "))
    result = 10 / num
    print(result)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

#5 Use Finally for Resource Cleanup
try:
    file = open("data.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("Program finished")

#6 Custom Exception for Invalid Age (<18)
age = int(input("Enter age: "))

try:
    if age < 18:
        raise Exception("Age must be 18 or above")

    print("Valid Age")

except Exception as e:
    print(e)

#7 Handle IndexError When Accessing a List
try:
    numbers = [10, 20, 30]

    print(numbers[5])

except IndexError:
    print("Index out of range")

#8 Take Two Numbers and Handle Errors
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError:
    print("Enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")

#9 Log Errors to a File
try:
    print(10 / 0)

except Exception as e:
    file = open("error.txt", "a")
    file.write(str(e) + "\n")
    file.close()

    print("Error saved in file")

#10 Validate Email Format
email = input("Enter email: ")

try:
    if "@" not in email:
        raise Exception("Invalid Email")

    print("Valid Email")

except Exception as e:
    print(e)