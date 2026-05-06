# Create two sets of numbers. Print numbers that are in both sets.

s1={1,2,3}
s2={2,3,4,5}
print(s1.intersection(s2))



# Create two sets. Print numbers that are in first set but not in second.
set1={1,2,3,4,5}  #1,2
set2={3,4,5,6}
print(set1.difference(set2))




# Take a list with duplicate values — remove all duplicates using a set.

# Example: [1, 2, 2, 3, 3, 3, 4] → {1, 2, 3, 4}

mylist = [1, 2, 2, 3, 3, 3, 4]
print(set(mylist))





# You have a list of students with duplicate names. Store only unique names and print them in sorted order.

names = ["sarah","ali","ahmed","sarah","amir","ali","ahmed","kashif","sana","azhar","ali","amir"]

unique_names=set(names)
print(sorted(unique_names))