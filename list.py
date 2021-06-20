number = [11, 23, 54, 21, 76]
print(number[2]) # two Number Index
#print(number[2:]) # two Number Index and then others Index
#print(number[-2]) # Minus two Number Index

values = [9.5, 'Maruf', 9]
print(values)

addList = [number, values] #add two list
print(addList)

number.insert(2, 111) #inser 111 value into index two
print(number)

number.remove(21) #delete 21 value from list
print(number)

number.pop(2)  #delete 2 number of Index from list
print(number)

number.pop()  #delete without Index number from list so last number will delete cz
# Data structure is Stack and LIFO, two method is PUSH & POP
print(number)

number.extend([101, 102, 103])
print(number)

del number[2:] #delete multiple Index
# print(number)

sum(number)
print(number)

number.sort()
print(number)