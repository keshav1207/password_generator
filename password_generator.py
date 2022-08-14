import random,string

upper = string.ascii_uppercase               # Consist of all Uppercase letters
special = string.punctuation                 # Consist of all special characters
numbers = string.digits                     # Consist of numbers[0-9]
lower = string.ascii_lowercase              # Consist of all Lowercase letters

characters = upper + special + numbers + lower
length = int(input('Enter the required length of the password:   '))

while True:
    password = ''
    numbers_test, upper_test, lower_test, special_test = False,False,False,False
    for i in range(length):
        password += random.choice(characters)

    for l in range(length):
        if password[l]  in upper:
            upper_test = True

        if password[l]  in special:
            special_test = True

        if password[l]  in numbers:
            numbers_test =True

        if password[l]  in lower:
            lower_test = True

    if upper_test == True and lower_test == True and numbers_test == True and special_test == True:
        break

print(f'This is your password: {password}')
