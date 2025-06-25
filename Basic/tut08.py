# empty_dict = {}
# print(type(empty_dict))

empty_dict = dict()
print(type(empty_dict))

student = {"name":"John","age":32,"grade":9}
print(student)
print(type(student))

# accessing dictionary elements
print(student['name'])

# using the get() method
print(student.get('name'))
print(student.get('not_exist')) # Output: None
print(student.get('not_exist',"Not Available")) #give a default value # Output: Not Available

# Modifying a dictionary
student['age'] = 16
print(student)
student['address'] = "USA" # add new key, value pair
print(student)

del student['grade'] # delete the key and value pair
print(student)

# Dictionary methods
keys = student.keys()
print(keys)
values = student.values()
print(values)
items = student.items() # get all key, value pairs
print(items)

print()
print()
# NB: common error => Shallow copy
student_copy = student
print(student_copy)

# now change value on the student dict
student['name'] = "Johnathan"
print(student) # Output: {'name': 'Johnathan', 'age': 16, 'address': 'USA'}
print(student_copy) # Output: {'name': 'Johnathan', 'age': 16, 'address': 'USA'}

## Fix the above error using copy()
student_copy1 = student.copy()
student['age'] = 15
print(student) # Output: {'name': 'Johnathan', 'age': 15, 'address': 'USA'}
print(student_copy1) # Output: {'name': 'Johnathan', 'age': 16, 'address': 'USA'}

#Iterating over the dict

# iterating over keys
for key in student.keys():
    print(key)

# iterating over values
for value in student.values():
    print(value)

# iterating over key value pairs
# for item in student.items():
#     key,value = item
#     print(f"{key}:{value}")
for key,value in student.items():
    print(f"{key}:{value}")

    #Nested Dictionaries
    students = {
        "student1":{'name': 'Johnathan', 'age': 16, 'address': 'USA'},
        "student2":{'name': 'Peter', 'age': 16, 'address': 'USA'},
    }

print(students)
print(students['student1']['name'])

## Iterating over nested dict
for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")

## Dictionary comprehension
squares = {i:i**2 for i in range(5)}
print(squares)

even_squares = {i:i**2 for i in range(10) if i%2==0}
print(even_squares)

## Practical e.g: count frequency of elements in list

lst = [1,2,4,5,4,5,2,2,4,8,9,4,1,3,4,4,5,6]
frequency = {}
for i in lst:
    if(i in frequency.keys()):
        frequency[i]+=1
    else:
        frequency[i]=1
    
print(frequency)

## Merge two dictionaries
dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}
merged_dict = {**dict1,**dict2}
print(merged_dict)