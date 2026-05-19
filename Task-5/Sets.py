# 4. Create a set of 5 fruits
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}
print(fruits)


# 5. Add a new fruit to the set
fruits.add("Pineapple")
print(fruits)


# 6. Remove an element from a set
fruits.remove("Banana")
print(fruits)


# 7. Find union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1.union(set2))


# 8. Find intersection of two sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print("Intersection:", set1.intersection(set2))


# 9. Check if one set is subset of another
set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1.issubset(set2))


# 10. Convert a list with duplicate values into a set
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)

print(unique_numbers)