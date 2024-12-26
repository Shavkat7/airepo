# Get Nested Value: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.

my_dict = {"a": 1, "b": {"nested": 2}, "c": 3}
nested_key = "b"
inner_key = "nested"
nested_value = my_dict.get(nested_key, {}).get(inner_key, "Key not found")
print(nested_value)