def is_strong_password(password):
    '''This function checks if the password is strong'''
    if len(password)<8:
        return False
    if not any (char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True

#call the function
print(is_strong_password("WeakPwd"))
print(is_strong_password("Str0ngPwd$"))