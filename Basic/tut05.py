for i in range(5): # in range the last number isn't included
    print(i)
print()
for j in range(1,10,2): # 2 here is a step range step is 1 by default
    print(j)
print()
for i in range(10,1,-1):
    print(i)

print()
str = "some string here"
for i in str: 
    print(i)


# while loop
count = 0
while count < 5:
    print(count)
    count+=1

print()
# break in py
for i in range(1,10):
    if i == 5:
        break
    print(i)

print()

# continue in py
for i in range(0,10):
    if(i%2==0):
        continue
    print(i)

print()

for i in range(5):
    if i==3:
        pass
    print(i)

print()

for i in range(5):
    if i == 3:
        pass  # do nothing when i == 3
    else:
        print(i)

# 🧠 pass vs continue
# Use pass when you want to do nothing but keep the code valid.

# Use continue when you want to skip the rest of that iteration.

# sum of first N natural numbers
n=int(input("Enter the number: "))
sum=0
for i in range(1,n+1):
    sum+=i

print(f"The sum up to {n}: ",sum)

#Nested loops 
for i in range(3):
    for j in range(2):
        print(f"i: {i} and j:{j}")


# display prime number between the given values

num = int(input("Enter the number: "))

for i in range(2,num+1):
    is_prime = True
    for j in range(2,num+1):
        if(i%j==0 and i!=j):
            is_prime=False
            break
    if is_prime==True:
        print(i)
