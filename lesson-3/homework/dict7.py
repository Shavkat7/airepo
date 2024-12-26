# Remove Key: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.

my_dict = {"a": 1, "b": 2, "c": 3}
key_to_remove = "b"
my_dict.pop(key_to_remove, None)
print(my_dict)