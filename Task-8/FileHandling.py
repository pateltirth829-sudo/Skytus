#1 Read a file and display its contents
file = open("data.txt", "r")

print(file.read())

file.close()

#2 Count the number of lines in a file
file = open("data.txt", "r")

lines = file.readlines()

print("Total Lines:", len(lines))

file.close()

#3 Count how many times each word appears in a file
file = open("data.txt", "r")

text = file.read()
words = text.split()

for word in set(words):
    print(word, ":", words.count(word))

file.close()

#4 Write 5 user-entered sentences to a file

file = open("data.txt", "w")

for i in range(5):
    sentence = input("Enter sentence: ")
    file.write(sentence + "\n")

file.close()

#5 Append a list of strings to an existing file
file = open("data.txt", "a")

items = ["Apple", "Banana", "Mango"]

for item in items:
    file.write(item + "\n")

file.close()

#6 Print only lines containing a specific word
word = input("Enter word: ")

file = open("data.txt", "r")

for line in file:
    if word in line:
        print(line)

file.close()

#7 Replace a specific word in a file
file = open("data.txt", "r")

text = file.read()

file.close()

text = text.replace("old", "new")

file = open("data.txt", "w")
file.write(text)
file.close()

#8 Merge contents of two text files into a third file

file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

data1 = file1.read()
data2 = file2.read()

file3 = open("merged.txt", "w")
file3.write(data1 + data2)

file1.close()
file2.close()
file3.close()

#9 Read a CSV file and display its contents

import csv

file = open("data.csv", "r")

reader = csv.reader(file)

for row in reader:
    print(row)

file.close()

#10 Back up a file by copying its contents into another file

source = open("data.txt", "r")

content = source.read()

backup = open("backup.txt", "w")
backup.write(content)

source.close()
backup.close()