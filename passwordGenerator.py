import random
import string

def generate_random_password(length=12):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the remaining length of the password
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the characters to ensure randomness
    random.shuffle(password)
    
    # Combine the list into a string and return
    return ''.join(password)

# Example usage
password = generate_random_password(12)
print("\n\n",f"Generated password: {password}\n\n")
