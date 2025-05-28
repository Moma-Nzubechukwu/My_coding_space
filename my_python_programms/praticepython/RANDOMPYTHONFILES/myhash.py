import hashlib

def hash_string(input_string):
    # Create a new SHA-256 hash object
    hash_object = hashlib.sha256()

    # Convert the input string to bytes and update the hash object
    hash_object.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_string = hash_object.hexdigest()

    return hashed_string

# Example usage:
"""
input_str = "Hello, World!"
hashed_str = hash_string(input_str)

print(f"Input: {input_str}")
print(f"Hashed: {hashed_str}")
"""
fileobj = open('words.txt', 'r')
file = fileobj.read()
home = hash_string(file)
print(home)

