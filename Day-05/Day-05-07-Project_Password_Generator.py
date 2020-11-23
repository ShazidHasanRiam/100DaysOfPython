#Day-05 of 100 Days of Coding
#November 23, 2020
#Shazid Hasan Riam

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
           'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Solution
# password = ""
#
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
#     # print(password)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
#
# print(password)

#Perfect Solution
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
    # print(password)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# print(password_list)
random.shuffle(password_list)
# print(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your final password is: {password}")