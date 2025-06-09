
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 20}

# Get a list of values
values_list = list(my_dict.values())

# Find the index of a specific value
value_to_find = 20
index = values_list.index(value_to_find)

print(f"The index of {value_to_find} is {index}")

indexes = [i for i, v in enumerate(values_list) if v == value_to_find]
print(f"Indexes of {value_to_find}: {indexes}")
