import hashlib

# Function to hash the input data
def hash_data(input_data):
    # Encode the input string to bytes, then hash it using SHA256
    hash_object = hashlib.sha256(input_data.encode())
    # Return the hexadecimal representation of the hash
    return hash_object.hexdigest()

# Function to simulate "unhashing" by comparing the stored hash with the new hash of input data
def unhash_data(input_data, stored_hash):
    # Hash the input data
    new_hash = hash_data(input_data)
    # Compare it with the stored hash
    if new_hash == stored_hash:
        return True  # The data matches the stored hash
    else:
        return False  # The data does not match

# Example usage
if __name__ == "__main__":
    # Original data
    original_data = "secret_password"
    
    # Hash the original data
    hashed_data = hash_data(original_data)
    print(f"Original data: {original_data}")
    print(f"Hashed data: {hashed_data}")

    # Simulating "unhashing" by verifying the original data with the hash
    data_to_verify = "secret_password"  # Change this to test with different data
    if unhash_data(data_to_verify, hashed_data):
        print("Data matches the hash!")
    else:
        print("Data does not match the hash!")
