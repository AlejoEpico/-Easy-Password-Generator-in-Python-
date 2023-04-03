import random

print('Welcome, this program generates passwords')
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>?'

number = input('Amount of password to generate: ')
number = int(number)

lenght = input('Input your password lenght: ')
lenght = int(lenght)

print ('\n this is your new password enjoy it!: ')

for pwd in range(number):
    password = ''
    for c in range(lenght):
        password += random.choice(chars)
    print(password)