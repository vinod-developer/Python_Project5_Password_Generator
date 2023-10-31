#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# The below sum is used if we go with sample() in L28
# sum = nr_letters + nr_symbols + nr_numbers

random_letters = random.sample(letters, nr_letters)
random_symbols = random.sample(symbols, nr_symbols)
random_numbers = random.sample(numbers, nr_numbers)

# ALTERNATE WAY - Also lists can be combined like this random_letters + symbols + numbers
combined_list = []
combined_list.extend(random_letters)
combined_list.extend(random_symbols)
combined_list.extend(random_numbers)

random.shuffle(combined_list)
print(combined_list)

#  ALTERNATE WAY BY USING sample() function - hard_random_password = random.sample(combined_list, sum)
# print(hard_random_password)
result = ""
for i in combined_list:
    result += i
print(f"Your password is {result}")





