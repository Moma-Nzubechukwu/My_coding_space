# Specify the file name and the string to search for
file_name = "example.txt"
search_string = "Namtes"

# Open the file and search for the string
with open(file_name, "r") as file:
    for line_number, line in enumerate(file, start=1):
        # Find all occurrences of the string in the line
        start_index = 0
        while True:
            start_index = line.find(search_string, start_index)
            if start_index == -1:  # No more occurrences
                break
            print(f"Found '{search_string}' on line {line_number}, position {start_index}")
            start_index += 1  # Move past the last found occurrence
