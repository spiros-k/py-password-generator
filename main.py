low_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]

password_low = int(input("How many lower letters do you want your password to have?\n"))
password_cap = int(input("How many capital letters do you want your password to have?\n"))
password_num = int(input("How many numbers do you want your password to have?\n"))
password_sym = int(input("How many symbols do you want your password to have?\n"))

import random

password = ""

for low in range(0, password_low):
    password += random.choice(low_letters)
    
for cap in range(0, password_cap):
    password += random.choice(capital_letters)
  
for num in range(0, password_num):
    password += random.choice(numbers)
  
for sym in range(0, password_sym):
    password += random.choice(symbols)

# generated_password = random.shuffle(password)

print(password)