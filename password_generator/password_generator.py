# Code by @AmirMotefaker

# Password Generator

# Sep-by-Step
# 1- Store all the characters as a list. We can use the string module of Python or type all of them.
# 2- Ask the user to enter the length of the password.
# 3- Shuffle the characters using the random.shuffle method.
# 4- Initialize an empty list to store the password.
# 5- Write a loop that iterates length times.
# 6- Pick a random character from all the characters using the random.choice method.
# 7- Append the random character to the password.
# 8- Shuffle the resultant password list to make it more random.
# 9- Convert the password list to string using the join method.
# 10- Print the password.

import string, random

# characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	# length of password from the user
	length = int(input("Enter password length: "))

	# shuffling the characters
	random.shuffle(characters)
	
	# picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	# shuffling the resultant password
	random.shuffle(password)

	# converting the list to string
	# printing the list
	print("".join(password))


# invoking the function
generate_random_password()
