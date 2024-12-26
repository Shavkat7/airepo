# Get Value: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.

my_dict = {"a": 1, "b": 2, "c": 3}
key = "b"
value = my_dict.get(key, "Key not found")
print(value)