#1. create a list of random number of dicts (from 2 to 10)
import random
import string
# Function to generate a random dictionary
def generate_random_dict():
    num_keys = random.randint(2, 10)
    keys = random.sample(string.ascii_lowercase, num_keys)
    random_dict = {key: random.randint(0, 100) for key in keys}
    return random_dict
# Create a list of random dictionaries
num_dicts = random.randint(2, 10)
list_of_dicts = []
# Populate the list with random dictionaries
for _ in range(num_dicts):
    random_dict = generate_random_dict()
    list_of_dicts.append(random_dict)

# 2. Previously generated list of dictionaries
print(list_of_dicts)
# Create a common dictionary
common_dict = {}

# Iterate through the list of dictionaries
for idx, dictionary in enumerate(list_of_dicts, start=1):
    for key, value in dictionary.items():
        if key in common_dict:
            # If key already exists, update the value to the maximum of the current and new value
            common_dict[key] = max(common_dict[key], value)
            # Rename the key to include the dict number with max value
            common_dict[f"{key}_{idx}"] = common_dict.pop(key)
        else:
            # If key is not in common_dict, add it with the current value
            common_dict[key] = value

# Print the result
print(common_dict)