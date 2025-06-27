## Exception handling
# try:
#     a=b
# except NameError as ex:
#     print(ex)

# try:
#     result = 12/0
# except ZeroDivisionError as ex:
#     print(ex)
#     print("Denominator can not be 0.")


# try:
#     result = 10/2
#     a=b
# except ZeroDivisionError as ex:
#     print(ex)
# except Exception as ex:
#     print(ex)
#     print("Main exception got caught here")

# try:
#     num = int(input("Enter a number: "))
#     result = 10/num
# except ValueError: # if string input
#     print("This is a not a valid number.")
# except ZeroDivisionError:
#     print("Enter denominator different form 0.")
# except Exception as ex:
#     print(ex)

# else block executes if the try us successful
# try:
#     num = int(input("Enter a number: "))
#     result = 10/num
# except ValueError: # if string input
#     print("This is a not a valid number.")
# except ZeroDivisionError:
#     print("Enter denominator different form 0.")
# except Exception as ex:
#     print(ex)
# else:
#     print(f"The result is {result}")

# finally block executes either ways 
try:
    num = int(input("Enter a number: "))
    result = 10/num
except ValueError: # if string input
    print("This is a not a valid number.")
except ZeroDivisionError:
    print("Enter denominator different form 0.")
except Exception as ex:
    print(ex)
else:
    print(f"The result is {result}")
finally:
    print("Execution complete.")