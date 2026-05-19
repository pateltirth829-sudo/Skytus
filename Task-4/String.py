# 1. Take a string input and print its length
text = input("Enter a string: ")
print("Length:", len(text))

# 2. Convert a sentence to lowercase
sentence = input("Enter a sentence: ")
print(sentence.lower())
# 3. Replace spaces with underscores in a string
text = input("Enter a string: ")
print(text.replace(" ", "_"))


# 4. Extract the first and last character of a string
text = input("Enter a string: ")
print("First character:", text[0])
print("Last character:", text[-1])


# 5. Reverse a string using slicing
text = input("Enter a string: ")
print("Reversed string:", text[::-1])


# 6. Count how many times a letter appears in a string
text = input("Enter a string: ")
letter = input("Enter a letter: ")
print("Count:", text.count(letter))


# 7. Check if a word is present in a sentence
sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

if word in sentence:
    print("Word found")
else:
    print("Word not found")


# 8. Take name & age and print using f-string formatting
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")


# 9. Remove extra spaces from the start and end of a string
text = input("Enter a string with spaces: ")
print(text.strip())


# 10. Join a list of words into a single string with - between them
words = ["Python", "Java", "C++"]
result = "-".join(words)
print(result)


