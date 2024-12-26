# Check for Nested Dictionaries: Given a dictionary, check if any values are also dictionaries.

my_dict = {"a": 1, "b": {"nested": 2}, "c": 3}
has_nested = any(isinstance(v, dict) for v in my_dict.values())
print(has_nested)