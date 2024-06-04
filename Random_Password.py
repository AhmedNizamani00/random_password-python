import random
import string

pass_len = 10
CharValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(CharValues)

print("Your Random Password is:", password)
