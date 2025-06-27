def convert_temperature(temp,unit):
    """This function converts temp b/n Celsius and Fahrenheit"""
    if unit=="C":
        return temp*9/5 + 32 # Celsius to Fahrenheit
    elif unit=='F':
        return (temp-32)*5/9 # Fahrenheit to Celsius
    else:
        return None
     
print(convert_temperature(25,'C'))
print(convert_temperature(-40,'F'))