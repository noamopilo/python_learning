# collect user preferences
#  - lenght
#  - should contain uppercase
#  - should contain special
#  - should contain digits

# get all availaible characthers
# randomly pick charachthers up to the lenght
# ensure we have at least 1 of each characther type
# ensure lenght is valid

import random
import string

def generate_password():
    length = int(input("Enter the desired pass length: ").strip())
    include_uppercase = input("Include uppercase letters? (Y/N): ").strip().lower()
    include_special = input("Include special characters? (Y/N): ").strip().lower()
    include_digits = input("Include digits? (Y/N): ").strip().lower()
    
    if length < 4:
        print("Password length must be at least 4 characters.")
        return
    
    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "y" else ""
    special = string.punctuation if include_special == "y" else ""
    digits = string.digits if include_digits == "y" else ""
    all_characters = lower + uppercase + special + digits
    
    required_characters = []
    if include_uppercase == "y":
        required_characters.append(random.choice(uppercase))
    if include_special == "y":
        required_characters.append(random.choice(special))
    if include_digits == "y":
        required_characters.append(random.choice(digits))
        
    remaining_lenght = length - len(required_characters)
    password = required_characters
    
    for _ in range(remaining_lenght):
        character = random.choice(all_characters)
        password.append(character)
    
    random.shuffle(password)
    str_password = "".join(password)
    return str_password
    
password = generate_password()
print(password)