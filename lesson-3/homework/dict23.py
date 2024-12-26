# Check for Common Keys: Given two dictionaries, check if they have any keys in common.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
common_keys = set(dict1.keys()).intersection(dict2.keys())
print(common_keys)