#1 Function to check if a number is prime
def prime(n):
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    if count == 2:
        print("Prime Number")
    else:
        print("Not Prime Number")

prime(7)

#2 Function to reverse a string
def reverse_string(text):
    print(text[::-1])

reverse_string("hello")

#3 Function to find factorial
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    print(fact)

factorial(5)

#4 Function to calculate simple interest
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    print(si)

simple_interest(1000, 5, 2)

#5 Function to check if a word is palindrome
def palindrome(word):
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome("tirth")

#6 Function to count vowels in a string
def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    print(count)

count_vowels("Hello")

#7 Function to merge two lists
def merge_lists(list1, list2):
    print(list1 + list2)

merge_lists([1, 2, 3], [4, 5, 6])

#8. Function to find GCD of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    print(a)

gcd(12, 18)

#9 Function to find area of rectangle
def rectangle_area(length, width):
    print(length * width)

rectangle_area(5, 4)

#10 Function to check Armstrong number
def armstrong(num):
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp = temp // 10

    if total == num:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

armstrong(153)