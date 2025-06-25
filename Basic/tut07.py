# to create a set we just use a {}
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))

empty_set = set()
print(type(empty_set))

list_to_set = set([0,1,2,5,5])
print(type(list_to_set))
print(list_to_set)


## set methods 
numbers = {0,1,2,3,4,5,6}
numbers.add(7)
numbers.add(7) 
numbers.remove(0) 
# numbers.remove(10)   # error because 10 doesn't exist in the set so we use the discard method
numbers.discard(10)

print(numbers)


popped_element = numbers.pop()
print(popped_element) # it removes the first entry not the last
print(numbers)

# numbers.clear() # clear all the elements

# Set membership test 
print(3 in numbers) # true
print(10 in numbers) # false

# Mathematical Operations
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

## Union
union_set = set1.union(set2)
print(union_set)

## Intersection
intersection_set = set1.intersection(set2)
print(intersection_set)

# set1.intersection_update(set2) # updates the set1 to the common elements
# print(set1)

# Difference
diff_set = set1.difference(set2)
print(diff_set)

# symmetric difference => common elements are removed

symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)

# Set Methods
set3 = {1,2,3,4,5,6}
set4 = {1,5,3}

print(set3.issubset(set4))
print(set3.issuperset(set4))

# Counting unique words 
text = "Today is such a beautiful day to learn python."
words = text.split()
unique_words = set(words)
print(unique_words)
print(len(unique_words))