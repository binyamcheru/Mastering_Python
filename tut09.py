empty_tuple = ()
# empty_tuple = tuple()
print(type(empty_tuple))

numbers = tuple([5,8,3,1,3,4])
print(numbers)

mixed_tuple = (1,"hello",True)
print(mixed_tuple)

print(numbers[0])
print(numbers[::-1])

## Tuple operation
concat_tuple = numbers + mixed_tuple
print(concat_tuple)

print(mixed_tuple*3)

# Tuples are immutable
# numbers[0] = 100 # ERROR: tuple' object does not support item assignment

# Tuple methods
print(numbers.count(5))
print(numbers.index(3))


## Packing and Unpacking tuples  
packed_tuple = 1,"hello",False,31.5
print(packed_tuple)

a,b,c,d = packed_tuple # unpacking tuple
print(a,b,c,d)

# Unpacking with *
first,*middle,last = numbers
print(first,middle,last)

## Nested tuples
nested_tuple = ((45,54),(False,"se"),(1,21,"hkk"))
print(nested_tuple[2][0])

# Iterating over a nested tuple
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item,end=" ")