

# 1. Create a list of your 5 favorite movies
movies = ["Taqdeer", "RRR", "Bahubali", "Pushpa", "Dragon"]
print(movies)


#2. Add a new movie to the list
movies.append("Dude")
print(movies)


# 3. Remove the first movie from the list
movies.pop(0)
print(movies)


# 4. Sort a list of numbers in ascending order
numbers = [45, 12, 78, 3, 56]
numbers.sort()
print(numbers)


# 5. Reverse a list
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)


# 6. Find the largest number in a list
numbers = [10, 50, 25, 90, 60]
print("Largest number:", max(numbers))


# 7. Merge two lists into one
list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = list1 + list2
print(merged)


# 8. Access the last element of a list without using index number
numbers = [10, 20, 30, 40]
print("Last element:", numbers[-1])


# 9. Create a nested list and access a specific inner element
nested = [[1, 2], [3, 4], [5, 6]]

print(nested[1][0])   


# 10. Count how many times an element appears in a list
numbers = [1, 2, 3, 2, 4, 2, 5]

print(numbers.count(2))