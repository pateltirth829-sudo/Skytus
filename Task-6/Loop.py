#1 Print numbers from 1 to 10 
for i in range(1, 11):
    print(i)

#2 display multiplication table for given number 
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#3 Find Factorial of the number 
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)

#4 Generate the first n fibonacci numbers
n = int(input("Enter N: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    
#5 check the number is prime
num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime Number")

#6 Reverse the number 
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse =", rev)

#7 count digit in number
num = int(input("Enter a number: "))
count = 0

while num > 0:
    count += 1
    num = num // 10

print("Digits =", count)

#8 Find some even numbers between 1 to 100

sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum += i

print("Sum =", sum)

#9 Print a pyramid pattern
rows = 5

for i in range(1, rows + 1):
    print("*" * i)

#10 Find all divisor of a number
num = int(input("Enter a number: "))

print("Divisors are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)