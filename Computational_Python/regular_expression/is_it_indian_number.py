def isPhoneNumber(text):
    if len(text) != 14:
        return False 
    if text[0] != '+':
        return False
    for i in range(1,2):
        if not text[i].isdecimal():
            return False 
        if text[3] != '-':
            return False
            
    return True

print('Is +91-8940383848 a phone number?')
print(isPhoneNumber('+91-8940383848'))