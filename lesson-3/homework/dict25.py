# Get the First Key-Value Pair: Retrieve the first key-value pair from a dictionary.

my_dict = {"a": 1, "b": 2, "c": 3}
first_key_value = next(iter(my_dict.items()), "Dictionary is empty")
print(first_key_value)