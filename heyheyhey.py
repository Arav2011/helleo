import random
import string

# Get the password length from the user
length = int(input("Enter the password length: "))

# Characters to use in the password
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Generate the password
password = "".join(random.choice(characters) for _ in range(length))

# Shuffle the password
password_list = list(password)
random.shuffle(password_list)
password = "".join(password_list)

# Display the password
print("Random Password:", password)