# Creating a dictionary
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Accessing values by key
value = my_dict['key1']

# Adding a key-value pair
my_dict['key4'] = 'value4'

# Updating a value by key
my_dict['key1'] = 'new_value1'

# Removing a key-value pair by key
del my_dict['key2']

# Checking if a key exists
key_exists = 'key3' in my_dict

# Getting a list of keys
keys_list = list(my_dict.keys())

# Getting a list of values
values_list = list(my_dict.values())

# Iterating through the dictionary
for key, value in my_dict.items():
    print(key, value)

# Checking the length of the dictionary
dict_length = len(my_dict)
