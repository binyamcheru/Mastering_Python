# lst = []
# print(type(lst))  # <class 'list'>

# mixed_list = ["John","Jack",1,2,4,True]
# print(mixed_list) 

# # accessing elements using an index
# print(mixed_list[0]) 
# print(mixed_list[-1]) # prints the last element

# # accessing elements using 
# print(mixed_list[1:]) # prints all starting from the second element to the last
# print(mixed_list[1:3]) # prints index 1 and 2 but not 3
# print(mixed_list[-1:])
# print(mixed_list[-1:-3]) # ???

# # modifying elements 
# mixed_list[1:] = "each letter"
# print(mixed_list)


# # function with list
# fruits = ["apple","banana","cherry"]
# fruits.append("orange")
# print(fruits)
# fruits.insert(1,"watermelon") # insert(index,value)
# print(fruits)
# fruits.remove("banana") # remove(value) = removes the first occurrence of an item
# popped_fruit = fruits.pop()
# print(fruits)
# print(popped_fruit)
# fruits.append("banana")
# fruits.append("banana")
# index = fruits.index("banana") 
# print(index)

# print(fruits.count("banana"))

# # Sorting lists in ascending order
# fruits.sort()
# print(fruits)

# fruits.reverse()
# print(fruits)

# fruits.clear() # remove all the elements
# print(fruits)

# #slicing list

# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[2:5])
# print(numbers[5:])
# print(numbers[:5])
# print(numbers[::]) # double colon means just list all elements
# print(numbers[::2]) # 2 is the step
# print(numbers[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(numbers[::-2])

## Iterating over the list

# for number in numbers:
#     print(number)

# for index,number in enumerate(numbers):
#     print(f"index: {index} => value: {number}")


## List comprehension
# lst=[]
# for x in range(10):
#     lst.append(x**2)

# print(lst)

# if you use list comprehension
squareList = [x**2 for x in range(10)]
print(squareList)

## NB:
# Basic Syntax: [expression for item in iterable]
# with conditional logic: [expression for item in iterable if condition]
# Nested list comprehension: [expression for item1 in iterable1 for item2 in iterable2]

# evenList = []
# for i in range(10):
#     if(i%2==0):
#         evenList.append(i)

# print(evenList)

evenList = [i for i in range(10) if i%2==0]
print(evenList)

# Nested list comprehension

lst1 = [1,2,3]
lst2 = ['a','b','c','d']

pair = [[i,j] for i in lst1 for j in lst2]

print(pair)

# Interesting example
words = ["hello","world","python","list","comprehension"]
lengths = [len(word) for word in words]
print(lengths) #Output: [5, 5, 6, 4, 13]