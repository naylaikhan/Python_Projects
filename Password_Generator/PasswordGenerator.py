import random

letters=[
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
  "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
numbers=[
  "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]
symbols=[
  "!", "@", "#", "$", "%", "^", "&", "*", "(", ")"
]

print("Welcome to the Password Generator!")
letters_choice = int(input("How many letters would you want in your password?\n "))
symbols_choice=int(input("How many symbols would you like?\n "))
numbers_choice=int(input("How many numbers would you like? \n"))

password_list=[]
for char in range(0,letters_choice):
    password_list.append(random.choice(letters))

for char in range(0,symbols_choice):
    password_list.append(random.choice(symbols))

for char in range(0,numbers_choice):
    password_list.append(random.choice(numbers))

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

password= "" 
for char in password_list:
    password+=char

print(f"Your Password is : {password}")


