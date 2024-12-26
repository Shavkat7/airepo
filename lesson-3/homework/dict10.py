# Get Key-Value Pair: Given a dictionary and a key, retrieve the key-value pair if the key exists.

my_dict = {"a": 1, "b": 2, "c": 3}
key = "b"
key_value_pair = (key, my_dict[key]) if key in my_dict else "Key not found"
print(key_value_pair)