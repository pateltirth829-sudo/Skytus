# 11. Create a dictionary storing student names and marks
students = {
    "Rahul": 85,
    "Priya": 90,
    "Amit": 78
}

print(students)


# 12. Add a new key-value pair to an existing dictionary
students["Neha"] = 88
print(students)


# 13. Delete a key-value pair from a dictionary
del students["Amit"]
print(students)


# 14. Merge two dictionaries into one
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {**dict1, **dict2}

print(merged)


# 15. Check if a key exists in a dictionary
students = {"Rahul": 85, "Priya": 90}

if "Rahul" in students:
    print("Key exists")
else:
    print("Key does not exist")


# 16. Count word frequency in a string using a dictionary
text = "apple banana apple mango banana apple"

words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)


# 17. Find the key with the maximum value in a dictionary
marks = {
    "Rahul": 85,
    "Priya": 95,
    "Amit": 78
}

highest = max(marks, key=marks.get)

print("Highest marks:", highest)


# 18. Reverse keys and values in a dictionary
data = {
    "a": 1,
    "b": 2,
    "c": 3
}

reversed_dict = {value: key for key, value in data.items()}

print(reversed_dict)


# 19. Update the value for a specific key
students = {
    "Rahul": 85,
    "Priya": 90
}

students["Rahul"] = 95

print(students)


# 20. Convert a list of tuples into a dictionary
data = [("a", 1), ("b", 2), ("c", 3)]

result = dict(data)

print(result)