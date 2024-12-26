# Find Keys with Value: Given a dictionary and a value, create a list of all keys that have that value.

my_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
value_to_find = 1
keys_with_value = [k for k, v in my_dict.items() if v == value_to_find]
print(keys_with_value)