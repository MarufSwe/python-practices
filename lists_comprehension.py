# Example 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

# Normal loop way
for x in fruits:
    if "e" in x:
        newList.append(x)
print(newList)

#List Comprehension way
# aList = [x for x in fruits if "a" in x]  # way 1
aList = [x for x in fruits if x.startswith("a")] # way 2
print(aList)

# Example 2
val = [4, -4, 2]
res = [4*x for x in val]
print('Multiplication 4 with all index: ', res)

# Example 3
name_year = [("Maruf", 1995), ("Mamun", 1991), ("Eya", 1996), ("China", 1975), ("Mahatab", 1965)]
name_res = [title for (title, year) in name_year if year > 1990]
print('show name and year before 1990: ', name_res)

# Example 4
# Cartesian Product
A = [1, 3]
B = [2, 4]
cartesian_product = [(a, b) for a in A for b in B]
print('cartesian_product is: ', cartesian_product)