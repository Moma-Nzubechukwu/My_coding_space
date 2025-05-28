# Simple custom hash function (Sum of ASCII values modulo a prime number)
def custom_hash(input_data):
    hash_value = 0
    # Iterate through each character in the input string
    for char in input_data:
        hash_value += ord(char)  # Add ASCII value of each character to the hash value
    # Return the hash value modulo a large prime number (to avoid overflow)
    return hash_value % 1000000007

# Function to simulate "unhashing" by comparing the hash
def unhash_data(input_data, stored_hash):
    # Calculate the hash for the input data
    new_hash = custom_hash(input_data)
    # Compare it with the stored hash
    if new_hash == stored_hash:
        return True  # The data matches the stored hash
    else:
        return False  # The data does not match

# Example usage
if __name__ == "__main__":
    # Original data
    original_data = "secret_password"
    
    # Hash the original data using the custom hash function
    hashed_data = custom_hash(original_data)
    print(f"Original data: {original_data}")
    print(f"Custom hashed data: {hashed_data}")

    # Simulating "unhashing" by verifying the original data with the hash
    data_to_verify = "secret_password"  # Change this to test with different data
    if unhash_data(data_to_verify, hashed_data):
        print("Data matches the hash!")
    else:
        print("Data does not match the hash!")
