# Import required modules
import random
import string

# Create character pool
 
characters = string.ascii_letters + string.digits + string.punctuation
#ascii_letters → a-z + A-Z
#digits → 0-9
#punctuation → symbols

# Take user input

length = int(input("Enter password length: "))

#Generate password

password = ""
for i in range(length):
    password += random.choice(characters)

# Display the generated password
print("Generated Password:",password)